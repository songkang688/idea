import torch

from vpt_registers.tiny_vit import Attention, DenseHead, TinyViT, ViTConfig


def _model(num_registers=0):
    return TinyViT(ViTConfig(image_size=16, patch_size=4, dim=24, depth=2, heads=2,
                             num_registers=num_registers))


def test_forward_shapes_no_prompt():
    m = _model()
    out = m(torch.randn(2, 3, 16, 16))
    assert out["patch_tokens"].shape == (2, 16, 24)
    assert out["prompt_tokens"] is None
    assert out["register_out"] is None


def test_forward_shapes_with_prompt_and_registers():
    m = _model(num_registers=3)
    prompt = torch.randn(2, 24)
    out = m(torch.randn(2, 3, 16, 16), prompt=prompt, capture_attn=True)
    assert out["patch_tokens"].shape == (2, 16, 24)
    assert out["prompt_tokens"].shape == (2, 2, 24)
    assert out["register_out"].shape == (2, 3, 24)
    assert len(out["attn"]) == 2
    T = 2 + 3 + 16
    assert out["attn"][0].shape == (2, 2, T, T)
    # attention rows are probability distributions
    assert torch.allclose(out["attn"][0].sum(-1), torch.ones(2, 2, T), atol=1e-5)


def test_prompt_injection_changes_patch_features():
    m = _model()
    x = torch.randn(2, 3, 16, 16)
    base = m(x)["patch_tokens"]
    with_prompt = m(x, prompt=torch.randn(4, 24))["patch_tokens"]
    assert not torch.allclose(base, with_prompt)


def test_attention_value_zeroing_matches_reference():
    """Exact check of the sink mechanism: with value_zero_slots=s, the
    layer's output must equal a reference recomputation in which the value
    rows of s are literally zeroed (keys/queries untouched)."""
    torch.manual_seed(0)
    attn = Attention(dim=24, heads=2)
    x = torch.randn(2, 8, 24)
    out, probs = attn(x, value_zero_slots=slice(0, 3), capture=True)
    qkv = attn.qkv(x).reshape(2, 8, 3, 2, 12)
    q, k, v = qkv.permute(2, 0, 3, 1, 4)
    v = v.clone()
    v[:, :, 0:3, :] = 0.0
    ref_probs = ((q @ k.transpose(-2, -1)) * attn.scale).softmax(-1)
    ref = attn.proj((ref_probs @ v).transpose(1, 2).reshape(2, 8, 24))
    assert torch.allclose(out, ref, atol=1e-6)
    assert torch.allclose(probs, ref_probs, atol=1e-6)


def test_sink_mode_absorbs_attention_but_differs_from_content_mode():
    """Behavioral check at model level: sink mode must differ both from
    content mode (values matter there) and from no-token (keys still absorb
    attention mass and change the geometry)."""
    m = _model()
    x = torch.randn(2, 3, 16, 16)
    torch.manual_seed(0)
    p = torch.randn(3, 24)
    out_sink = m(x, prompt=p, prompt_is_sink=True)["patch_tokens"]
    out_content = m(x, prompt=p, prompt_is_sink=False)["patch_tokens"]
    out_none = m(x)["patch_tokens"]
    assert not torch.allclose(out_sink, out_content)
    assert not torch.allclose(out_sink, out_none)


def test_backbone_identical_across_arms():
    """Arms own their prompt params; the backbone must stay bit-identical."""
    m = _model()
    before = {k: v.clone() for k, v in m.state_dict().items()}
    m(torch.randn(2, 3, 16, 16), prompt=torch.randn(4, 24))
    for k, v in m.state_dict().items():
        assert torch.equal(before[k], v)


def test_dense_head_linear_and_conv_shapes():
    for kind in ("linear", "conv"):
        head = DenseHead(24, num_labels=4, patch_size=4, kind=kind)
        tokens = torch.randn(2, 16, 24)
        logits = head(tokens, grid=4)
        assert logits.shape == (2, 4, 16, 16), kind


def test_dense_head_linear_is_per_patch_local():
    """The linear head must be a per-patch readout: changing one patch token
    changes only that patch's pixels."""
    head = DenseHead(24, num_labels=4, patch_size=4, kind="linear")
    tokens = torch.randn(1, 16, 24)
    base = head(tokens, grid=4)
    tokens2 = tokens.clone()
    tokens2[0, 5] += 1.0  # patch (row 1, col 1)
    out = head(tokens2, grid=4)
    diff = (out - base).abs().sum(dim=1)[0]  # (16, 16)
    changed = diff > 1e-8
    expect = torch.zeros(16, 16, dtype=torch.bool)
    expect[4:8, 4:8] = True
    assert torch.equal(changed, expect)

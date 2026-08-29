# IDEA-C- raw ideas
count=416

### IDEA-C-0001
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SAM-OBJECTNESS.
- Problem: Papers about SAM-OBJECTNESS rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If SAM family fails on amorphous targets because it encodes an objectness prior, not because the encoder lacks features. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SAM-OBJECTNESS.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SAM-OBJECTNESS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-OBJECTNESS

### IDEA-C-0002
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SAM-OBJECTNESS.
- Problem: Papers about SAM-OBJECTNESS rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If SAM family fails on amorphous targets because it encodes an objectness prior, not because the encoder lacks features. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SAM-OBJECTNESS.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SAM-OBJECTNESS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-OBJECTNESS

### IDEA-C-0003
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SAM-OBJECTNESS.
- Problem: Papers about SAM-OBJECTNESS rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If SAM family fails on amorphous targets because it encodes an objectness prior, not because the encoder lacks features. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SAM-OBJECTNESS.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SAM-OBJECTNESS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-OBJECTNESS

### IDEA-C-0004
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SAM-OBJECTNESS.
- Problem: Papers about SAM-OBJECTNESS rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If SAM family fails on amorphous targets because it encodes an objectness prior, not because the encoder lacks features. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SAM-OBJECTNESS.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SAM-OBJECTNESS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-OBJECTNESS

### IDEA-C-0005
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SAM-OBJECTNESS.
- Problem: Papers about SAM-OBJECTNESS rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If SAM family fails on amorphous targets because it encodes an objectness prior, not because the encoder lacks features. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SAM-OBJECTNESS.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SAM-OBJECTNESS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-OBJECTNESS

### IDEA-C-0006
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SAM-OBJECTNESS.
- Problem: Papers about SAM-OBJECTNESS rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If SAM family fails on amorphous targets because it encodes an objectness prior, not because the encoder lacks features. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SAM-OBJECTNESS.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SAM-OBJECTNESS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-OBJECTNESS

### IDEA-C-0007
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SAM-OBJECTNESS.
- Problem: Papers about SAM-OBJECTNESS rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If SAM family fails on amorphous targets because it encodes an objectness prior, not because the encoder lacks features. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SAM-OBJECTNESS.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SAM-OBJECTNESS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-OBJECTNESS

### IDEA-C-0008
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SAM-OBJECTNESS.
- Problem: Papers about SAM-OBJECTNESS rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If SAM family fails on amorphous targets because it encodes an objectness prior, not because the encoder lacks features. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SAM-OBJECTNESS.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SAM-OBJECTNESS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-OBJECTNESS

### IDEA-C-0009
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SAM-TEXTURE.
- Problem: Papers about SAM-TEXTURE rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If SFM failures on vessels/smoke are caused by texture-as-object confusion, not missing capacity. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SAM-TEXTURE.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SAM-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-TEXTURE

### IDEA-C-0010
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SAM-TEXTURE.
- Problem: Papers about SAM-TEXTURE rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If SFM failures on vessels/smoke are caused by texture-as-object confusion, not missing capacity. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SAM-TEXTURE.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SAM-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-TEXTURE

### IDEA-C-0011
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SAM-TEXTURE.
- Problem: Papers about SAM-TEXTURE rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If SFM failures on vessels/smoke are caused by texture-as-object confusion, not missing capacity. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SAM-TEXTURE.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SAM-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-TEXTURE

### IDEA-C-0012
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SAM-TEXTURE.
- Problem: Papers about SAM-TEXTURE rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If SFM failures on vessels/smoke are caused by texture-as-object confusion, not missing capacity. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SAM-TEXTURE.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SAM-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-TEXTURE

### IDEA-C-0013
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SAM-TEXTURE.
- Problem: Papers about SAM-TEXTURE rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If SFM failures on vessels/smoke are caused by texture-as-object confusion, not missing capacity. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SAM-TEXTURE.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SAM-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-TEXTURE

### IDEA-C-0014
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SAM-TEXTURE.
- Problem: Papers about SAM-TEXTURE rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If SFM failures on vessels/smoke are caused by texture-as-object confusion, not missing capacity. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SAM-TEXTURE.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SAM-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-TEXTURE

### IDEA-C-0015
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SAM-TEXTURE.
- Problem: Papers about SAM-TEXTURE rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If SFM failures on vessels/smoke are caused by texture-as-object confusion, not missing capacity. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SAM-TEXTURE.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SAM-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-TEXTURE

### IDEA-C-0016
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SAM-TEXTURE.
- Problem: Papers about SAM-TEXTURE rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If SFM failures on vessels/smoke are caused by texture-as-object confusion, not missing capacity. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SAM-TEXTURE.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SAM-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-TEXTURE

### IDEA-C-0017
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SAM-PROMPT-GEOM.
- Problem: Papers about SAM-PROMPT-GEOM rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Point vs box vs mask prompt performance gaps are explained by spatial support mismatch with target topology, not 'box is better' as a universal rule. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SAM-PROMPT-GEOM.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SAM-PROMPT-GEOM intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-PROMPT-GEOM

### IDEA-C-0018
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SAM-PROMPT-GEOM.
- Problem: Papers about SAM-PROMPT-GEOM rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Point vs box vs mask prompt performance gaps are explained by spatial support mismatch with target topology, not 'box is better' as a universal rule. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SAM-PROMPT-GEOM.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SAM-PROMPT-GEOM intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-PROMPT-GEOM

### IDEA-C-0019
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SAM-PROMPT-GEOM.
- Problem: Papers about SAM-PROMPT-GEOM rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Point vs box vs mask prompt performance gaps are explained by spatial support mismatch with target topology, not 'box is better' as a universal rule. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SAM-PROMPT-GEOM.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SAM-PROMPT-GEOM intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-PROMPT-GEOM

### IDEA-C-0020
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SAM-PROMPT-GEOM.
- Problem: Papers about SAM-PROMPT-GEOM rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Point vs box vs mask prompt performance gaps are explained by spatial support mismatch with target topology, not 'box is better' as a universal rule. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SAM-PROMPT-GEOM.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SAM-PROMPT-GEOM intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-PROMPT-GEOM

### IDEA-C-0021
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SAM-PROMPT-GEOM.
- Problem: Papers about SAM-PROMPT-GEOM rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Point vs box vs mask prompt performance gaps are explained by spatial support mismatch with target topology, not 'box is better' as a universal rule. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SAM-PROMPT-GEOM.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SAM-PROMPT-GEOM intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-PROMPT-GEOM

### IDEA-C-0022
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SAM-PROMPT-GEOM.
- Problem: Papers about SAM-PROMPT-GEOM rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Point vs box vs mask prompt performance gaps are explained by spatial support mismatch with target topology, not 'box is better' as a universal rule. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SAM-PROMPT-GEOM.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SAM-PROMPT-GEOM intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-PROMPT-GEOM

### IDEA-C-0023
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SAM-PROMPT-GEOM.
- Problem: Papers about SAM-PROMPT-GEOM rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Point vs box vs mask prompt performance gaps are explained by spatial support mismatch with target topology, not 'box is better' as a universal rule. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SAM-PROMPT-GEOM.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SAM-PROMPT-GEOM intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-PROMPT-GEOM

### IDEA-C-0024
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SAM-PROMPT-GEOM.
- Problem: Papers about SAM-PROMPT-GEOM rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Point vs box vs mask prompt performance gaps are explained by spatial support mismatch with target topology, not 'box is better' as a universal rule. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SAM-PROMPT-GEOM.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SAM-PROMPT-GEOM intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-PROMPT-GEOM

### IDEA-C-0025
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SAM-IOU-CAL.
- Problem: Papers about SAM-IOU-CAL rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If SAM IoU tokens are calibrated on SA-1B objects and systematically miscalibrated on low-contrast/amorphous masks. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SAM-IOU-CAL.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SAM-IOU-CAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-IOU-CAL

### IDEA-C-0026
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SAM-IOU-CAL.
- Problem: Papers about SAM-IOU-CAL rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If SAM IoU tokens are calibrated on SA-1B objects and systematically miscalibrated on low-contrast/amorphous masks. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SAM-IOU-CAL.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SAM-IOU-CAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-IOU-CAL

### IDEA-C-0027
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SAM-IOU-CAL.
- Problem: Papers about SAM-IOU-CAL rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If SAM IoU tokens are calibrated on SA-1B objects and systematically miscalibrated on low-contrast/amorphous masks. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SAM-IOU-CAL.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SAM-IOU-CAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-IOU-CAL

### IDEA-C-0028
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SAM-IOU-CAL.
- Problem: Papers about SAM-IOU-CAL rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If SAM IoU tokens are calibrated on SA-1B objects and systematically miscalibrated on low-contrast/amorphous masks. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SAM-IOU-CAL.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SAM-IOU-CAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-IOU-CAL

### IDEA-C-0029
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SAM-IOU-CAL.
- Problem: Papers about SAM-IOU-CAL rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If SAM IoU tokens are calibrated on SA-1B objects and systematically miscalibrated on low-contrast/amorphous masks. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SAM-IOU-CAL.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SAM-IOU-CAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-IOU-CAL

### IDEA-C-0030
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SAM-IOU-CAL.
- Problem: Papers about SAM-IOU-CAL rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If SAM IoU tokens are calibrated on SA-1B objects and systematically miscalibrated on low-contrast/amorphous masks. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SAM-IOU-CAL.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SAM-IOU-CAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-IOU-CAL

### IDEA-C-0031
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SAM-IOU-CAL.
- Problem: Papers about SAM-IOU-CAL rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If SAM IoU tokens are calibrated on SA-1B objects and systematically miscalibrated on low-contrast/amorphous masks. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SAM-IOU-CAL.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SAM-IOU-CAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-IOU-CAL

### IDEA-C-0032
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SAM-IOU-CAL.
- Problem: Papers about SAM-IOU-CAL rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If SAM IoU tokens are calibrated on SA-1B objects and systematically miscalibrated on low-contrast/amorphous masks. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SAM-IOU-CAL.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SAM-IOU-CAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-IOU-CAL

### IDEA-C-0033
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SAM-NEGCLICK.
- Problem: Papers about SAM-NEGCLICK rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Negative clicks help objects but harm density fields (smoke/infiltrative tumor) by punching holes in the support. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SAM-NEGCLICK.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SAM-NEGCLICK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-NEGCLICK

### IDEA-C-0034
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SAM-NEGCLICK.
- Problem: Papers about SAM-NEGCLICK rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Negative clicks help objects but harm density fields (smoke/infiltrative tumor) by punching holes in the support. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SAM-NEGCLICK.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SAM-NEGCLICK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-NEGCLICK

### IDEA-C-0035
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SAM-NEGCLICK.
- Problem: Papers about SAM-NEGCLICK rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Negative clicks help objects but harm density fields (smoke/infiltrative tumor) by punching holes in the support. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SAM-NEGCLICK.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SAM-NEGCLICK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-NEGCLICK

### IDEA-C-0036
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SAM-NEGCLICK.
- Problem: Papers about SAM-NEGCLICK rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Negative clicks help objects but harm density fields (smoke/infiltrative tumor) by punching holes in the support. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SAM-NEGCLICK.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SAM-NEGCLICK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-NEGCLICK

### IDEA-C-0037
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SAM-NEGCLICK.
- Problem: Papers about SAM-NEGCLICK rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Negative clicks help objects but harm density fields (smoke/infiltrative tumor) by punching holes in the support. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SAM-NEGCLICK.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SAM-NEGCLICK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-NEGCLICK

### IDEA-C-0038
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SAM-NEGCLICK.
- Problem: Papers about SAM-NEGCLICK rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Negative clicks help objects but harm density fields (smoke/infiltrative tumor) by punching holes in the support. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SAM-NEGCLICK.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SAM-NEGCLICK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-NEGCLICK

### IDEA-C-0039
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SAM-NEGCLICK.
- Problem: Papers about SAM-NEGCLICK rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Negative clicks help objects but harm density fields (smoke/infiltrative tumor) by punching holes in the support. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SAM-NEGCLICK.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SAM-NEGCLICK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-NEGCLICK

### IDEA-C-0040
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SAM-NEGCLICK.
- Problem: Papers about SAM-NEGCLICK rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Negative clicks help objects but harm density fields (smoke/infiltrative tumor) by punching holes in the support. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SAM-NEGCLICK.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SAM-NEGCLICK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-NEGCLICK

### IDEA-C-0041
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SAM-MULTIMASK.
- Problem: Papers about SAM-MULTIMASK rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Multi-mask ambiguity ranking is inverted on medical/amorphous images versus COCO. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SAM-MULTIMASK.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SAM-MULTIMASK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-MULTIMASK

### IDEA-C-0042
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SAM-MULTIMASK.
- Problem: Papers about SAM-MULTIMASK rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Multi-mask ambiguity ranking is inverted on medical/amorphous images versus COCO. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SAM-MULTIMASK.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SAM-MULTIMASK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-MULTIMASK

### IDEA-C-0043
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SAM-MULTIMASK.
- Problem: Papers about SAM-MULTIMASK rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Multi-mask ambiguity ranking is inverted on medical/amorphous images versus COCO. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SAM-MULTIMASK.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SAM-MULTIMASK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-MULTIMASK

### IDEA-C-0044
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SAM-MULTIMASK.
- Problem: Papers about SAM-MULTIMASK rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Multi-mask ambiguity ranking is inverted on medical/amorphous images versus COCO. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SAM-MULTIMASK.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SAM-MULTIMASK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-MULTIMASK

### IDEA-C-0045
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SAM-MULTIMASK.
- Problem: Papers about SAM-MULTIMASK rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Multi-mask ambiguity ranking is inverted on medical/amorphous images versus COCO. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SAM-MULTIMASK.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SAM-MULTIMASK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-MULTIMASK

### IDEA-C-0046
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SAM-MULTIMASK.
- Problem: Papers about SAM-MULTIMASK rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Multi-mask ambiguity ranking is inverted on medical/amorphous images versus COCO. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SAM-MULTIMASK.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SAM-MULTIMASK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-MULTIMASK

### IDEA-C-0047
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SAM-MULTIMASK.
- Problem: Papers about SAM-MULTIMASK rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Multi-mask ambiguity ranking is inverted on medical/amorphous images versus COCO. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SAM-MULTIMASK.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SAM-MULTIMASK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-MULTIMASK

### IDEA-C-0048
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SAM-MULTIMASK.
- Problem: Papers about SAM-MULTIMASK rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Multi-mask ambiguity ranking is inverted on medical/amorphous images versus COCO. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SAM-MULTIMASK.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SAM-MULTIMASK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM-MULTIMASK

### IDEA-C-0049
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SAM2-MEMORY.
- Problem: Papers about SAM2-MEMORY rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If SAM2 memory helps video objects but leaks identity across independently moving fire/smoke plumes. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SAM2-MEMORY.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SAM2-MEMORY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-MEMORY

### IDEA-C-0050
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SAM2-MEMORY.
- Problem: Papers about SAM2-MEMORY rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If SAM2 memory helps video objects but leaks identity across independently moving fire/smoke plumes. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SAM2-MEMORY.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SAM2-MEMORY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-MEMORY

### IDEA-C-0051
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SAM2-MEMORY.
- Problem: Papers about SAM2-MEMORY rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If SAM2 memory helps video objects but leaks identity across independently moving fire/smoke plumes. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SAM2-MEMORY.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SAM2-MEMORY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-MEMORY

### IDEA-C-0052
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SAM2-MEMORY.
- Problem: Papers about SAM2-MEMORY rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If SAM2 memory helps video objects but leaks identity across independently moving fire/smoke plumes. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SAM2-MEMORY.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SAM2-MEMORY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-MEMORY

### IDEA-C-0053
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SAM2-MEMORY.
- Problem: Papers about SAM2-MEMORY rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If SAM2 memory helps video objects but leaks identity across independently moving fire/smoke plumes. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SAM2-MEMORY.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SAM2-MEMORY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-MEMORY

### IDEA-C-0054
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SAM2-MEMORY.
- Problem: Papers about SAM2-MEMORY rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If SAM2 memory helps video objects but leaks identity across independently moving fire/smoke plumes. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SAM2-MEMORY.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SAM2-MEMORY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-MEMORY

### IDEA-C-0055
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SAM2-MEMORY.
- Problem: Papers about SAM2-MEMORY rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If SAM2 memory helps video objects but leaks identity across independently moving fire/smoke plumes. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SAM2-MEMORY.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SAM2-MEMORY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-MEMORY

### IDEA-C-0056
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SAM2-MEMORY.
- Problem: Papers about SAM2-MEMORY rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If SAM2 memory helps video objects but leaks identity across independently moving fire/smoke plumes. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SAM2-MEMORY.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SAM2-MEMORY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-MEMORY

### IDEA-C-0057
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SAM2-CD.
- Problem: Papers about SAM2-CD rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Context-dependent concepts fail because prompts cannot name relations; failure is linguistic not visual. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SAM2-CD.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SAM2-CD intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-CD

### IDEA-C-0058
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SAM2-CD.
- Problem: Papers about SAM2-CD rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Context-dependent concepts fail because prompts cannot name relations; failure is linguistic not visual. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SAM2-CD.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SAM2-CD intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-CD

### IDEA-C-0059
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SAM2-CD.
- Problem: Papers about SAM2-CD rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Context-dependent concepts fail because prompts cannot name relations; failure is linguistic not visual. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SAM2-CD.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SAM2-CD intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-CD

### IDEA-C-0060
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SAM2-CD.
- Problem: Papers about SAM2-CD rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Context-dependent concepts fail because prompts cannot name relations; failure is linguistic not visual. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SAM2-CD.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SAM2-CD intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-CD

### IDEA-C-0061
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SAM2-CD.
- Problem: Papers about SAM2-CD rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Context-dependent concepts fail because prompts cannot name relations; failure is linguistic not visual. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SAM2-CD.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SAM2-CD intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-CD

### IDEA-C-0062
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SAM2-CD.
- Problem: Papers about SAM2-CD rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Context-dependent concepts fail because prompts cannot name relations; failure is linguistic not visual. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SAM2-CD.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SAM2-CD intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-CD

### IDEA-C-0063
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SAM2-CD.
- Problem: Papers about SAM2-CD rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Context-dependent concepts fail because prompts cannot name relations; failure is linguistic not visual. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SAM2-CD.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SAM2-CD intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-CD

### IDEA-C-0064
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SAM2-CD.
- Problem: Papers about SAM2-CD rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Context-dependent concepts fail because prompts cannot name relations; failure is linguistic not visual. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SAM2-CD.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SAM2-CD intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SAM2-CD

### IDEA-C-0065
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind HQ-BOUNDARY.
- Problem: Papers about HQ-BOUNDARY rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If HQ-SAM high-quality token improves natural edges but not refractive/transparent boundaries. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for HQ-BOUNDARY.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard HQ-BOUNDARY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HQ-BOUNDARY

### IDEA-C-0066
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind HQ-BOUNDARY.
- Problem: Papers about HQ-BOUNDARY rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If HQ-SAM high-quality token improves natural edges but not refractive/transparent boundaries. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for HQ-BOUNDARY.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard HQ-BOUNDARY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HQ-BOUNDARY

### IDEA-C-0067
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind HQ-BOUNDARY.
- Problem: Papers about HQ-BOUNDARY rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If HQ-SAM high-quality token improves natural edges but not refractive/transparent boundaries. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for HQ-BOUNDARY.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard HQ-BOUNDARY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HQ-BOUNDARY

### IDEA-C-0068
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind HQ-BOUNDARY.
- Problem: Papers about HQ-BOUNDARY rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If HQ-SAM high-quality token improves natural edges but not refractive/transparent boundaries. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for HQ-BOUNDARY.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard HQ-BOUNDARY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HQ-BOUNDARY

### IDEA-C-0069
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind HQ-BOUNDARY.
- Problem: Papers about HQ-BOUNDARY rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If HQ-SAM high-quality token improves natural edges but not refractive/transparent boundaries. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for HQ-BOUNDARY.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard HQ-BOUNDARY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HQ-BOUNDARY

### IDEA-C-0070
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind HQ-BOUNDARY.
- Problem: Papers about HQ-BOUNDARY rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If HQ-SAM high-quality token improves natural edges but not refractive/transparent boundaries. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for HQ-BOUNDARY.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard HQ-BOUNDARY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HQ-BOUNDARY

### IDEA-C-0071
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind HQ-BOUNDARY.
- Problem: Papers about HQ-BOUNDARY rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If HQ-SAM high-quality token improves natural edges but not refractive/transparent boundaries. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for HQ-BOUNDARY.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard HQ-BOUNDARY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HQ-BOUNDARY

### IDEA-C-0072
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind HQ-BOUNDARY.
- Problem: Papers about HQ-BOUNDARY rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If HQ-SAM high-quality token improves natural edges but not refractive/transparent boundaries. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for HQ-BOUNDARY.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard HQ-BOUNDARY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HQ-BOUNDARY

### IDEA-C-0073
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind FT-FORGET.
- Problem: Papers about FT-FORGET rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Full fine-tuning MedSAM-style destroys promptable zero-shot more than PEFT, but PEFT still destroys it on other modalities. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for FT-FORGET.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard FT-FORGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FT-FORGET

### IDEA-C-0074
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind FT-FORGET.
- Problem: Papers about FT-FORGET rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Full fine-tuning MedSAM-style destroys promptable zero-shot more than PEFT, but PEFT still destroys it on other modalities. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for FT-FORGET.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard FT-FORGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FT-FORGET

### IDEA-C-0075
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind FT-FORGET.
- Problem: Papers about FT-FORGET rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Full fine-tuning MedSAM-style destroys promptable zero-shot more than PEFT, but PEFT still destroys it on other modalities. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for FT-FORGET.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard FT-FORGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FT-FORGET

### IDEA-C-0076
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind FT-FORGET.
- Problem: Papers about FT-FORGET rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Full fine-tuning MedSAM-style destroys promptable zero-shot more than PEFT, but PEFT still destroys it on other modalities. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for FT-FORGET.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard FT-FORGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FT-FORGET

### IDEA-C-0077
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind FT-FORGET.
- Problem: Papers about FT-FORGET rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Full fine-tuning MedSAM-style destroys promptable zero-shot more than PEFT, but PEFT still destroys it on other modalities. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for FT-FORGET.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard FT-FORGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FT-FORGET

### IDEA-C-0078
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind FT-FORGET.
- Problem: Papers about FT-FORGET rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Full fine-tuning MedSAM-style destroys promptable zero-shot more than PEFT, but PEFT still destroys it on other modalities. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for FT-FORGET.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard FT-FORGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FT-FORGET

### IDEA-C-0079
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind FT-FORGET.
- Problem: Papers about FT-FORGET rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Full fine-tuning MedSAM-style destroys promptable zero-shot more than PEFT, but PEFT still destroys it on other modalities. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for FT-FORGET.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard FT-FORGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FT-FORGET

### IDEA-C-0080
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind FT-FORGET.
- Problem: Papers about FT-FORGET rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Full fine-tuning MedSAM-style destroys promptable zero-shot more than PEFT, but PEFT still destroys it on other modalities. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for FT-FORGET.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard FT-FORGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FT-FORGET

### IDEA-C-0081
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind PEFT-SPECTRAL.
- Problem: Papers about PEFT-SPECTRAL rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If LoRA updates for dense tasks are spectrally low-pass; extra rank does not buy boundary frequencies. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for PEFT-SPECTRAL.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard PEFT-SPECTRAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SPECTRAL

### IDEA-C-0082
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind PEFT-SPECTRAL.
- Problem: Papers about PEFT-SPECTRAL rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If LoRA updates for dense tasks are spectrally low-pass; extra rank does not buy boundary frequencies. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for PEFT-SPECTRAL.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard PEFT-SPECTRAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SPECTRAL

### IDEA-C-0083
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind PEFT-SPECTRAL.
- Problem: Papers about PEFT-SPECTRAL rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If LoRA updates for dense tasks are spectrally low-pass; extra rank does not buy boundary frequencies. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for PEFT-SPECTRAL.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard PEFT-SPECTRAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SPECTRAL

### IDEA-C-0084
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind PEFT-SPECTRAL.
- Problem: Papers about PEFT-SPECTRAL rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If LoRA updates for dense tasks are spectrally low-pass; extra rank does not buy boundary frequencies. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for PEFT-SPECTRAL.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard PEFT-SPECTRAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SPECTRAL

### IDEA-C-0085
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind PEFT-SPECTRAL.
- Problem: Papers about PEFT-SPECTRAL rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If LoRA updates for dense tasks are spectrally low-pass; extra rank does not buy boundary frequencies. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for PEFT-SPECTRAL.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard PEFT-SPECTRAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SPECTRAL

### IDEA-C-0086
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind PEFT-SPECTRAL.
- Problem: Papers about PEFT-SPECTRAL rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If LoRA updates for dense tasks are spectrally low-pass; extra rank does not buy boundary frequencies. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for PEFT-SPECTRAL.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard PEFT-SPECTRAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SPECTRAL

### IDEA-C-0087
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind PEFT-SPECTRAL.
- Problem: Papers about PEFT-SPECTRAL rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If LoRA updates for dense tasks are spectrally low-pass; extra rank does not buy boundary frequencies. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for PEFT-SPECTRAL.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard PEFT-SPECTRAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SPECTRAL

### IDEA-C-0088
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind PEFT-SPECTRAL.
- Problem: Papers about PEFT-SPECTRAL rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If LoRA updates for dense tasks are spectrally low-pass; extra rank does not buy boundary frequencies. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for PEFT-SPECTRAL.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard PEFT-SPECTRAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SPECTRAL

### IDEA-C-0089
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind PEFT-SITE.
- Problem: Papers about PEFT-SITE rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If LoRA placement on Q vs V vs MLP has different effects on localization vs recognition. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for PEFT-SITE.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard PEFT-SITE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SITE

### IDEA-C-0090
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind PEFT-SITE.
- Problem: Papers about PEFT-SITE rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If LoRA placement on Q vs V vs MLP has different effects on localization vs recognition. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for PEFT-SITE.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard PEFT-SITE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SITE

### IDEA-C-0091
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind PEFT-SITE.
- Problem: Papers about PEFT-SITE rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If LoRA placement on Q vs V vs MLP has different effects on localization vs recognition. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for PEFT-SITE.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard PEFT-SITE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SITE

### IDEA-C-0092
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind PEFT-SITE.
- Problem: Papers about PEFT-SITE rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If LoRA placement on Q vs V vs MLP has different effects on localization vs recognition. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for PEFT-SITE.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard PEFT-SITE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SITE

### IDEA-C-0093
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind PEFT-SITE.
- Problem: Papers about PEFT-SITE rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If LoRA placement on Q vs V vs MLP has different effects on localization vs recognition. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for PEFT-SITE.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard PEFT-SITE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SITE

### IDEA-C-0094
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind PEFT-SITE.
- Problem: Papers about PEFT-SITE rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If LoRA placement on Q vs V vs MLP has different effects on localization vs recognition. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for PEFT-SITE.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard PEFT-SITE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SITE

### IDEA-C-0095
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind PEFT-SITE.
- Problem: Papers about PEFT-SITE rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If LoRA placement on Q vs V vs MLP has different effects on localization vs recognition. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for PEFT-SITE.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard PEFT-SITE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SITE

### IDEA-C-0096
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind PEFT-SITE.
- Problem: Papers about PEFT-SITE rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If LoRA placement on Q vs V vs MLP has different effects on localization vs recognition. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for PEFT-SITE.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard PEFT-SITE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-SITE

### IDEA-C-0097
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind PEFT-DECODER.
- Problem: Papers about PEFT-DECODER rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Decoder-only FT matches full FT on large organs and fails on small lesions, revealing where the encoder was actually needed. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for PEFT-DECODER.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard PEFT-DECODER intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-DECODER

### IDEA-C-0098
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind PEFT-DECODER.
- Problem: Papers about PEFT-DECODER rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Decoder-only FT matches full FT on large organs and fails on small lesions, revealing where the encoder was actually needed. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for PEFT-DECODER.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard PEFT-DECODER intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-DECODER

### IDEA-C-0099
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind PEFT-DECODER.
- Problem: Papers about PEFT-DECODER rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Decoder-only FT matches full FT on large organs and fails on small lesions, revealing where the encoder was actually needed. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for PEFT-DECODER.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard PEFT-DECODER intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-DECODER

### IDEA-C-0100
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind PEFT-DECODER.
- Problem: Papers about PEFT-DECODER rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Decoder-only FT matches full FT on large organs and fails on small lesions, revealing where the encoder was actually needed. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for PEFT-DECODER.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard PEFT-DECODER intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-DECODER

### IDEA-C-0101
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind PEFT-DECODER.
- Problem: Papers about PEFT-DECODER rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Decoder-only FT matches full FT on large organs and fails on small lesions, revealing where the encoder was actually needed. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for PEFT-DECODER.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard PEFT-DECODER intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-DECODER

### IDEA-C-0102
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind PEFT-DECODER.
- Problem: Papers about PEFT-DECODER rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Decoder-only FT matches full FT on large organs and fails on small lesions, revealing where the encoder was actually needed. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for PEFT-DECODER.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard PEFT-DECODER intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-DECODER

### IDEA-C-0103
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind PEFT-DECODER.
- Problem: Papers about PEFT-DECODER rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Decoder-only FT matches full FT on large organs and fails on small lesions, revealing where the encoder was actually needed. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for PEFT-DECODER.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard PEFT-DECODER intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-DECODER

### IDEA-C-0104
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind PEFT-DECODER.
- Problem: Papers about PEFT-DECODER rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Decoder-only FT matches full FT on large organs and fails on small lesions, revealing where the encoder was actually needed. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for PEFT-DECODER.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard PEFT-DECODER intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-DECODER

### IDEA-C-0105
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind PEFT-RANK-COLLAPSE.
- Problem: Papers about PEFT-RANK-COLLAPSE rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If PEFT adapters collapse to rank-1 spatial maps that ignore instance count. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for PEFT-RANK-COLLAPSE.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard PEFT-RANK-COLLAPSE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-RANK-COLLAPSE

### IDEA-C-0106
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind PEFT-RANK-COLLAPSE.
- Problem: Papers about PEFT-RANK-COLLAPSE rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If PEFT adapters collapse to rank-1 spatial maps that ignore instance count. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for PEFT-RANK-COLLAPSE.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard PEFT-RANK-COLLAPSE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-RANK-COLLAPSE

### IDEA-C-0107
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind PEFT-RANK-COLLAPSE.
- Problem: Papers about PEFT-RANK-COLLAPSE rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If PEFT adapters collapse to rank-1 spatial maps that ignore instance count. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for PEFT-RANK-COLLAPSE.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard PEFT-RANK-COLLAPSE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-RANK-COLLAPSE

### IDEA-C-0108
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind PEFT-RANK-COLLAPSE.
- Problem: Papers about PEFT-RANK-COLLAPSE rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If PEFT adapters collapse to rank-1 spatial maps that ignore instance count. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for PEFT-RANK-COLLAPSE.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard PEFT-RANK-COLLAPSE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-RANK-COLLAPSE

### IDEA-C-0109
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind PEFT-RANK-COLLAPSE.
- Problem: Papers about PEFT-RANK-COLLAPSE rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If PEFT adapters collapse to rank-1 spatial maps that ignore instance count. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for PEFT-RANK-COLLAPSE.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard PEFT-RANK-COLLAPSE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-RANK-COLLAPSE

### IDEA-C-0110
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind PEFT-RANK-COLLAPSE.
- Problem: Papers about PEFT-RANK-COLLAPSE rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If PEFT adapters collapse to rank-1 spatial maps that ignore instance count. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for PEFT-RANK-COLLAPSE.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard PEFT-RANK-COLLAPSE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-RANK-COLLAPSE

### IDEA-C-0111
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind PEFT-RANK-COLLAPSE.
- Problem: Papers about PEFT-RANK-COLLAPSE rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If PEFT adapters collapse to rank-1 spatial maps that ignore instance count. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for PEFT-RANK-COLLAPSE.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard PEFT-RANK-COLLAPSE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-RANK-COLLAPSE

### IDEA-C-0112
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind PEFT-RANK-COLLAPSE.
- Problem: Papers about PEFT-RANK-COLLAPSE rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If PEFT adapters collapse to rank-1 spatial maps that ignore instance count. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for PEFT-RANK-COLLAPSE.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard PEFT-RANK-COLLAPSE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PEFT-RANK-COLLAPSE

### IDEA-C-0113
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind BN-VS-LORA.
- Problem: Papers about BN-VS-LORA rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If On tiny medical sets, unfreezing BN/LN dominates LoRA; reported LoRA gains are actually norm adaptation. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for BN-VS-LORA.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard BN-VS-LORA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BN-VS-LORA

### IDEA-C-0114
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind BN-VS-LORA.
- Problem: Papers about BN-VS-LORA rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If On tiny medical sets, unfreezing BN/LN dominates LoRA; reported LoRA gains are actually norm adaptation. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for BN-VS-LORA.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard BN-VS-LORA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BN-VS-LORA

### IDEA-C-0115
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind BN-VS-LORA.
- Problem: Papers about BN-VS-LORA rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If On tiny medical sets, unfreezing BN/LN dominates LoRA; reported LoRA gains are actually norm adaptation. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for BN-VS-LORA.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard BN-VS-LORA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BN-VS-LORA

### IDEA-C-0116
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind BN-VS-LORA.
- Problem: Papers about BN-VS-LORA rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If On tiny medical sets, unfreezing BN/LN dominates LoRA; reported LoRA gains are actually norm adaptation. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for BN-VS-LORA.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard BN-VS-LORA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BN-VS-LORA

### IDEA-C-0117
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind BN-VS-LORA.
- Problem: Papers about BN-VS-LORA rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If On tiny medical sets, unfreezing BN/LN dominates LoRA; reported LoRA gains are actually norm adaptation. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for BN-VS-LORA.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard BN-VS-LORA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BN-VS-LORA

### IDEA-C-0118
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind BN-VS-LORA.
- Problem: Papers about BN-VS-LORA rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If On tiny medical sets, unfreezing BN/LN dominates LoRA; reported LoRA gains are actually norm adaptation. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for BN-VS-LORA.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard BN-VS-LORA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BN-VS-LORA

### IDEA-C-0119
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind BN-VS-LORA.
- Problem: Papers about BN-VS-LORA rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If On tiny medical sets, unfreezing BN/LN dominates LoRA; reported LoRA gains are actually norm adaptation. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for BN-VS-LORA.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard BN-VS-LORA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BN-VS-LORA

### IDEA-C-0120
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind BN-VS-LORA.
- Problem: Papers about BN-VS-LORA rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If On tiny medical sets, unfreezing BN/LN dominates LoRA; reported LoRA gains are actually norm adaptation. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for BN-VS-LORA.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard BN-VS-LORA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BN-VS-LORA

### IDEA-C-0121
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind LINEAR-PROBE.
- Problem: Papers about LINEAR-PROBE rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If A linear head on frozen SAM embeddings beats prompted SAM on amorphous targets if objectness is the bottleneck. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for LINEAR-PROBE.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard LINEAR-PROBE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LINEAR-PROBE

### IDEA-C-0122
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind LINEAR-PROBE.
- Problem: Papers about LINEAR-PROBE rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If A linear head on frozen SAM embeddings beats prompted SAM on amorphous targets if objectness is the bottleneck. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for LINEAR-PROBE.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard LINEAR-PROBE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LINEAR-PROBE

### IDEA-C-0123
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind LINEAR-PROBE.
- Problem: Papers about LINEAR-PROBE rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If A linear head on frozen SAM embeddings beats prompted SAM on amorphous targets if objectness is the bottleneck. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for LINEAR-PROBE.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard LINEAR-PROBE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LINEAR-PROBE

### IDEA-C-0124
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind LINEAR-PROBE.
- Problem: Papers about LINEAR-PROBE rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If A linear head on frozen SAM embeddings beats prompted SAM on amorphous targets if objectness is the bottleneck. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for LINEAR-PROBE.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard LINEAR-PROBE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LINEAR-PROBE

### IDEA-C-0125
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind LINEAR-PROBE.
- Problem: Papers about LINEAR-PROBE rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If A linear head on frozen SAM embeddings beats prompted SAM on amorphous targets if objectness is the bottleneck. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for LINEAR-PROBE.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard LINEAR-PROBE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LINEAR-PROBE

### IDEA-C-0126
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind LINEAR-PROBE.
- Problem: Papers about LINEAR-PROBE rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If A linear head on frozen SAM embeddings beats prompted SAM on amorphous targets if objectness is the bottleneck. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for LINEAR-PROBE.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard LINEAR-PROBE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LINEAR-PROBE

### IDEA-C-0127
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind LINEAR-PROBE.
- Problem: Papers about LINEAR-PROBE rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If A linear head on frozen SAM embeddings beats prompted SAM on amorphous targets if objectness is the bottleneck. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for LINEAR-PROBE.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard LINEAR-PROBE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LINEAR-PROBE

### IDEA-C-0128
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind LINEAR-PROBE.
- Problem: Papers about LINEAR-PROBE rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If A linear head on frozen SAM embeddings beats prompted SAM on amorphous targets if objectness is the bottleneck. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for LINEAR-PROBE.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard LINEAR-PROBE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LINEAR-PROBE

### IDEA-C-0129
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind DICE-RANK.
- Problem: Papers about DICE-RANK rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Method ranking on medical VFMs reverses under size-stratified Dice / NSD / CC-Dice vs mean Dice. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for DICE-RANK.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard DICE-RANK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DICE-RANK

### IDEA-C-0130
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind DICE-RANK.
- Problem: Papers about DICE-RANK rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Method ranking on medical VFMs reverses under size-stratified Dice / NSD / CC-Dice vs mean Dice. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for DICE-RANK.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard DICE-RANK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DICE-RANK

### IDEA-C-0131
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind DICE-RANK.
- Problem: Papers about DICE-RANK rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Method ranking on medical VFMs reverses under size-stratified Dice / NSD / CC-Dice vs mean Dice. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for DICE-RANK.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard DICE-RANK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DICE-RANK

### IDEA-C-0132
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind DICE-RANK.
- Problem: Papers about DICE-RANK rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Method ranking on medical VFMs reverses under size-stratified Dice / NSD / CC-Dice vs mean Dice. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for DICE-RANK.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard DICE-RANK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DICE-RANK

### IDEA-C-0133
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind DICE-RANK.
- Problem: Papers about DICE-RANK rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Method ranking on medical VFMs reverses under size-stratified Dice / NSD / CC-Dice vs mean Dice. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for DICE-RANK.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard DICE-RANK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DICE-RANK

### IDEA-C-0134
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind DICE-RANK.
- Problem: Papers about DICE-RANK rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Method ranking on medical VFMs reverses under size-stratified Dice / NSD / CC-Dice vs mean Dice. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for DICE-RANK.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard DICE-RANK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DICE-RANK

### IDEA-C-0135
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind DICE-RANK.
- Problem: Papers about DICE-RANK rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Method ranking on medical VFMs reverses under size-stratified Dice / NSD / CC-Dice vs mean Dice. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for DICE-RANK.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard DICE-RANK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DICE-RANK

### IDEA-C-0136
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind DICE-RANK.
- Problem: Papers about DICE-RANK rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Method ranking on medical VFMs reverses under size-stratified Dice / NSD / CC-Dice vs mean Dice. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for DICE-RANK.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard DICE-RANK intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DICE-RANK

### IDEA-C-0137
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind LEAKAGE.
- Problem: Papers about LEAKAGE rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Apparent MedSAM generalization is partly patient/scanner/hospital leakage in official splits. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for LEAKAGE.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard LEAKAGE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LEAKAGE

### IDEA-C-0138
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind LEAKAGE.
- Problem: Papers about LEAKAGE rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Apparent MedSAM generalization is partly patient/scanner/hospital leakage in official splits. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for LEAKAGE.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard LEAKAGE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LEAKAGE

### IDEA-C-0139
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind LEAKAGE.
- Problem: Papers about LEAKAGE rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Apparent MedSAM generalization is partly patient/scanner/hospital leakage in official splits. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for LEAKAGE.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard LEAKAGE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LEAKAGE

### IDEA-C-0140
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind LEAKAGE.
- Problem: Papers about LEAKAGE rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Apparent MedSAM generalization is partly patient/scanner/hospital leakage in official splits. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for LEAKAGE.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard LEAKAGE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LEAKAGE

### IDEA-C-0141
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind LEAKAGE.
- Problem: Papers about LEAKAGE rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Apparent MedSAM generalization is partly patient/scanner/hospital leakage in official splits. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for LEAKAGE.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard LEAKAGE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LEAKAGE

### IDEA-C-0142
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind LEAKAGE.
- Problem: Papers about LEAKAGE rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Apparent MedSAM generalization is partly patient/scanner/hospital leakage in official splits. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for LEAKAGE.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard LEAKAGE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LEAKAGE

### IDEA-C-0143
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind LEAKAGE.
- Problem: Papers about LEAKAGE rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Apparent MedSAM generalization is partly patient/scanner/hospital leakage in official splits. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for LEAKAGE.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard LEAKAGE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LEAKAGE

### IDEA-C-0144
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind LEAKAGE.
- Problem: Papers about LEAKAGE rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Apparent MedSAM generalization is partly patient/scanner/hospital leakage in official splits. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for LEAKAGE.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard LEAKAGE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LEAKAGE

### IDEA-C-0145
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind PRETRAIN-OVERLAP.
- Problem: Papers about PRETRAIN-OVERLAP rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Zero-shot SAM 'wins' on some medical tests because of SA-1B / web-image overlap with textbook anatomies. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for PRETRAIN-OVERLAP.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard PRETRAIN-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PRETRAIN-OVERLAP

### IDEA-C-0146
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind PRETRAIN-OVERLAP.
- Problem: Papers about PRETRAIN-OVERLAP rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Zero-shot SAM 'wins' on some medical tests because of SA-1B / web-image overlap with textbook anatomies. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for PRETRAIN-OVERLAP.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard PRETRAIN-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PRETRAIN-OVERLAP

### IDEA-C-0147
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind PRETRAIN-OVERLAP.
- Problem: Papers about PRETRAIN-OVERLAP rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Zero-shot SAM 'wins' on some medical tests because of SA-1B / web-image overlap with textbook anatomies. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for PRETRAIN-OVERLAP.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard PRETRAIN-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PRETRAIN-OVERLAP

### IDEA-C-0148
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind PRETRAIN-OVERLAP.
- Problem: Papers about PRETRAIN-OVERLAP rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Zero-shot SAM 'wins' on some medical tests because of SA-1B / web-image overlap with textbook anatomies. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for PRETRAIN-OVERLAP.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard PRETRAIN-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PRETRAIN-OVERLAP

### IDEA-C-0149
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind PRETRAIN-OVERLAP.
- Problem: Papers about PRETRAIN-OVERLAP rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Zero-shot SAM 'wins' on some medical tests because of SA-1B / web-image overlap with textbook anatomies. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for PRETRAIN-OVERLAP.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard PRETRAIN-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PRETRAIN-OVERLAP

### IDEA-C-0150
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind PRETRAIN-OVERLAP.
- Problem: Papers about PRETRAIN-OVERLAP rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Zero-shot SAM 'wins' on some medical tests because of SA-1B / web-image overlap with textbook anatomies. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for PRETRAIN-OVERLAP.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard PRETRAIN-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PRETRAIN-OVERLAP

### IDEA-C-0151
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind PRETRAIN-OVERLAP.
- Problem: Papers about PRETRAIN-OVERLAP rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Zero-shot SAM 'wins' on some medical tests because of SA-1B / web-image overlap with textbook anatomies. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for PRETRAIN-OVERLAP.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard PRETRAIN-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PRETRAIN-OVERLAP

### IDEA-C-0152
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind PRETRAIN-OVERLAP.
- Problem: Papers about PRETRAIN-OVERLAP rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Zero-shot SAM 'wins' on some medical tests because of SA-1B / web-image overlap with textbook anatomies. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for PRETRAIN-OVERLAP.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard PRETRAIN-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PRETRAIN-OVERLAP

### IDEA-C-0153
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind LABEL-NOISE.
- Problem: Papers about LABEL-NOISE rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Inter-rater disagreement geometry, not model capacity, caps Dice on ambiguous lesions; methods overfit rater A. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for LABEL-NOISE.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard LABEL-NOISE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LABEL-NOISE

### IDEA-C-0154
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind LABEL-NOISE.
- Problem: Papers about LABEL-NOISE rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Inter-rater disagreement geometry, not model capacity, caps Dice on ambiguous lesions; methods overfit rater A. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for LABEL-NOISE.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard LABEL-NOISE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LABEL-NOISE

### IDEA-C-0155
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind LABEL-NOISE.
- Problem: Papers about LABEL-NOISE rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Inter-rater disagreement geometry, not model capacity, caps Dice on ambiguous lesions; methods overfit rater A. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for LABEL-NOISE.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard LABEL-NOISE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LABEL-NOISE

### IDEA-C-0156
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind LABEL-NOISE.
- Problem: Papers about LABEL-NOISE rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Inter-rater disagreement geometry, not model capacity, caps Dice on ambiguous lesions; methods overfit rater A. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for LABEL-NOISE.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard LABEL-NOISE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LABEL-NOISE

### IDEA-C-0157
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind LABEL-NOISE.
- Problem: Papers about LABEL-NOISE rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Inter-rater disagreement geometry, not model capacity, caps Dice on ambiguous lesions; methods overfit rater A. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for LABEL-NOISE.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard LABEL-NOISE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LABEL-NOISE

### IDEA-C-0158
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind LABEL-NOISE.
- Problem: Papers about LABEL-NOISE rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Inter-rater disagreement geometry, not model capacity, caps Dice on ambiguous lesions; methods overfit rater A. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for LABEL-NOISE.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard LABEL-NOISE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LABEL-NOISE

### IDEA-C-0159
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind LABEL-NOISE.
- Problem: Papers about LABEL-NOISE rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Inter-rater disagreement geometry, not model capacity, caps Dice on ambiguous lesions; methods overfit rater A. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for LABEL-NOISE.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard LABEL-NOISE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LABEL-NOISE

### IDEA-C-0160
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind LABEL-NOISE.
- Problem: Papers about LABEL-NOISE rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Inter-rater disagreement geometry, not model capacity, caps Dice on ambiguous lesions; methods overfit rater A. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for LABEL-NOISE.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard LABEL-NOISE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LABEL-NOISE

### IDEA-C-0161
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SLICE-INCONSIST.
- Problem: Papers about SLICE-INCONSIST rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If 2D SAM-per-slice is inconsistent in 3D because prompts are i.i.d.; the bug is prompt independence not 2D kernels. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SLICE-INCONSIST.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SLICE-INCONSIST intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SLICE-INCONSIST

### IDEA-C-0162
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SLICE-INCONSIST.
- Problem: Papers about SLICE-INCONSIST rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If 2D SAM-per-slice is inconsistent in 3D because prompts are i.i.d.; the bug is prompt independence not 2D kernels. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SLICE-INCONSIST.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SLICE-INCONSIST intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SLICE-INCONSIST

### IDEA-C-0163
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SLICE-INCONSIST.
- Problem: Papers about SLICE-INCONSIST rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If 2D SAM-per-slice is inconsistent in 3D because prompts are i.i.d.; the bug is prompt independence not 2D kernels. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SLICE-INCONSIST.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SLICE-INCONSIST intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SLICE-INCONSIST

### IDEA-C-0164
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SLICE-INCONSIST.
- Problem: Papers about SLICE-INCONSIST rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If 2D SAM-per-slice is inconsistent in 3D because prompts are i.i.d.; the bug is prompt independence not 2D kernels. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SLICE-INCONSIST.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SLICE-INCONSIST intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SLICE-INCONSIST

### IDEA-C-0165
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SLICE-INCONSIST.
- Problem: Papers about SLICE-INCONSIST rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If 2D SAM-per-slice is inconsistent in 3D because prompts are i.i.d.; the bug is prompt independence not 2D kernels. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SLICE-INCONSIST.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SLICE-INCONSIST intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SLICE-INCONSIST

### IDEA-C-0166
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SLICE-INCONSIST.
- Problem: Papers about SLICE-INCONSIST rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If 2D SAM-per-slice is inconsistent in 3D because prompts are i.i.d.; the bug is prompt independence not 2D kernels. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SLICE-INCONSIST.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SLICE-INCONSIST intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SLICE-INCONSIST

### IDEA-C-0167
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SLICE-INCONSIST.
- Problem: Papers about SLICE-INCONSIST rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If 2D SAM-per-slice is inconsistent in 3D because prompts are i.i.d.; the bug is prompt independence not 2D kernels. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SLICE-INCONSIST.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SLICE-INCONSIST intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SLICE-INCONSIST

### IDEA-C-0168
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SLICE-INCONSIST.
- Problem: Papers about SLICE-INCONSIST rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If 2D SAM-per-slice is inconsistent in 3D because prompts are i.i.d.; the bug is prompt independence not 2D kernels. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SLICE-INCONSIST.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SLICE-INCONSIST intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SLICE-INCONSIST

### IDEA-C-0169
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind ANISO.
- Problem: Papers about ANISO rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Anisotropic CT spacing fools ViT patch geometry; failures attributed to 'domain' are resampling artifacts. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for ANISO.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard ANISO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: ANISO

### IDEA-C-0170
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind ANISO.
- Problem: Papers about ANISO rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Anisotropic CT spacing fools ViT patch geometry; failures attributed to 'domain' are resampling artifacts. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for ANISO.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard ANISO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: ANISO

### IDEA-C-0171
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind ANISO.
- Problem: Papers about ANISO rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Anisotropic CT spacing fools ViT patch geometry; failures attributed to 'domain' are resampling artifacts. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for ANISO.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard ANISO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: ANISO

### IDEA-C-0172
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind ANISO.
- Problem: Papers about ANISO rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Anisotropic CT spacing fools ViT patch geometry; failures attributed to 'domain' are resampling artifacts. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for ANISO.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard ANISO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: ANISO

### IDEA-C-0173
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind ANISO.
- Problem: Papers about ANISO rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Anisotropic CT spacing fools ViT patch geometry; failures attributed to 'domain' are resampling artifacts. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for ANISO.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard ANISO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: ANISO

### IDEA-C-0174
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind ANISO.
- Problem: Papers about ANISO rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Anisotropic CT spacing fools ViT patch geometry; failures attributed to 'domain' are resampling artifacts. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for ANISO.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard ANISO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: ANISO

### IDEA-C-0175
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind ANISO.
- Problem: Papers about ANISO rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Anisotropic CT spacing fools ViT patch geometry; failures attributed to 'domain' are resampling artifacts. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for ANISO.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard ANISO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: ANISO

### IDEA-C-0176
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind ANISO.
- Problem: Papers about ANISO rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Anisotropic CT spacing fools ViT patch geometry; failures attributed to 'domain' are resampling artifacts. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for ANISO.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard ANISO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: ANISO

### IDEA-C-0177
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SMALL-OBJ-INTERP.
- Problem: Papers about SMALL-OBJ-INTERP rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Small-object error is dominated by input resampling, not architecture; same model at native resolution closes the gap. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SMALL-OBJ-INTERP.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SMALL-OBJ-INTERP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMALL-OBJ-INTERP

### IDEA-C-0178
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SMALL-OBJ-INTERP.
- Problem: Papers about SMALL-OBJ-INTERP rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Small-object error is dominated by input resampling, not architecture; same model at native resolution closes the gap. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SMALL-OBJ-INTERP.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SMALL-OBJ-INTERP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMALL-OBJ-INTERP

### IDEA-C-0179
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SMALL-OBJ-INTERP.
- Problem: Papers about SMALL-OBJ-INTERP rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Small-object error is dominated by input resampling, not architecture; same model at native resolution closes the gap. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SMALL-OBJ-INTERP.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SMALL-OBJ-INTERP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMALL-OBJ-INTERP

### IDEA-C-0180
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SMALL-OBJ-INTERP.
- Problem: Papers about SMALL-OBJ-INTERP rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Small-object error is dominated by input resampling, not architecture; same model at native resolution closes the gap. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SMALL-OBJ-INTERP.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SMALL-OBJ-INTERP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMALL-OBJ-INTERP

### IDEA-C-0181
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SMALL-OBJ-INTERP.
- Problem: Papers about SMALL-OBJ-INTERP rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Small-object error is dominated by input resampling, not architecture; same model at native resolution closes the gap. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SMALL-OBJ-INTERP.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SMALL-OBJ-INTERP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMALL-OBJ-INTERP

### IDEA-C-0182
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SMALL-OBJ-INTERP.
- Problem: Papers about SMALL-OBJ-INTERP rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Small-object error is dominated by input resampling, not architecture; same model at native resolution closes the gap. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SMALL-OBJ-INTERP.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SMALL-OBJ-INTERP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMALL-OBJ-INTERP

### IDEA-C-0183
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SMALL-OBJ-INTERP.
- Problem: Papers about SMALL-OBJ-INTERP rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Small-object error is dominated by input resampling, not architecture; same model at native resolution closes the gap. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SMALL-OBJ-INTERP.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SMALL-OBJ-INTERP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMALL-OBJ-INTERP

### IDEA-C-0184
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SMALL-OBJ-INTERP.
- Problem: Papers about SMALL-OBJ-INTERP rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Small-object error is dominated by input resampling, not architecture; same model at native resolution closes the gap. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SMALL-OBJ-INTERP.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SMALL-OBJ-INTERP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMALL-OBJ-INTERP

### IDEA-C-0185
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind CALIB-SEG.
- Problem: Papers about CALIB-SEG rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Pixel confidence of VFMs is anti-correlated with error on boundaries; temperature scaling on pixels fails. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for CALIB-SEG.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard CALIB-SEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CALIB-SEG

### IDEA-C-0186
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind CALIB-SEG.
- Problem: Papers about CALIB-SEG rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Pixel confidence of VFMs is anti-correlated with error on boundaries; temperature scaling on pixels fails. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for CALIB-SEG.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard CALIB-SEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CALIB-SEG

### IDEA-C-0187
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind CALIB-SEG.
- Problem: Papers about CALIB-SEG rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Pixel confidence of VFMs is anti-correlated with error on boundaries; temperature scaling on pixels fails. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for CALIB-SEG.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard CALIB-SEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CALIB-SEG

### IDEA-C-0188
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind CALIB-SEG.
- Problem: Papers about CALIB-SEG rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Pixel confidence of VFMs is anti-correlated with error on boundaries; temperature scaling on pixels fails. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for CALIB-SEG.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard CALIB-SEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CALIB-SEG

### IDEA-C-0189
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind CALIB-SEG.
- Problem: Papers about CALIB-SEG rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Pixel confidence of VFMs is anti-correlated with error on boundaries; temperature scaling on pixels fails. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for CALIB-SEG.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard CALIB-SEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CALIB-SEG

### IDEA-C-0190
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind CALIB-SEG.
- Problem: Papers about CALIB-SEG rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Pixel confidence of VFMs is anti-correlated with error on boundaries; temperature scaling on pixels fails. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for CALIB-SEG.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard CALIB-SEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CALIB-SEG

### IDEA-C-0191
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind CALIB-SEG.
- Problem: Papers about CALIB-SEG rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Pixel confidence of VFMs is anti-correlated with error on boundaries; temperature scaling on pixels fails. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for CALIB-SEG.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard CALIB-SEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CALIB-SEG

### IDEA-C-0192
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind CALIB-SEG.
- Problem: Papers about CALIB-SEG rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Pixel confidence of VFMs is anti-correlated with error on boundaries; temperature scaling on pixels fails. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for CALIB-SEG.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard CALIB-SEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CALIB-SEG

### IDEA-C-0193
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SYN-PHOTO.
- Problem: Papers about SYN-PHOTO rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Photorealistic synthetic data helps classification probes but not boundaries; geometric label-perfect renders transfer more. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SYN-PHOTO.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SYN-PHOTO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-PHOTO

### IDEA-C-0194
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SYN-PHOTO.
- Problem: Papers about SYN-PHOTO rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Photorealistic synthetic data helps classification probes but not boundaries; geometric label-perfect renders transfer more. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SYN-PHOTO.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SYN-PHOTO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-PHOTO

### IDEA-C-0195
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SYN-PHOTO.
- Problem: Papers about SYN-PHOTO rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Photorealistic synthetic data helps classification probes but not boundaries; geometric label-perfect renders transfer more. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SYN-PHOTO.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SYN-PHOTO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-PHOTO

### IDEA-C-0196
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SYN-PHOTO.
- Problem: Papers about SYN-PHOTO rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Photorealistic synthetic data helps classification probes but not boundaries; geometric label-perfect renders transfer more. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SYN-PHOTO.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SYN-PHOTO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-PHOTO

### IDEA-C-0197
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SYN-PHOTO.
- Problem: Papers about SYN-PHOTO rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Photorealistic synthetic data helps classification probes but not boundaries; geometric label-perfect renders transfer more. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SYN-PHOTO.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SYN-PHOTO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-PHOTO

### IDEA-C-0198
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SYN-PHOTO.
- Problem: Papers about SYN-PHOTO rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Photorealistic synthetic data helps classification probes but not boundaries; geometric label-perfect renders transfer more. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SYN-PHOTO.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SYN-PHOTO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-PHOTO

### IDEA-C-0199
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SYN-PHOTO.
- Problem: Papers about SYN-PHOTO rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Photorealistic synthetic data helps classification probes but not boundaries; geometric label-perfect renders transfer more. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SYN-PHOTO.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SYN-PHOTO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-PHOTO

### IDEA-C-0200
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SYN-PHOTO.
- Problem: Papers about SYN-PHOTO rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Photorealistic synthetic data helps classification probes but not boundaries; geometric label-perfect renders transfer more. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SYN-PHOTO.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SYN-PHOTO intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-PHOTO

### IDEA-C-0201
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SYN-DOMAIN.
- Problem: Papers about SYN-DOMAIN rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Synthetic-to-real gap for smoke is lighting/scattering, not texture GAN fidelity. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SYN-DOMAIN.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SYN-DOMAIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-DOMAIN

### IDEA-C-0202
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SYN-DOMAIN.
- Problem: Papers about SYN-DOMAIN rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Synthetic-to-real gap for smoke is lighting/scattering, not texture GAN fidelity. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SYN-DOMAIN.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SYN-DOMAIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-DOMAIN

### IDEA-C-0203
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SYN-DOMAIN.
- Problem: Papers about SYN-DOMAIN rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Synthetic-to-real gap for smoke is lighting/scattering, not texture GAN fidelity. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SYN-DOMAIN.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SYN-DOMAIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-DOMAIN

### IDEA-C-0204
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SYN-DOMAIN.
- Problem: Papers about SYN-DOMAIN rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Synthetic-to-real gap for smoke is lighting/scattering, not texture GAN fidelity. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SYN-DOMAIN.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SYN-DOMAIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-DOMAIN

### IDEA-C-0205
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SYN-DOMAIN.
- Problem: Papers about SYN-DOMAIN rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Synthetic-to-real gap for smoke is lighting/scattering, not texture GAN fidelity. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SYN-DOMAIN.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SYN-DOMAIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-DOMAIN

### IDEA-C-0206
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SYN-DOMAIN.
- Problem: Papers about SYN-DOMAIN rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Synthetic-to-real gap for smoke is lighting/scattering, not texture GAN fidelity. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SYN-DOMAIN.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SYN-DOMAIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-DOMAIN

### IDEA-C-0207
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SYN-DOMAIN.
- Problem: Papers about SYN-DOMAIN rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Synthetic-to-real gap for smoke is lighting/scattering, not texture GAN fidelity. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SYN-DOMAIN.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SYN-DOMAIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-DOMAIN

### IDEA-C-0208
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SYN-DOMAIN.
- Problem: Papers about SYN-DOMAIN rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Synthetic-to-real gap for smoke is lighting/scattering, not texture GAN fidelity. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SYN-DOMAIN.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SYN-DOMAIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SYN-DOMAIN

### IDEA-C-0209
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind VLM-POOL.
- Problem: Papers about VLM-POOL rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If VLM global pooling destroys the spatial signal needed for dense prediction; language helps class identity not masks. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for VLM-POOL.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard VLM-POOL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-POOL

### IDEA-C-0210
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind VLM-POOL.
- Problem: Papers about VLM-POOL rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If VLM global pooling destroys the spatial signal needed for dense prediction; language helps class identity not masks. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for VLM-POOL.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard VLM-POOL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-POOL

### IDEA-C-0211
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind VLM-POOL.
- Problem: Papers about VLM-POOL rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If VLM global pooling destroys the spatial signal needed for dense prediction; language helps class identity not masks. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for VLM-POOL.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard VLM-POOL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-POOL

### IDEA-C-0212
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind VLM-POOL.
- Problem: Papers about VLM-POOL rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If VLM global pooling destroys the spatial signal needed for dense prediction; language helps class identity not masks. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for VLM-POOL.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard VLM-POOL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-POOL

### IDEA-C-0213
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind VLM-POOL.
- Problem: Papers about VLM-POOL rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If VLM global pooling destroys the spatial signal needed for dense prediction; language helps class identity not masks. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for VLM-POOL.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard VLM-POOL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-POOL

### IDEA-C-0214
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind VLM-POOL.
- Problem: Papers about VLM-POOL rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If VLM global pooling destroys the spatial signal needed for dense prediction; language helps class identity not masks. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for VLM-POOL.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard VLM-POOL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-POOL

### IDEA-C-0215
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind VLM-POOL.
- Problem: Papers about VLM-POOL rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If VLM global pooling destroys the spatial signal needed for dense prediction; language helps class identity not masks. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for VLM-POOL.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard VLM-POOL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-POOL

### IDEA-C-0216
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind VLM-POOL.
- Problem: Papers about VLM-POOL rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If VLM global pooling destroys the spatial signal needed for dense prediction; language helps class identity not masks. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for VLM-POOL.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard VLM-POOL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-POOL

### IDEA-C-0217
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind VLM-TOKEN.
- Problem: Papers about VLM-TOKEN rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Open-vocab segmentation is retrieval of class tokens, not pixel grouping; grouping still needs an objectness model. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for VLM-TOKEN.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard VLM-TOKEN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-TOKEN

### IDEA-C-0218
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind VLM-TOKEN.
- Problem: Papers about VLM-TOKEN rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Open-vocab segmentation is retrieval of class tokens, not pixel grouping; grouping still needs an objectness model. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for VLM-TOKEN.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard VLM-TOKEN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-TOKEN

### IDEA-C-0219
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind VLM-TOKEN.
- Problem: Papers about VLM-TOKEN rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Open-vocab segmentation is retrieval of class tokens, not pixel grouping; grouping still needs an objectness model. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for VLM-TOKEN.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard VLM-TOKEN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-TOKEN

### IDEA-C-0220
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind VLM-TOKEN.
- Problem: Papers about VLM-TOKEN rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Open-vocab segmentation is retrieval of class tokens, not pixel grouping; grouping still needs an objectness model. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for VLM-TOKEN.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard VLM-TOKEN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-TOKEN

### IDEA-C-0221
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind VLM-TOKEN.
- Problem: Papers about VLM-TOKEN rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Open-vocab segmentation is retrieval of class tokens, not pixel grouping; grouping still needs an objectness model. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for VLM-TOKEN.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard VLM-TOKEN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-TOKEN

### IDEA-C-0222
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind VLM-TOKEN.
- Problem: Papers about VLM-TOKEN rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Open-vocab segmentation is retrieval of class tokens, not pixel grouping; grouping still needs an objectness model. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for VLM-TOKEN.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard VLM-TOKEN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-TOKEN

### IDEA-C-0223
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind VLM-TOKEN.
- Problem: Papers about VLM-TOKEN rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Open-vocab segmentation is retrieval of class tokens, not pixel grouping; grouping still needs an objectness model. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for VLM-TOKEN.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard VLM-TOKEN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-TOKEN

### IDEA-C-0224
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind VLM-TOKEN.
- Problem: Papers about VLM-TOKEN rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Open-vocab segmentation is retrieval of class tokens, not pixel grouping; grouping still needs an objectness model. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for VLM-TOKEN.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard VLM-TOKEN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: VLM-TOKEN

### IDEA-C-0225
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind PROMPT-LEARN.
- Problem: Papers about PROMPT-LEARN rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Prompt embeddings memorize dataset names rather than visual concepts; they fail on renamed classes. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for PROMPT-LEARN.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard PROMPT-LEARN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PROMPT-LEARN

### IDEA-C-0226
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind PROMPT-LEARN.
- Problem: Papers about PROMPT-LEARN rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Prompt embeddings memorize dataset names rather than visual concepts; they fail on renamed classes. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for PROMPT-LEARN.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard PROMPT-LEARN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PROMPT-LEARN

### IDEA-C-0227
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind PROMPT-LEARN.
- Problem: Papers about PROMPT-LEARN rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Prompt embeddings memorize dataset names rather than visual concepts; they fail on renamed classes. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for PROMPT-LEARN.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard PROMPT-LEARN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PROMPT-LEARN

### IDEA-C-0228
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind PROMPT-LEARN.
- Problem: Papers about PROMPT-LEARN rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Prompt embeddings memorize dataset names rather than visual concepts; they fail on renamed classes. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for PROMPT-LEARN.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard PROMPT-LEARN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PROMPT-LEARN

### IDEA-C-0229
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind PROMPT-LEARN.
- Problem: Papers about PROMPT-LEARN rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Prompt embeddings memorize dataset names rather than visual concepts; they fail on renamed classes. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for PROMPT-LEARN.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard PROMPT-LEARN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PROMPT-LEARN

### IDEA-C-0230
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind PROMPT-LEARN.
- Problem: Papers about PROMPT-LEARN rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Prompt embeddings memorize dataset names rather than visual concepts; they fail on renamed classes. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for PROMPT-LEARN.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard PROMPT-LEARN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PROMPT-LEARN

### IDEA-C-0231
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind PROMPT-LEARN.
- Problem: Papers about PROMPT-LEARN rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Prompt embeddings memorize dataset names rather than visual concepts; they fail on renamed classes. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for PROMPT-LEARN.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard PROMPT-LEARN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PROMPT-LEARN

### IDEA-C-0232
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind PROMPT-LEARN.
- Problem: Papers about PROMPT-LEARN rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Prompt embeddings memorize dataset names rather than visual concepts; they fail on renamed classes. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for PROMPT-LEARN.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard PROMPT-LEARN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: PROMPT-LEARN

### IDEA-C-0233
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind FEWSHOT-OVERLAP.
- Problem: Papers about FEWSHOT-OVERLAP rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Few-shot medical segmentation is secretly many-shot via pretraining overlap with the same public organs. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for FEWSHOT-OVERLAP.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard FEWSHOT-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FEWSHOT-OVERLAP

### IDEA-C-0234
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind FEWSHOT-OVERLAP.
- Problem: Papers about FEWSHOT-OVERLAP rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Few-shot medical segmentation is secretly many-shot via pretraining overlap with the same public organs. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for FEWSHOT-OVERLAP.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard FEWSHOT-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FEWSHOT-OVERLAP

### IDEA-C-0235
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind FEWSHOT-OVERLAP.
- Problem: Papers about FEWSHOT-OVERLAP rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Few-shot medical segmentation is secretly many-shot via pretraining overlap with the same public organs. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for FEWSHOT-OVERLAP.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard FEWSHOT-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FEWSHOT-OVERLAP

### IDEA-C-0236
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind FEWSHOT-OVERLAP.
- Problem: Papers about FEWSHOT-OVERLAP rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Few-shot medical segmentation is secretly many-shot via pretraining overlap with the same public organs. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for FEWSHOT-OVERLAP.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard FEWSHOT-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FEWSHOT-OVERLAP

### IDEA-C-0237
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind FEWSHOT-OVERLAP.
- Problem: Papers about FEWSHOT-OVERLAP rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Few-shot medical segmentation is secretly many-shot via pretraining overlap with the same public organs. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for FEWSHOT-OVERLAP.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard FEWSHOT-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FEWSHOT-OVERLAP

### IDEA-C-0238
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind FEWSHOT-OVERLAP.
- Problem: Papers about FEWSHOT-OVERLAP rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Few-shot medical segmentation is secretly many-shot via pretraining overlap with the same public organs. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for FEWSHOT-OVERLAP.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard FEWSHOT-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FEWSHOT-OVERLAP

### IDEA-C-0239
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind FEWSHOT-OVERLAP.
- Problem: Papers about FEWSHOT-OVERLAP rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Few-shot medical segmentation is secretly many-shot via pretraining overlap with the same public organs. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for FEWSHOT-OVERLAP.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard FEWSHOT-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FEWSHOT-OVERLAP

### IDEA-C-0240
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind FEWSHOT-OVERLAP.
- Problem: Papers about FEWSHOT-OVERLAP rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Few-shot medical segmentation is secretly many-shot via pretraining overlap with the same public organs. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for FEWSHOT-OVERLAP.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard FEWSHOT-OVERLAP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FEWSHOT-OVERLAP

### IDEA-C-0241
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind WEAK-BOX.
- Problem: Papers about WEAK-BOX rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Box-supervised SAM self-training confirms box bias and never recovers concavities. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for WEAK-BOX.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard WEAK-BOX intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: WEAK-BOX

### IDEA-C-0242
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind WEAK-BOX.
- Problem: Papers about WEAK-BOX rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Box-supervised SAM self-training confirms box bias and never recovers concavities. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for WEAK-BOX.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard WEAK-BOX intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: WEAK-BOX

### IDEA-C-0243
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind WEAK-BOX.
- Problem: Papers about WEAK-BOX rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Box-supervised SAM self-training confirms box bias and never recovers concavities. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for WEAK-BOX.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard WEAK-BOX intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: WEAK-BOX

### IDEA-C-0244
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind WEAK-BOX.
- Problem: Papers about WEAK-BOX rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Box-supervised SAM self-training confirms box bias and never recovers concavities. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for WEAK-BOX.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard WEAK-BOX intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: WEAK-BOX

### IDEA-C-0245
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind WEAK-BOX.
- Problem: Papers about WEAK-BOX rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Box-supervised SAM self-training confirms box bias and never recovers concavities. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for WEAK-BOX.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard WEAK-BOX intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: WEAK-BOX

### IDEA-C-0246
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind WEAK-BOX.
- Problem: Papers about WEAK-BOX rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Box-supervised SAM self-training confirms box bias and never recovers concavities. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for WEAK-BOX.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard WEAK-BOX intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: WEAK-BOX

### IDEA-C-0247
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind WEAK-BOX.
- Problem: Papers about WEAK-BOX rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Box-supervised SAM self-training confirms box bias and never recovers concavities. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for WEAK-BOX.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard WEAK-BOX intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: WEAK-BOX

### IDEA-C-0248
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind WEAK-BOX.
- Problem: Papers about WEAK-BOX rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Box-supervised SAM self-training confirms box bias and never recovers concavities. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for WEAK-BOX.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard WEAK-BOX intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: WEAK-BOX

### IDEA-C-0249
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SELF-TRAIN-BIAS.
- Problem: Papers about SELF-TRAIN-BIAS rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Pseudo-label self-training on SAM increases precision on easy objects and decreases recall on amorphous ones. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SELF-TRAIN-BIAS.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SELF-TRAIN-BIAS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELF-TRAIN-BIAS

### IDEA-C-0250
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SELF-TRAIN-BIAS.
- Problem: Papers about SELF-TRAIN-BIAS rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Pseudo-label self-training on SAM increases precision on easy objects and decreases recall on amorphous ones. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SELF-TRAIN-BIAS.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SELF-TRAIN-BIAS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELF-TRAIN-BIAS

### IDEA-C-0251
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SELF-TRAIN-BIAS.
- Problem: Papers about SELF-TRAIN-BIAS rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Pseudo-label self-training on SAM increases precision on easy objects and decreases recall on amorphous ones. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SELF-TRAIN-BIAS.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SELF-TRAIN-BIAS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELF-TRAIN-BIAS

### IDEA-C-0252
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SELF-TRAIN-BIAS.
- Problem: Papers about SELF-TRAIN-BIAS rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Pseudo-label self-training on SAM increases precision on easy objects and decreases recall on amorphous ones. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SELF-TRAIN-BIAS.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SELF-TRAIN-BIAS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELF-TRAIN-BIAS

### IDEA-C-0253
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SELF-TRAIN-BIAS.
- Problem: Papers about SELF-TRAIN-BIAS rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Pseudo-label self-training on SAM increases precision on easy objects and decreases recall on amorphous ones. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SELF-TRAIN-BIAS.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SELF-TRAIN-BIAS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELF-TRAIN-BIAS

### IDEA-C-0254
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SELF-TRAIN-BIAS.
- Problem: Papers about SELF-TRAIN-BIAS rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Pseudo-label self-training on SAM increases precision on easy objects and decreases recall on amorphous ones. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SELF-TRAIN-BIAS.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SELF-TRAIN-BIAS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELF-TRAIN-BIAS

### IDEA-C-0255
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SELF-TRAIN-BIAS.
- Problem: Papers about SELF-TRAIN-BIAS rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Pseudo-label self-training on SAM increases precision on easy objects and decreases recall on amorphous ones. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SELF-TRAIN-BIAS.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SELF-TRAIN-BIAS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELF-TRAIN-BIAS

### IDEA-C-0256
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SELF-TRAIN-BIAS.
- Problem: Papers about SELF-TRAIN-BIAS rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Pseudo-label self-training on SAM increases precision on easy objects and decreases recall on amorphous ones. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SELF-TRAIN-BIAS.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SELF-TRAIN-BIAS intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELF-TRAIN-BIAS

### IDEA-C-0257
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind DA-TEXTURE.
- Problem: Papers about DA-TEXTURE rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Unsupervised DA matches stain/texture and ignores anatomy; target Dice rises while topology errors rise. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for DA-TEXTURE.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard DA-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DA-TEXTURE

### IDEA-C-0258
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind DA-TEXTURE.
- Problem: Papers about DA-TEXTURE rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Unsupervised DA matches stain/texture and ignores anatomy; target Dice rises while topology errors rise. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for DA-TEXTURE.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard DA-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DA-TEXTURE

### IDEA-C-0259
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind DA-TEXTURE.
- Problem: Papers about DA-TEXTURE rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Unsupervised DA matches stain/texture and ignores anatomy; target Dice rises while topology errors rise. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for DA-TEXTURE.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard DA-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DA-TEXTURE

### IDEA-C-0260
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind DA-TEXTURE.
- Problem: Papers about DA-TEXTURE rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Unsupervised DA matches stain/texture and ignores anatomy; target Dice rises while topology errors rise. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for DA-TEXTURE.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard DA-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DA-TEXTURE

### IDEA-C-0261
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind DA-TEXTURE.
- Problem: Papers about DA-TEXTURE rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Unsupervised DA matches stain/texture and ignores anatomy; target Dice rises while topology errors rise. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for DA-TEXTURE.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard DA-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DA-TEXTURE

### IDEA-C-0262
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind DA-TEXTURE.
- Problem: Papers about DA-TEXTURE rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Unsupervised DA matches stain/texture and ignores anatomy; target Dice rises while topology errors rise. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for DA-TEXTURE.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard DA-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DA-TEXTURE

### IDEA-C-0263
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind DA-TEXTURE.
- Problem: Papers about DA-TEXTURE rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Unsupervised DA matches stain/texture and ignores anatomy; target Dice rises while topology errors rise. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for DA-TEXTURE.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard DA-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DA-TEXTURE

### IDEA-C-0264
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind DA-TEXTURE.
- Problem: Papers about DA-TEXTURE rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Unsupervised DA matches stain/texture and ignores anatomy; target Dice rises while topology errors rise. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for DA-TEXTURE.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard DA-TEXTURE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: DA-TEXTURE

### IDEA-C-0265
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind LONGTAIL-DET.
- Problem: Papers about LONGTAIL-DET rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Detection AP gains from VFMs are concentrated in frequent classes; tail classes regress. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for LONGTAIL-DET.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard LONGTAIL-DET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LONGTAIL-DET

### IDEA-C-0266
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind LONGTAIL-DET.
- Problem: Papers about LONGTAIL-DET rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Detection AP gains from VFMs are concentrated in frequent classes; tail classes regress. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for LONGTAIL-DET.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard LONGTAIL-DET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LONGTAIL-DET

### IDEA-C-0267
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind LONGTAIL-DET.
- Problem: Papers about LONGTAIL-DET rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Detection AP gains from VFMs are concentrated in frequent classes; tail classes regress. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for LONGTAIL-DET.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard LONGTAIL-DET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LONGTAIL-DET

### IDEA-C-0268
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind LONGTAIL-DET.
- Problem: Papers about LONGTAIL-DET rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Detection AP gains from VFMs are concentrated in frequent classes; tail classes regress. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for LONGTAIL-DET.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard LONGTAIL-DET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LONGTAIL-DET

### IDEA-C-0269
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind LONGTAIL-DET.
- Problem: Papers about LONGTAIL-DET rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Detection AP gains from VFMs are concentrated in frequent classes; tail classes regress. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for LONGTAIL-DET.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard LONGTAIL-DET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LONGTAIL-DET

### IDEA-C-0270
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind LONGTAIL-DET.
- Problem: Papers about LONGTAIL-DET rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Detection AP gains from VFMs are concentrated in frequent classes; tail classes regress. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for LONGTAIL-DET.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard LONGTAIL-DET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LONGTAIL-DET

### IDEA-C-0271
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind LONGTAIL-DET.
- Problem: Papers about LONGTAIL-DET rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Detection AP gains from VFMs are concentrated in frequent classes; tail classes regress. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for LONGTAIL-DET.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard LONGTAIL-DET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LONGTAIL-DET

### IDEA-C-0272
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind LONGTAIL-DET.
- Problem: Papers about LONGTAIL-DET rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Detection AP gains from VFMs are concentrated in frequent classes; tail classes regress. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for LONGTAIL-DET.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard LONGTAIL-DET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: LONGTAIL-DET

### IDEA-C-0273
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind UNCERT-ERROR.
- Problem: Papers about UNCERT-ERROR rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If MC-dropout / ensembles on SAM do not track true error on transparent objects. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for UNCERT-ERROR.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard UNCERT-ERROR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: UNCERT-ERROR

### IDEA-C-0274
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind UNCERT-ERROR.
- Problem: Papers about UNCERT-ERROR rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If MC-dropout / ensembles on SAM do not track true error on transparent objects. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for UNCERT-ERROR.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard UNCERT-ERROR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: UNCERT-ERROR

### IDEA-C-0275
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind UNCERT-ERROR.
- Problem: Papers about UNCERT-ERROR rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If MC-dropout / ensembles on SAM do not track true error on transparent objects. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for UNCERT-ERROR.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard UNCERT-ERROR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: UNCERT-ERROR

### IDEA-C-0276
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind UNCERT-ERROR.
- Problem: Papers about UNCERT-ERROR rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If MC-dropout / ensembles on SAM do not track true error on transparent objects. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for UNCERT-ERROR.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard UNCERT-ERROR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: UNCERT-ERROR

### IDEA-C-0277
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind UNCERT-ERROR.
- Problem: Papers about UNCERT-ERROR rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If MC-dropout / ensembles on SAM do not track true error on transparent objects. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for UNCERT-ERROR.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard UNCERT-ERROR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: UNCERT-ERROR

### IDEA-C-0278
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind UNCERT-ERROR.
- Problem: Papers about UNCERT-ERROR rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If MC-dropout / ensembles on SAM do not track true error on transparent objects. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for UNCERT-ERROR.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard UNCERT-ERROR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: UNCERT-ERROR

### IDEA-C-0279
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind UNCERT-ERROR.
- Problem: Papers about UNCERT-ERROR rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If MC-dropout / ensembles on SAM do not track true error on transparent objects. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for UNCERT-ERROR.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard UNCERT-ERROR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: UNCERT-ERROR

### IDEA-C-0280
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind UNCERT-ERROR.
- Problem: Papers about UNCERT-ERROR rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If MC-dropout / ensembles on SAM do not track true error on transparent objects. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for UNCERT-ERROR.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard UNCERT-ERROR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: UNCERT-ERROR

### IDEA-C-0281
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind CLICK-BUDGET.
- Problem: Papers about CLICK-BUDGET rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Interactive SAM annotation has diminishing returns after 2 clicks on objects and no returns on smoke. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for CLICK-BUDGET.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard CLICK-BUDGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CLICK-BUDGET

### IDEA-C-0282
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind CLICK-BUDGET.
- Problem: Papers about CLICK-BUDGET rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Interactive SAM annotation has diminishing returns after 2 clicks on objects and no returns on smoke. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for CLICK-BUDGET.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard CLICK-BUDGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CLICK-BUDGET

### IDEA-C-0283
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind CLICK-BUDGET.
- Problem: Papers about CLICK-BUDGET rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Interactive SAM annotation has diminishing returns after 2 clicks on objects and no returns on smoke. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for CLICK-BUDGET.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard CLICK-BUDGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CLICK-BUDGET

### IDEA-C-0284
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind CLICK-BUDGET.
- Problem: Papers about CLICK-BUDGET rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Interactive SAM annotation has diminishing returns after 2 clicks on objects and no returns on smoke. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for CLICK-BUDGET.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard CLICK-BUDGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CLICK-BUDGET

### IDEA-C-0285
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind CLICK-BUDGET.
- Problem: Papers about CLICK-BUDGET rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Interactive SAM annotation has diminishing returns after 2 clicks on objects and no returns on smoke. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for CLICK-BUDGET.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard CLICK-BUDGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CLICK-BUDGET

### IDEA-C-0286
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind CLICK-BUDGET.
- Problem: Papers about CLICK-BUDGET rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Interactive SAM annotation has diminishing returns after 2 clicks on objects and no returns on smoke. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for CLICK-BUDGET.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard CLICK-BUDGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CLICK-BUDGET

### IDEA-C-0287
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind CLICK-BUDGET.
- Problem: Papers about CLICK-BUDGET rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Interactive SAM annotation has diminishing returns after 2 clicks on objects and no returns on smoke. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for CLICK-BUDGET.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard CLICK-BUDGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CLICK-BUDGET

### IDEA-C-0288
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind CLICK-BUDGET.
- Problem: Papers about CLICK-BUDGET rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Interactive SAM annotation has diminishing returns after 2 clicks on objects and no returns on smoke. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for CLICK-BUDGET.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard CLICK-BUDGET intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CLICK-BUDGET

### IDEA-C-0289
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind NEGRESULT-SCALE.
- Problem: Papers about NEGRESULT-SCALE rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Scaling SAM decoder width does not fix amorphous targets; encoder objectness is the bottleneck. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for NEGRESULT-SCALE.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard NEGRESULT-SCALE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-SCALE

### IDEA-C-0290
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind NEGRESULT-SCALE.
- Problem: Papers about NEGRESULT-SCALE rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Scaling SAM decoder width does not fix amorphous targets; encoder objectness is the bottleneck. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for NEGRESULT-SCALE.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard NEGRESULT-SCALE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-SCALE

### IDEA-C-0291
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind NEGRESULT-SCALE.
- Problem: Papers about NEGRESULT-SCALE rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Scaling SAM decoder width does not fix amorphous targets; encoder objectness is the bottleneck. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for NEGRESULT-SCALE.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard NEGRESULT-SCALE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-SCALE

### IDEA-C-0292
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind NEGRESULT-SCALE.
- Problem: Papers about NEGRESULT-SCALE rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Scaling SAM decoder width does not fix amorphous targets; encoder objectness is the bottleneck. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for NEGRESULT-SCALE.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard NEGRESULT-SCALE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-SCALE

### IDEA-C-0293
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind NEGRESULT-SCALE.
- Problem: Papers about NEGRESULT-SCALE rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Scaling SAM decoder width does not fix amorphous targets; encoder objectness is the bottleneck. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for NEGRESULT-SCALE.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard NEGRESULT-SCALE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-SCALE

### IDEA-C-0294
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind NEGRESULT-SCALE.
- Problem: Papers about NEGRESULT-SCALE rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Scaling SAM decoder width does not fix amorphous targets; encoder objectness is the bottleneck. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for NEGRESULT-SCALE.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard NEGRESULT-SCALE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-SCALE

### IDEA-C-0295
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind NEGRESULT-SCALE.
- Problem: Papers about NEGRESULT-SCALE rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Scaling SAM decoder width does not fix amorphous targets; encoder objectness is the bottleneck. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for NEGRESULT-SCALE.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard NEGRESULT-SCALE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-SCALE

### IDEA-C-0296
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind NEGRESULT-SCALE.
- Problem: Papers about NEGRESULT-SCALE rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Scaling SAM decoder width does not fix amorphous targets; encoder objectness is the bottleneck. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for NEGRESULT-SCALE.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard NEGRESULT-SCALE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-SCALE

### IDEA-C-0297
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind NEGRESULT-DATA.
- Problem: Papers about NEGRESULT-DATA rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If More in-domain labeled smoke images beat any prompt engineering given equal annotation minutes. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for NEGRESULT-DATA.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard NEGRESULT-DATA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-DATA

### IDEA-C-0298
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind NEGRESULT-DATA.
- Problem: Papers about NEGRESULT-DATA rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If More in-domain labeled smoke images beat any prompt engineering given equal annotation minutes. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for NEGRESULT-DATA.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard NEGRESULT-DATA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-DATA

### IDEA-C-0299
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind NEGRESULT-DATA.
- Problem: Papers about NEGRESULT-DATA rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If More in-domain labeled smoke images beat any prompt engineering given equal annotation minutes. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for NEGRESULT-DATA.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard NEGRESULT-DATA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-DATA

### IDEA-C-0300
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind NEGRESULT-DATA.
- Problem: Papers about NEGRESULT-DATA rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If More in-domain labeled smoke images beat any prompt engineering given equal annotation minutes. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for NEGRESULT-DATA.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard NEGRESULT-DATA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-DATA

### IDEA-C-0301
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind NEGRESULT-DATA.
- Problem: Papers about NEGRESULT-DATA rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If More in-domain labeled smoke images beat any prompt engineering given equal annotation minutes. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for NEGRESULT-DATA.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard NEGRESULT-DATA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-DATA

### IDEA-C-0302
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind NEGRESULT-DATA.
- Problem: Papers about NEGRESULT-DATA rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If More in-domain labeled smoke images beat any prompt engineering given equal annotation minutes. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for NEGRESULT-DATA.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard NEGRESULT-DATA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-DATA

### IDEA-C-0303
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind NEGRESULT-DATA.
- Problem: Papers about NEGRESULT-DATA rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If More in-domain labeled smoke images beat any prompt engineering given equal annotation minutes. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for NEGRESULT-DATA.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard NEGRESULT-DATA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-DATA

### IDEA-C-0304
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind NEGRESULT-DATA.
- Problem: Papers about NEGRESULT-DATA rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If More in-domain labeled smoke images beat any prompt engineering given equal annotation minutes. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for NEGRESULT-DATA.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard NEGRESULT-DATA intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: NEGRESULT-DATA

### IDEA-C-0305
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind COMPUTE-FAIR.
- Problem: Papers about COMPUTE-FAIR rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Published VFM wins disappear under equal-FLOP / equal-annotation budgets vs nnU-Net. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for COMPUTE-FAIR.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard COMPUTE-FAIR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: COMPUTE-FAIR

### IDEA-C-0306
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind COMPUTE-FAIR.
- Problem: Papers about COMPUTE-FAIR rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Published VFM wins disappear under equal-FLOP / equal-annotation budgets vs nnU-Net. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for COMPUTE-FAIR.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard COMPUTE-FAIR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: COMPUTE-FAIR

### IDEA-C-0307
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind COMPUTE-FAIR.
- Problem: Papers about COMPUTE-FAIR rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Published VFM wins disappear under equal-FLOP / equal-annotation budgets vs nnU-Net. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for COMPUTE-FAIR.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard COMPUTE-FAIR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: COMPUTE-FAIR

### IDEA-C-0308
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind COMPUTE-FAIR.
- Problem: Papers about COMPUTE-FAIR rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Published VFM wins disappear under equal-FLOP / equal-annotation budgets vs nnU-Net. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for COMPUTE-FAIR.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard COMPUTE-FAIR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: COMPUTE-FAIR

### IDEA-C-0309
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind COMPUTE-FAIR.
- Problem: Papers about COMPUTE-FAIR rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Published VFM wins disappear under equal-FLOP / equal-annotation budgets vs nnU-Net. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for COMPUTE-FAIR.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard COMPUTE-FAIR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: COMPUTE-FAIR

### IDEA-C-0310
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind COMPUTE-FAIR.
- Problem: Papers about COMPUTE-FAIR rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Published VFM wins disappear under equal-FLOP / equal-annotation budgets vs nnU-Net. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for COMPUTE-FAIR.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard COMPUTE-FAIR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: COMPUTE-FAIR

### IDEA-C-0311
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind COMPUTE-FAIR.
- Problem: Papers about COMPUTE-FAIR rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Published VFM wins disappear under equal-FLOP / equal-annotation budgets vs nnU-Net. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for COMPUTE-FAIR.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard COMPUTE-FAIR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: COMPUTE-FAIR

### IDEA-C-0312
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind COMPUTE-FAIR.
- Problem: Papers about COMPUTE-FAIR rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Published VFM wins disappear under equal-FLOP / equal-annotation budgets vs nnU-Net. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for COMPUTE-FAIR.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard COMPUTE-FAIR intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: COMPUTE-FAIR

### IDEA-C-0313
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind TTA-PROMPT.
- Problem: Papers about TTA-PROMPT rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Test-time prompt ensembling helps more than extra training for SAM on medical organs. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for TTA-PROMPT.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard TTA-PROMPT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: TTA-PROMPT

### IDEA-C-0314
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind TTA-PROMPT.
- Problem: Papers about TTA-PROMPT rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Test-time prompt ensembling helps more than extra training for SAM on medical organs. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for TTA-PROMPT.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard TTA-PROMPT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: TTA-PROMPT

### IDEA-C-0315
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind TTA-PROMPT.
- Problem: Papers about TTA-PROMPT rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Test-time prompt ensembling helps more than extra training for SAM on medical organs. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for TTA-PROMPT.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard TTA-PROMPT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: TTA-PROMPT

### IDEA-C-0316
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind TTA-PROMPT.
- Problem: Papers about TTA-PROMPT rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Test-time prompt ensembling helps more than extra training for SAM on medical organs. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for TTA-PROMPT.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard TTA-PROMPT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: TTA-PROMPT

### IDEA-C-0317
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind TTA-PROMPT.
- Problem: Papers about TTA-PROMPT rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Test-time prompt ensembling helps more than extra training for SAM on medical organs. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for TTA-PROMPT.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard TTA-PROMPT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: TTA-PROMPT

### IDEA-C-0318
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind TTA-PROMPT.
- Problem: Papers about TTA-PROMPT rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Test-time prompt ensembling helps more than extra training for SAM on medical organs. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for TTA-PROMPT.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard TTA-PROMPT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: TTA-PROMPT

### IDEA-C-0319
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind TTA-PROMPT.
- Problem: Papers about TTA-PROMPT rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Test-time prompt ensembling helps more than extra training for SAM on medical organs. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for TTA-PROMPT.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard TTA-PROMPT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: TTA-PROMPT

### IDEA-C-0320
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind TTA-PROMPT.
- Problem: Papers about TTA-PROMPT rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Test-time prompt ensembling helps more than extra training for SAM on medical organs. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for TTA-PROMPT.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard TTA-PROMPT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: TTA-PROMPT

### IDEA-C-0321
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind REFRACTION.
- Problem: Papers about REFRACTION rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Transparent object errors are refraction/background-through-object, not low contrast; matting features beat SAM tokens. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for REFRACTION.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard REFRACTION intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REFRACTION

### IDEA-C-0322
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind REFRACTION.
- Problem: Papers about REFRACTION rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Transparent object errors are refraction/background-through-object, not low contrast; matting features beat SAM tokens. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for REFRACTION.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard REFRACTION intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REFRACTION

### IDEA-C-0323
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind REFRACTION.
- Problem: Papers about REFRACTION rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Transparent object errors are refraction/background-through-object, not low contrast; matting features beat SAM tokens. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for REFRACTION.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard REFRACTION intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REFRACTION

### IDEA-C-0324
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind REFRACTION.
- Problem: Papers about REFRACTION rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Transparent object errors are refraction/background-through-object, not low contrast; matting features beat SAM tokens. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for REFRACTION.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard REFRACTION intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REFRACTION

### IDEA-C-0325
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind REFRACTION.
- Problem: Papers about REFRACTION rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Transparent object errors are refraction/background-through-object, not low contrast; matting features beat SAM tokens. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for REFRACTION.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard REFRACTION intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REFRACTION

### IDEA-C-0326
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind REFRACTION.
- Problem: Papers about REFRACTION rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Transparent object errors are refraction/background-through-object, not low contrast; matting features beat SAM tokens. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for REFRACTION.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard REFRACTION intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REFRACTION

### IDEA-C-0327
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind REFRACTION.
- Problem: Papers about REFRACTION rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Transparent object errors are refraction/background-through-object, not low contrast; matting features beat SAM tokens. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for REFRACTION.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard REFRACTION intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REFRACTION

### IDEA-C-0328
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind REFRACTION.
- Problem: Papers about REFRACTION rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Transparent object errors are refraction/background-through-object, not low contrast; matting features beat SAM tokens. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for REFRACTION.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard REFRACTION intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REFRACTION

### IDEA-C-0329
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind FIRE-TEMPORAL.
- Problem: Papers about FIRE-TEMPORAL rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Fire is better as a temporal residual than an appearance class; single-frame SAM2 underperforms frame-diff linear probes. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for FIRE-TEMPORAL.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard FIRE-TEMPORAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FIRE-TEMPORAL

### IDEA-C-0330
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind FIRE-TEMPORAL.
- Problem: Papers about FIRE-TEMPORAL rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Fire is better as a temporal residual than an appearance class; single-frame SAM2 underperforms frame-diff linear probes. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for FIRE-TEMPORAL.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard FIRE-TEMPORAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FIRE-TEMPORAL

### IDEA-C-0331
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind FIRE-TEMPORAL.
- Problem: Papers about FIRE-TEMPORAL rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Fire is better as a temporal residual than an appearance class; single-frame SAM2 underperforms frame-diff linear probes. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for FIRE-TEMPORAL.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard FIRE-TEMPORAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FIRE-TEMPORAL

### IDEA-C-0332
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind FIRE-TEMPORAL.
- Problem: Papers about FIRE-TEMPORAL rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Fire is better as a temporal residual than an appearance class; single-frame SAM2 underperforms frame-diff linear probes. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for FIRE-TEMPORAL.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard FIRE-TEMPORAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FIRE-TEMPORAL

### IDEA-C-0333
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind FIRE-TEMPORAL.
- Problem: Papers about FIRE-TEMPORAL rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Fire is better as a temporal residual than an appearance class; single-frame SAM2 underperforms frame-diff linear probes. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for FIRE-TEMPORAL.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard FIRE-TEMPORAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FIRE-TEMPORAL

### IDEA-C-0334
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind FIRE-TEMPORAL.
- Problem: Papers about FIRE-TEMPORAL rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Fire is better as a temporal residual than an appearance class; single-frame SAM2 underperforms frame-diff linear probes. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for FIRE-TEMPORAL.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard FIRE-TEMPORAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FIRE-TEMPORAL

### IDEA-C-0335
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind FIRE-TEMPORAL.
- Problem: Papers about FIRE-TEMPORAL rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Fire is better as a temporal residual than an appearance class; single-frame SAM2 underperforms frame-diff linear probes. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for FIRE-TEMPORAL.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard FIRE-TEMPORAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FIRE-TEMPORAL

### IDEA-C-0336
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind FIRE-TEMPORAL.
- Problem: Papers about FIRE-TEMPORAL rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Fire is better as a temporal residual than an appearance class; single-frame SAM2 underperforms frame-diff linear probes. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for FIRE-TEMPORAL.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard FIRE-TEMPORAL intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: FIRE-TEMPORAL

### IDEA-C-0337
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SMOKE-DENSITY.
- Problem: Papers about SMOKE-DENSITY rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Smoke should be a continuous density regression; binarization at 0.5 is an evaluation bug not a model bug. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SMOKE-DENSITY.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SMOKE-DENSITY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMOKE-DENSITY

### IDEA-C-0338
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SMOKE-DENSITY.
- Problem: Papers about SMOKE-DENSITY rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Smoke should be a continuous density regression; binarization at 0.5 is an evaluation bug not a model bug. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SMOKE-DENSITY.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SMOKE-DENSITY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMOKE-DENSITY

### IDEA-C-0339
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SMOKE-DENSITY.
- Problem: Papers about SMOKE-DENSITY rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Smoke should be a continuous density regression; binarization at 0.5 is an evaluation bug not a model bug. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SMOKE-DENSITY.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SMOKE-DENSITY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMOKE-DENSITY

### IDEA-C-0340
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SMOKE-DENSITY.
- Problem: Papers about SMOKE-DENSITY rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Smoke should be a continuous density regression; binarization at 0.5 is an evaluation bug not a model bug. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SMOKE-DENSITY.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SMOKE-DENSITY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMOKE-DENSITY

### IDEA-C-0341
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SMOKE-DENSITY.
- Problem: Papers about SMOKE-DENSITY rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Smoke should be a continuous density regression; binarization at 0.5 is an evaluation bug not a model bug. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SMOKE-DENSITY.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SMOKE-DENSITY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMOKE-DENSITY

### IDEA-C-0342
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SMOKE-DENSITY.
- Problem: Papers about SMOKE-DENSITY rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Smoke should be a continuous density regression; binarization at 0.5 is an evaluation bug not a model bug. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SMOKE-DENSITY.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SMOKE-DENSITY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMOKE-DENSITY

### IDEA-C-0343
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SMOKE-DENSITY.
- Problem: Papers about SMOKE-DENSITY rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Smoke should be a continuous density regression; binarization at 0.5 is an evaluation bug not a model bug. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SMOKE-DENSITY.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SMOKE-DENSITY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMOKE-DENSITY

### IDEA-C-0344
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SMOKE-DENSITY.
- Problem: Papers about SMOKE-DENSITY rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Smoke should be a continuous density regression; binarization at 0.5 is an evaluation bug not a model bug. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SMOKE-DENSITY.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SMOKE-DENSITY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SMOKE-DENSITY

### IDEA-C-0345
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind INFILTRATIVE.
- Problem: Papers about INFILTRATIVE rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Infiltrative tumors violate instance assumptions; connected-component postprocess of SAM is harmful. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for INFILTRATIVE.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard INFILTRATIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: INFILTRATIVE

### IDEA-C-0346
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind INFILTRATIVE.
- Problem: Papers about INFILTRATIVE rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Infiltrative tumors violate instance assumptions; connected-component postprocess of SAM is harmful. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for INFILTRATIVE.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard INFILTRATIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: INFILTRATIVE

### IDEA-C-0347
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind INFILTRATIVE.
- Problem: Papers about INFILTRATIVE rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Infiltrative tumors violate instance assumptions; connected-component postprocess of SAM is harmful. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for INFILTRATIVE.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard INFILTRATIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: INFILTRATIVE

### IDEA-C-0348
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind INFILTRATIVE.
- Problem: Papers about INFILTRATIVE rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Infiltrative tumors violate instance assumptions; connected-component postprocess of SAM is harmful. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for INFILTRATIVE.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard INFILTRATIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: INFILTRATIVE

### IDEA-C-0349
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind INFILTRATIVE.
- Problem: Papers about INFILTRATIVE rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Infiltrative tumors violate instance assumptions; connected-component postprocess of SAM is harmful. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for INFILTRATIVE.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard INFILTRATIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: INFILTRATIVE

### IDEA-C-0350
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind INFILTRATIVE.
- Problem: Papers about INFILTRATIVE rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Infiltrative tumors violate instance assumptions; connected-component postprocess of SAM is harmful. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for INFILTRATIVE.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard INFILTRATIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: INFILTRATIVE

### IDEA-C-0351
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind INFILTRATIVE.
- Problem: Papers about INFILTRATIVE rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Infiltrative tumors violate instance assumptions; connected-component postprocess of SAM is harmful. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for INFILTRATIVE.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard INFILTRATIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: INFILTRATIVE

### IDEA-C-0352
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind INFILTRATIVE.
- Problem: Papers about INFILTRATIVE rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Infiltrative tumors violate instance assumptions; connected-component postprocess of SAM is harmful. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for INFILTRATIVE.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard INFILTRATIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: INFILTRATIVE

### IDEA-C-0353
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind POINT-THIN.
- Problem: Papers about POINT-THIN rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Single positive point on thin vessels is a Dirac mismatch; a short scribble is a different statistical estimator. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for POINT-THIN.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard POINT-THIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: POINT-THIN

### IDEA-C-0354
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind POINT-THIN.
- Problem: Papers about POINT-THIN rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Single positive point on thin vessels is a Dirac mismatch; a short scribble is a different statistical estimator. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for POINT-THIN.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard POINT-THIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: POINT-THIN

### IDEA-C-0355
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind POINT-THIN.
- Problem: Papers about POINT-THIN rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Single positive point on thin vessels is a Dirac mismatch; a short scribble is a different statistical estimator. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for POINT-THIN.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard POINT-THIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: POINT-THIN

### IDEA-C-0356
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind POINT-THIN.
- Problem: Papers about POINT-THIN rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Single positive point on thin vessels is a Dirac mismatch; a short scribble is a different statistical estimator. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for POINT-THIN.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard POINT-THIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: POINT-THIN

### IDEA-C-0357
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind POINT-THIN.
- Problem: Papers about POINT-THIN rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Single positive point on thin vessels is a Dirac mismatch; a short scribble is a different statistical estimator. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for POINT-THIN.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard POINT-THIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: POINT-THIN

### IDEA-C-0358
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind POINT-THIN.
- Problem: Papers about POINT-THIN rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Single positive point on thin vessels is a Dirac mismatch; a short scribble is a different statistical estimator. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for POINT-THIN.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard POINT-THIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: POINT-THIN

### IDEA-C-0359
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind POINT-THIN.
- Problem: Papers about POINT-THIN rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Single positive point on thin vessels is a Dirac mismatch; a short scribble is a different statistical estimator. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for POINT-THIN.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard POINT-THIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: POINT-THIN

### IDEA-C-0360
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind POINT-THIN.
- Problem: Papers about POINT-THIN rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Single positive point on thin vessels is a Dirac mismatch; a short scribble is a different statistical estimator. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for POINT-THIN.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard POINT-THIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: POINT-THIN

### IDEA-C-0361
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind BOX-SIZE.
- Problem: Papers about BOX-SIZE rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Box tightness is a hidden confounder: papers comparing prompts do not control box IoU-to-GT. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for BOX-SIZE.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard BOX-SIZE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BOX-SIZE

### IDEA-C-0362
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind BOX-SIZE.
- Problem: Papers about BOX-SIZE rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Box tightness is a hidden confounder: papers comparing prompts do not control box IoU-to-GT. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for BOX-SIZE.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard BOX-SIZE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BOX-SIZE

### IDEA-C-0363
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind BOX-SIZE.
- Problem: Papers about BOX-SIZE rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Box tightness is a hidden confounder: papers comparing prompts do not control box IoU-to-GT. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for BOX-SIZE.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard BOX-SIZE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BOX-SIZE

### IDEA-C-0364
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind BOX-SIZE.
- Problem: Papers about BOX-SIZE rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Box tightness is a hidden confounder: papers comparing prompts do not control box IoU-to-GT. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for BOX-SIZE.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard BOX-SIZE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BOX-SIZE

### IDEA-C-0365
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind BOX-SIZE.
- Problem: Papers about BOX-SIZE rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Box tightness is a hidden confounder: papers comparing prompts do not control box IoU-to-GT. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for BOX-SIZE.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard BOX-SIZE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BOX-SIZE

### IDEA-C-0366
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind BOX-SIZE.
- Problem: Papers about BOX-SIZE rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Box tightness is a hidden confounder: papers comparing prompts do not control box IoU-to-GT. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for BOX-SIZE.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard BOX-SIZE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BOX-SIZE

### IDEA-C-0367
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind BOX-SIZE.
- Problem: Papers about BOX-SIZE rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Box tightness is a hidden confounder: papers comparing prompts do not control box IoU-to-GT. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for BOX-SIZE.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard BOX-SIZE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BOX-SIZE

### IDEA-C-0368
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind BOX-SIZE.
- Problem: Papers about BOX-SIZE rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Box tightness is a hidden confounder: papers comparing prompts do not control box IoU-to-GT. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for BOX-SIZE.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard BOX-SIZE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: BOX-SIZE

### IDEA-C-0369
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind JPEG.
- Problem: Papers about JPEG rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Compression artifacts flip SAM masks more than Gaussian noise at equal PSNR. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for JPEG.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard JPEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: JPEG

### IDEA-C-0370
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind JPEG.
- Problem: Papers about JPEG rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Compression artifacts flip SAM masks more than Gaussian noise at equal PSNR. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for JPEG.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard JPEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: JPEG

### IDEA-C-0371
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind JPEG.
- Problem: Papers about JPEG rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Compression artifacts flip SAM masks more than Gaussian noise at equal PSNR. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for JPEG.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard JPEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: JPEG

### IDEA-C-0372
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind JPEG.
- Problem: Papers about JPEG rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Compression artifacts flip SAM masks more than Gaussian noise at equal PSNR. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for JPEG.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard JPEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: JPEG

### IDEA-C-0373
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind JPEG.
- Problem: Papers about JPEG rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Compression artifacts flip SAM masks more than Gaussian noise at equal PSNR. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for JPEG.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard JPEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: JPEG

### IDEA-C-0374
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind JPEG.
- Problem: Papers about JPEG rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Compression artifacts flip SAM masks more than Gaussian noise at equal PSNR. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for JPEG.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard JPEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: JPEG

### IDEA-C-0375
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind JPEG.
- Problem: Papers about JPEG rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Compression artifacts flip SAM masks more than Gaussian noise at equal PSNR. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for JPEG.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard JPEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: JPEG

### IDEA-C-0376
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind JPEG.
- Problem: Papers about JPEG rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Compression artifacts flip SAM masks more than Gaussian noise at equal PSNR. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for JPEG.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard JPEG intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: JPEG

### IDEA-C-0377
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind RESOLUTION-WIN.
- Problem: Papers about RESOLUTION-WIN rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If ViT window/patch size relative to lesion diameter predicts failure better than domain labels. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for RESOLUTION-WIN.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard RESOLUTION-WIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: RESOLUTION-WIN

### IDEA-C-0378
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind RESOLUTION-WIN.
- Problem: Papers about RESOLUTION-WIN rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If ViT window/patch size relative to lesion diameter predicts failure better than domain labels. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for RESOLUTION-WIN.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard RESOLUTION-WIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: RESOLUTION-WIN

### IDEA-C-0379
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind RESOLUTION-WIN.
- Problem: Papers about RESOLUTION-WIN rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If ViT window/patch size relative to lesion diameter predicts failure better than domain labels. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for RESOLUTION-WIN.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard RESOLUTION-WIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: RESOLUTION-WIN

### IDEA-C-0380
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind RESOLUTION-WIN.
- Problem: Papers about RESOLUTION-WIN rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If ViT window/patch size relative to lesion diameter predicts failure better than domain labels. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for RESOLUTION-WIN.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard RESOLUTION-WIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: RESOLUTION-WIN

### IDEA-C-0381
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind RESOLUTION-WIN.
- Problem: Papers about RESOLUTION-WIN rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If ViT window/patch size relative to lesion diameter predicts failure better than domain labels. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for RESOLUTION-WIN.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard RESOLUTION-WIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: RESOLUTION-WIN

### IDEA-C-0382
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind RESOLUTION-WIN.
- Problem: Papers about RESOLUTION-WIN rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If ViT window/patch size relative to lesion diameter predicts failure better than domain labels. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for RESOLUTION-WIN.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard RESOLUTION-WIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: RESOLUTION-WIN

### IDEA-C-0383
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind RESOLUTION-WIN.
- Problem: Papers about RESOLUTION-WIN rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If ViT window/patch size relative to lesion diameter predicts failure better than domain labels. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for RESOLUTION-WIN.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard RESOLUTION-WIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: RESOLUTION-WIN

### IDEA-C-0384
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind RESOLUTION-WIN.
- Problem: Papers about RESOLUTION-WIN rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If ViT window/patch size relative to lesion diameter predicts failure better than domain labels. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for RESOLUTION-WIN.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard RESOLUTION-WIN intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: RESOLUTION-WIN

### IDEA-C-0385
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind CROSS-MODAL-REPORT.
- Problem: Papers about CROSS-MODAL-REPORT rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Radiology report supervision improves classification of presence, not mask boundaries. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for CROSS-MODAL-REPORT.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard CROSS-MODAL-REPORT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CROSS-MODAL-REPORT

### IDEA-C-0386
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind CROSS-MODAL-REPORT.
- Problem: Papers about CROSS-MODAL-REPORT rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Radiology report supervision improves classification of presence, not mask boundaries. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for CROSS-MODAL-REPORT.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard CROSS-MODAL-REPORT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CROSS-MODAL-REPORT

### IDEA-C-0387
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind CROSS-MODAL-REPORT.
- Problem: Papers about CROSS-MODAL-REPORT rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Radiology report supervision improves classification of presence, not mask boundaries. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for CROSS-MODAL-REPORT.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard CROSS-MODAL-REPORT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CROSS-MODAL-REPORT

### IDEA-C-0388
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind CROSS-MODAL-REPORT.
- Problem: Papers about CROSS-MODAL-REPORT rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Radiology report supervision improves classification of presence, not mask boundaries. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for CROSS-MODAL-REPORT.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard CROSS-MODAL-REPORT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CROSS-MODAL-REPORT

### IDEA-C-0389
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind CROSS-MODAL-REPORT.
- Problem: Papers about CROSS-MODAL-REPORT rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Radiology report supervision improves classification of presence, not mask boundaries. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for CROSS-MODAL-REPORT.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard CROSS-MODAL-REPORT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CROSS-MODAL-REPORT

### IDEA-C-0390
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind CROSS-MODAL-REPORT.
- Problem: Papers about CROSS-MODAL-REPORT rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Radiology report supervision improves classification of presence, not mask boundaries. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for CROSS-MODAL-REPORT.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard CROSS-MODAL-REPORT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CROSS-MODAL-REPORT

### IDEA-C-0391
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind CROSS-MODAL-REPORT.
- Problem: Papers about CROSS-MODAL-REPORT rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Radiology report supervision improves classification of presence, not mask boundaries. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for CROSS-MODAL-REPORT.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard CROSS-MODAL-REPORT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CROSS-MODAL-REPORT

### IDEA-C-0392
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind CROSS-MODAL-REPORT.
- Problem: Papers about CROSS-MODAL-REPORT rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Radiology report supervision improves classification of presence, not mask boundaries. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for CROSS-MODAL-REPORT.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard CROSS-MODAL-REPORT intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: CROSS-MODAL-REPORT

### IDEA-C-0393
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind REPLAY.
- Problem: Papers about REPLAY rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Tiny replay of synthetic click-segmentation preserves SAM promptability during medical PEFT. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for REPLAY.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard REPLAY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REPLAY

### IDEA-C-0394
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind REPLAY.
- Problem: Papers about REPLAY rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Tiny replay of synthetic click-segmentation preserves SAM promptability during medical PEFT. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for REPLAY.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard REPLAY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REPLAY

### IDEA-C-0395
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind REPLAY.
- Problem: Papers about REPLAY rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Tiny replay of synthetic click-segmentation preserves SAM promptability during medical PEFT. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for REPLAY.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard REPLAY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REPLAY

### IDEA-C-0396
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind REPLAY.
- Problem: Papers about REPLAY rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Tiny replay of synthetic click-segmentation preserves SAM promptability during medical PEFT. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for REPLAY.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard REPLAY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REPLAY

### IDEA-C-0397
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind REPLAY.
- Problem: Papers about REPLAY rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Tiny replay of synthetic click-segmentation preserves SAM promptability during medical PEFT. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for REPLAY.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard REPLAY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REPLAY

### IDEA-C-0398
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind REPLAY.
- Problem: Papers about REPLAY rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Tiny replay of synthetic click-segmentation preserves SAM promptability during medical PEFT. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for REPLAY.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard REPLAY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REPLAY

### IDEA-C-0399
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind REPLAY.
- Problem: Papers about REPLAY rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Tiny replay of synthetic click-segmentation preserves SAM promptability during medical PEFT. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for REPLAY.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard REPLAY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REPLAY

### IDEA-C-0400
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind REPLAY.
- Problem: Papers about REPLAY rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Tiny replay of synthetic click-segmentation preserves SAM promptability during medical PEFT. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for REPLAY.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard REPLAY intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: REPLAY

### IDEA-C-0401
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind SELECTIVE.
- Problem: Papers about SELECTIVE rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If A reject option on SAM IoU tokens raises effective Dice more than any adapter of equal compute. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for SELECTIVE.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard SELECTIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELECTIVE

### IDEA-C-0402
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind SELECTIVE.
- Problem: Papers about SELECTIVE rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If A reject option on SAM IoU tokens raises effective Dice more than any adapter of equal compute. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for SELECTIVE.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard SELECTIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELECTIVE

### IDEA-C-0403
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind SELECTIVE.
- Problem: Papers about SELECTIVE rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If A reject option on SAM IoU tokens raises effective Dice more than any adapter of equal compute. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for SELECTIVE.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard SELECTIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELECTIVE

### IDEA-C-0404
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind SELECTIVE.
- Problem: Papers about SELECTIVE rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If A reject option on SAM IoU tokens raises effective Dice more than any adapter of equal compute. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for SELECTIVE.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard SELECTIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELECTIVE

### IDEA-C-0405
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind SELECTIVE.
- Problem: Papers about SELECTIVE rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If A reject option on SAM IoU tokens raises effective Dice more than any adapter of equal compute. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for SELECTIVE.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard SELECTIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELECTIVE

### IDEA-C-0406
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind SELECTIVE.
- Problem: Papers about SELECTIVE rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If A reject option on SAM IoU tokens raises effective Dice more than any adapter of equal compute. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for SELECTIVE.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard SELECTIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELECTIVE

### IDEA-C-0407
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind SELECTIVE.
- Problem: Papers about SELECTIVE rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If A reject option on SAM IoU tokens raises effective Dice more than any adapter of equal compute. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for SELECTIVE.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard SELECTIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELECTIVE

### IDEA-C-0408
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind SELECTIVE.
- Problem: Papers about SELECTIVE rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If A reject option on SAM IoU tokens raises effective Dice more than any adapter of equal compute. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for SELECTIVE.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard SELECTIVE intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: SELECTIVE

### IDEA-C-0409
- Idea: Training/eval dynamics 'annotation-minutes-matched' as the real cause behind HUMAN-LOOP.
- Problem: Papers about HUMAN-LOOP rarely report annotation-minutes-matched, so mechanisms are unidentified.
- Hypothesis: If Human correction of SAM on smoke is slower than from-scratch brush because of jagged false boundaries. then controlling annotation-minutes-matched will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat annotation-minutes-matched as an independent variable for HUMAN-LOOP.
- MinExp: Ablate annotation-minutes-matched in a 2x2 with vs without the standard HUMAN-LOOP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HUMAN-LOOP

### IDEA-C-0410
- Idea: Training/eval dynamics 'scanner-held-out' as the real cause behind HUMAN-LOOP.
- Problem: Papers about HUMAN-LOOP rarely report scanner-held-out, so mechanisms are unidentified.
- Hypothesis: If Human correction of SAM on smoke is slower than from-scratch brush because of jagged false boundaries. then controlling scanner-held-out will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat scanner-held-out as an independent variable for HUMAN-LOOP.
- MinExp: Ablate scanner-held-out in a 2x2 with vs without the standard HUMAN-LOOP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HUMAN-LOOP

### IDEA-C-0411
- Idea: Training/eval dynamics 'seed-sensitivity' as the real cause behind HUMAN-LOOP.
- Problem: Papers about HUMAN-LOOP rarely report seed-sensitivity, so mechanisms are unidentified.
- Hypothesis: If Human correction of SAM on smoke is slower than from-scratch brush because of jagged false boundaries. then controlling seed-sensitivity will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat seed-sensitivity as an independent variable for HUMAN-LOOP.
- MinExp: Ablate seed-sensitivity in a 2x2 with vs without the standard HUMAN-LOOP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HUMAN-LOOP

### IDEA-C-0412
- Idea: Training/eval dynamics 'class-size-quartile' as the real cause behind HUMAN-LOOP.
- Problem: Papers about HUMAN-LOOP rarely report class-size-quartile, so mechanisms are unidentified.
- Hypothesis: If Human correction of SAM on smoke is slower than from-scratch brush because of jagged false boundaries. then controlling class-size-quartile will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat class-size-quartile as an independent variable for HUMAN-LOOP.
- MinExp: Ablate class-size-quartile in a 2x2 with vs without the standard HUMAN-LOOP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HUMAN-LOOP

### IDEA-C-0413
- Idea: Training/eval dynamics 'boundary-NSD' as the real cause behind HUMAN-LOOP.
- Problem: Papers about HUMAN-LOOP rarely report boundary-NSD, so mechanisms are unidentified.
- Hypothesis: If Human correction of SAM on smoke is slower than from-scratch brush because of jagged false boundaries. then controlling boundary-NSD will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat boundary-NSD as an independent variable for HUMAN-LOOP.
- MinExp: Ablate boundary-NSD in a 2x2 with vs without the standard HUMAN-LOOP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HUMAN-LOOP

### IDEA-C-0414
- Idea: Training/eval dynamics 'calibration-ECE' as the real cause behind HUMAN-LOOP.
- Problem: Papers about HUMAN-LOOP rarely report calibration-ECE, so mechanisms are unidentified.
- Hypothesis: If Human correction of SAM on smoke is slower than from-scratch brush because of jagged false boundaries. then controlling calibration-ECE will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat calibration-ECE as an independent variable for HUMAN-LOOP.
- MinExp: Ablate calibration-ECE in a 2x2 with vs without the standard HUMAN-LOOP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HUMAN-LOOP

### IDEA-C-0415
- Idea: Training/eval dynamics 'forgetting-on-SA1B-proxy' as the real cause behind HUMAN-LOOP.
- Problem: Papers about HUMAN-LOOP rarely report forgetting-on-SA1B-proxy, so mechanisms are unidentified.
- Hypothesis: If Human correction of SAM on smoke is slower than from-scratch brush because of jagged false boundaries. then controlling forgetting-on-SA1B-proxy will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat forgetting-on-SA1B-proxy as an independent variable for HUMAN-LOOP.
- MinExp: Ablate forgetting-on-SA1B-proxy in a 2x2 with vs without the standard HUMAN-LOOP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HUMAN-LOOP

### IDEA-C-0416
- Idea: Training/eval dynamics 'prompt-jitter' as the real cause behind HUMAN-LOOP.
- Problem: Papers about HUMAN-LOOP rarely report prompt-jitter, so mechanisms are unidentified.
- Hypothesis: If Human correction of SAM on smoke is slower than from-scratch brush because of jagged false boundaries. then controlling prompt-jitter will shrink or reverse the claimed effect.
- Important: Stops false novelty from uncontrolled training dynamics.
- Novel: Treat prompt-jitter as an independent variable for HUMAN-LOOP.
- MinExp: Ablate prompt-jitter in a 2x2 with vs without the standard HUMAN-LOOP intervention.
- Risk: Negative results are harder to publish; pre-register the kill criterion.
- Cluster: HUMAN-LOOP

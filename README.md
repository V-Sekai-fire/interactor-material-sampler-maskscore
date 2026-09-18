# Material Sampler MaskScore

Turns garment reference photographs into tiling materials through the image-to-material tool, then exports them for MaskScore scoring.

## Purpose
The second-hand fashion corpus is photographs, and the material tools downstream want
materials. This plugin drives the image-to-material tool's Python API so a photograph
becomes an exported material without a recorded click sequence.

## Workflow
1. Sample garments from the HuggingFace dataset.
2. Create a material asset and import the photograph as its source image.
3. Wait for the layer stack to compute.
4. Export the material and score it with EditScore/MaskScore.

## Install
Copy this directory into the user plugin directory
(`~/Documents/Adobe/Adobe Substance 3D Sampler/python/plugins/`) and restart the
application. `MASKSCORE_IMAGE` naming a photograph runs a batch on load; with the
variable unset the plugin stays idle.

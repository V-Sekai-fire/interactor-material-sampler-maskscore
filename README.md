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
Copy `MaterialSamplerMaskScore/` into the user plugin directory
(`~/Documents/Allegorithmic/Adobe Substance 3D Sampler/plugins/`) and restart the
application. The loader expects the folder and its `.py`, `.qml` and `.svg` to share
one name. `MASKSCORE_IMAGE` naming a photograph runs a batch on load; with the
variable unset the plugin registers its panel and stays idle.

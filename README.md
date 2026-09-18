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
one name. `maskscore.json` beside the module names the photograph and the export directory.

## The batch does not run at load
The plugin registers its panel and stops there. At plugin-load time the workflow
assets are not loaded, so `create_project` fails with `Could not create workflow
asset PBR Metallic / Roughness` and `create_asset` returns `None`. Run the batch
from the panel button once the application is up.

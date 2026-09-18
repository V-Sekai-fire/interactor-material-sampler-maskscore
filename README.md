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

## What the API actually wants
Measured against the shipped build, because the documentation gives no signatures:

- `import_images(images, position, import_option, ...)` — the position and the
  option are required, not optional.
- `export_material(path, ...) -> str` is synchronous and returns the path. It takes
  an `ExportController` as a keyword, so the returned value is a string and has no
  callbacks on it.
- Neither `wait_for_computation()` nor `ExportController.wait()` belongs in the
  panel's slot: both stall the thread the work runs on, so the export is never
  reached.

`ImageImportOption` offers `image_to_material_B2M` and `image_to_material_AI_powered`.
The default here is B2M. The AI-powered path samples from a generative model, which
would make every material generated synthetic and carry the provenance obligations
that go with it; B2M is algorithmic, so the same photograph gives the same material.

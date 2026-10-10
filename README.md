# interactor-material-sampler-maskscore

A plugin for an image-to-material application that turns garment photographs into tiling materials and exports them for MaskScore scoring.

## What it is for

The second-hand fashion corpus is photographs, and the material tools downstream want materials. The plugin drives the application's Python API: it imports a photograph into a new material, lets the layer stack compute, and exports the result. It uses the algorithmic conversion rather than the generative one, so the same photograph gives the same material. `dataset_sampler.py` picks garments from the corpus.

## Install and run

Copy `MaterialSamplerMaskScore/` into the application's user plugin directory and restart the application. A `maskscore.json` beside the module names the photograph and the export directory, and the batch runs from the plugin panel's button.

## Licence

MIT. See [LICENSE](LICENSE).

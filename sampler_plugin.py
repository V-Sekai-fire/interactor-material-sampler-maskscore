import os

import substance_sampler

IMAGE_ENV = "MASKSCORE_IMAGE"
EXPORT_ENV = "MASKSCORE_EXPORT_DIR"
DEFAULT_EXPORT_DIR = os.path.join(os.path.expanduser("~"), "maskscore", "materials")


def material_from_image(image_path, name=None):
    """Create a material asset whose source image is one garment photograph."""
    name = name or os.path.splitext(os.path.basename(image_path))[0]
    asset = substance_sampler.create_asset(name, substance_sampler.AssetType.material, True)
    asset.import_images([image_path])
    substance_sampler.wait_for_computation()
    return asset


def export_material(asset, export_dir=None):
    export_dir = export_dir or os.environ.get(EXPORT_ENV, DEFAULT_EXPORT_DIR)
    os.makedirs(export_dir, exist_ok=True)
    controller = asset.export_material(export_dir)
    controller.wait()
    return export_dir


def run_batch(image_path, project_path=None, export_dir=None):
    project_path = project_path or os.path.join(
        os.path.expanduser("~"), "maskscore", "sampler", "maskscore.ssa"
    )
    os.makedirs(os.path.dirname(project_path), exist_ok=True)
    substance_sampler.create_project("maskscore", project_path)
    asset = material_from_image(image_path)
    written = export_material(asset, export_dir)
    substance_sampler.save_project()
    return written


def _start():
    image = os.environ.get(IMAGE_ENV)
    if not image:
        print("material-sampler-maskscore idle: set %s to run a batch" % IMAGE_ENV)
        return
    print("material-sampler-maskscore wrote %s" % run_batch(image))


substance_sampler.run_in_main_thread(_start)

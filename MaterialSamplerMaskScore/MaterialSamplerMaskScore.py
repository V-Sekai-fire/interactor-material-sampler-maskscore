import json
import os

from PySide6 import QtCore, QtQml, QtQuick

import substance_sampler

BATCH_CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "maskscore.json")
DEFAULT_EXPORT_DIR = os.path.join(os.path.expanduser("~"), "maskscore", "materials")


def batch_config(path=BATCH_CONFIG):
    """Read the batch to run. Absent file means idle, which is how the tool opens by hand."""
    if not os.path.exists(path):
        return {}
    with open(path) as handle:
        return json.load(handle)


def material_from_image(image_path, name=None):
    """Create a material asset whose source image is one garment photograph."""
    name = name or os.path.splitext(os.path.basename(image_path))[0]
    asset = substance_sampler.create_asset(name, substance_sampler.AssetType.material, True)
    asset.import_images([image_path])
    substance_sampler.wait_for_computation()
    return asset


def export_material(asset, export_dir=None):
    export_dir = export_dir or DEFAULT_EXPORT_DIR
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


class MaterialSamplerMaskScore(QtQuick.QQuickItem):
    def __init__(self, parent=None):
        super(MaterialSamplerMaskScore, self).__init__(parent)

    @QtCore.Slot(str)
    def build_material(self, image_path):
        config = batch_config()
        written = run_batch(
            image_path or config.get("image"),
            config.get("project_path"),
            config.get("export_dir"),
        )
        print("material-sampler-maskscore wrote %s" % written)


def _start():
    QtQml.qmlRegisterType(
        MaterialSamplerMaskScore, "MaterialSamplerMaskScore", 1, 0,
        "MaterialSamplerMaskScore",
    )
    # The batch does not run here: at plugin-load time the workflow assets are
    # not loaded yet, so create_project fails and create_asset returns None.
    print("material-sampler-maskscore ready: run the batch from the panel")


substance_sampler.run_in_main_thread(_start)

"""
Tests for config.py
"""
from os.path import dirname
from models import config
from controllers import main_controller


def test_configeration():
    """Configeration function can run"""
    model = main_model.MainModel()

    controller = main_controller.MainController(model)
    controller.change_selected_directory("dicom_file")

    configuration = config.Config(controller)
    parent_directory = dirname(__file__).split("\\src")[0]
    configuration.update_default_dir(f"{parent_directory}")

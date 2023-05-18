"""
Tests for config.py
"""
from os.path import dirname
from src.models import main_model
from src.models import config
from src.controllers import main_controller


def test_config():
    """Configeration function can run"""
    model = main_model.MainModel()

    controller = main_controller.MainController(model)
    controller.change_selected_directory("dicom_file")

    configuration = config.Config(controller)

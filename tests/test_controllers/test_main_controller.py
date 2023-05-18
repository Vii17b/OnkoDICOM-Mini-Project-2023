"""
Tests for main_controller.py
"""

from models import main_model


def test_main_controller(qtbot):
    model = main_model.MainModel()

    controller = main_controller.MainController(model)

    controller.change_selected_directory("dicom_file")

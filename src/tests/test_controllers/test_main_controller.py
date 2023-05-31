"""
Tests for main_controller.py
"""


from src.models.main_model import MainModel
from src.controllers.main_controller import MainController


def test_main_controller(qtbot):
    model_test = MainModel()

    controller_test = MainController(model_test)
    controller_test._main_model
    controller_test._config
    controller_test._dicom_parser
    controller_test.go_to_next_image()
    controller_test.go_to_preivous_image()
    controller_test.open_image_viewer()
    controller_test._image_popup.close()

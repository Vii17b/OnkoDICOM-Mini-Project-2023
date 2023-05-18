"""
Tests for main_controller.py
"""

from models.dicom import DicomParser
from models.config import Config

from views.image_popup import ImageView
from views.directory_popup import DirectoryView


def test_main_controller(qtbot):
    model = main_model.MainModel()

    controller = main_controller.MainController(model)

    controller.change_selected_directory("dicom_file")

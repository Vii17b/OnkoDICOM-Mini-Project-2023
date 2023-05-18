"""
Tests for directory_popup.py
"""

from models.main_model import MainModel
from controllers.main_controller import MainController
from views.directory_popup import DirectoryView


def test_directory_popup():
    model_test = MainModel()
    controller_test = MainController(model_test)

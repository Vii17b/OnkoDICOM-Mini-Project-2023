"""
Tests for directory_popup.py
"""

from src.models.main_model import MainModel
from src.controllers.main_controller import MainController
from src.views.directory_popup import DirectoryView


def test_directory_popup():
    model_test = MainModel()
    controller_test = MainController(model_test)

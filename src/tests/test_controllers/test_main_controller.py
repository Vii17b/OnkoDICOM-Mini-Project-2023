"""
Tests for main_controller.py
"""

from models.main_model import MainModel
from controllers.main_controller import MainController


def test_main_controller(qtbot):
    model_test = MainModel()

    controller_test = MainController(model_test)

"""
Tests for main_controller.py
"""

from models import main_model
from controllers import main_controller


def test_main_controller(qtbot):
    model_test = main_model.MainModel()

    controller_test = main_controller.MainController(model_test)

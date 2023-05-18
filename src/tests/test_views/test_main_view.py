"""
Tests for main_view.py
"""

from models import main_model
from controllers import main_controller
from views.main_view import MainView


def test_main_view(qtbot):
    model_test = main_model.MainModel()
    controller_test = main_controller.MainController(model)

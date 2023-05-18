"""
Tests for main_view.py
"""

from models.main_model import MainModel
from controllers.main_controller import MainController
from views.main_view import MainView


def test_main_view(qtbot):
    model_test = MainModel()
    controller_test = MainController(model)

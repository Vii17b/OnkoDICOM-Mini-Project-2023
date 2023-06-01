"""
Tests for main_view.py
"""

from src.models.main_model import MainModel
from src.controllers.main_controller import MainController
from src.views.main_view import MainView


def test_main_view_no_parser(qtbot):
    model_test = MainModel()
    controller_test = MainController(model_test)

    view_test = MainView(controller_test)

    assert view_test.selection() is False

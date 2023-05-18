"""
Tests for main_view.py
"""

from src.models import main_model
from src.controllers import main_controller
from src.views.main_view import MainView


def test_main_view(qtbot):
    model = main_model.MainModel()

    controller = main_controller.MainController(model)

    main_view = MainView(controller)

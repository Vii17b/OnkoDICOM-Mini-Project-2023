"""
Tests for main_view.py
"""

from models import main_model
from controllers import main_controller
from views.main_view import MainView


def test_main_view(qtbot):
    model = main_model.MainModel()
    controller = main_controller.MainController(model)
    main_view = MainView(controller)

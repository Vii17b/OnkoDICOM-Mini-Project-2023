"""
Tests for image_popup.py
"""

from src.models import main_model
from src.controllers import main_controller
from src.views.image_popup import ImageView


def test_image(qtbot):
    model_test = main_model.MainModel()
    controller_test = main_controller.MainController(model_test)
    main_view_test = MainView(controller_test)

"""
Tests for image_popup.py
"""

from src.models import main_model
from src.controllers import main_controller
from src.views.image_popup import ImageView


def test_image(qtbot):
    model = main_model.MainModel()
    controller = main_controller.MainController(model)

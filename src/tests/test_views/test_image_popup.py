"""
Tests for image_popup.py
"""

from src.models.main_model import MainModel
from src.controllers.main_controller import MainController
from src.views.image_popup import ImageView


def test_image_popup():
    model_test = MainModel()
    controller_test = MainController(model_test)

    image_view_test = ImageView(controller_test)

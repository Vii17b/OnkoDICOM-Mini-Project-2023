"""
Tests for image_popup.py
"""

from models.main_model import MainModel
from controllers.main_controller import MainController
from views.image_popup import ImageView


def test_image_popup():
    model_test = MainModel()
    controller_test = MainController(model_test)

    image_view_test = ImageView(controller_test)

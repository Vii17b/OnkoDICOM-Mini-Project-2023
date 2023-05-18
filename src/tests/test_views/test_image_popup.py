"""
Tests for image_popup.py
"""

from models import main_model
from controllers import main_controller
from views.image_popup import ImageView


def test_image_popup(qtbot):
    model_test = main_model.MainModel()
    controller_test = main_controller.MainController(model_test)

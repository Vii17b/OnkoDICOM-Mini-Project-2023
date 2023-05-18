"""
Tests for image_popup.py
"""

from models import main_model
from controllers import main_controller
from views.image_popup import ImageView


def test_image(qtbot):
    model = main_model.MainModel()
    controller = main_controller.MainController(model)

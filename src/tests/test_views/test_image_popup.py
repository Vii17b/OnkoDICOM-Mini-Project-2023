"""
Tests for image_popup.py
"""

from models import main_model
from controllers import main_controller
from views.image_popup import ImageView


def test_image(qtbot):
    model_test = main_model.MainModel()
    controller_test = main_controller.MainController(model_test)
    main_view_test = MainView(controller_test)

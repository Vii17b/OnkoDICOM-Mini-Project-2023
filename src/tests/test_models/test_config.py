"""
Tests for config.py
"""
from os.path import dirname
from models import main_model
from models import config
from controllers import main_controller


def test_config():
    """Configeration function can run"""
    model_test = main_model.MainModel()
    controller_test = main_controller.MainController(model_test)

    configuration = config.Config(controller_test)

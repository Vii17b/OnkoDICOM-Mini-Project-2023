"""
Tests for config.py
"""

from models.main_model import MainModel
from models.config import Config

from controllers.main_controller import MainController


def test_config():
    model_test = MainModel()
    controller_test = MainController(model_test)

    config_test = Config(controller_test)

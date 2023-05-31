"""
Tests for config.py
"""

from src.models.main_model import MainModel
from src.models.config import Config

from src.controllers.main_controller import MainController
import os


def test_config():
    # tests without an existing config file
    os.remove("/home/osboxes/.OnkoDICOM/OnkoDICOM.db")

    model_test = MainModel()
    controller_test = MainController(model_test)

    config_test = Config(controller_test)

    del model_test
    del controller_test
    del config_test

    # tests with an existing config file
    model_test = MainModel()
    controller_test = MainController(model_test)

    config_test = Config(controller_test)

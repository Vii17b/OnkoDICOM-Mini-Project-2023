"""
Tests for config.py
"""

import pytest

from src.models.main_model import MainModel
from src.models.config import Config

from src.controllers.main_controller import MainController
import os


def test_config_no_file():
    # tests without an existing config file
    os.remove("/home/osboxes/.OnkoDICOM/OnkoDICOM.db")

    model_test = MainModel()
    controller_test = MainController(model_test)


def test_config_file_exists(qtbot):
    # tests with an existing config file
    model_test = MainModel()
    controller_test = MainController(model_test)

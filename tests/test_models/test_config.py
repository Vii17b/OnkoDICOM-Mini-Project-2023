"""
Tests for config.py
"""
from os.path import dirname
from models import config
from controllers import main_controller


def test_configeration():
    """Configeration function can run"""
    configuration = config.Config()
    parent_directory = dirname(__file__).split("\\src")[0]
    configuration.update_default_dir(f"{parent_directory}")

""" Tests for config.py """

from os.path import dirname
from models.config import config


def test_config():
    configuration = config.Config()
    parent_directory = dirname(__file__).split("\\src")[0]
    configuration.update_default_dir(f"{parent_directory}")

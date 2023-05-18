"""
Tests for main.py
"""

import pytest

import sys
from PySide6.QtWidgets import QApplication

from main import App


@pytest.fixture
def app_test():
    app_test = App(sys.argv)
    return app_test


def test_startup(app_test):
    pass

"""
Tests for main.py
"""

import pytest

import sys
from PySide6.QtWidgets import QApplication

from main import App


@pytest.fixture
def app_test():
    app_test = App()
    return app_test


def test_startup(app_test):
    assert app_test.windowTitle() == "OnkoDICOM 2023 Mini Project"
    assert app_test.plot_w

"""
Tests for main.py
"""

import pytest
from PySide6.QtWidgets import QApplication

from main import App


@pytest.fixture
def app_test(QApplication):
    app_test = App()
    qtbot.addWidget(app_test)
    return app_test


def test_startup(app_test):
    assert app_test.windowTitle() == "OnkoDICOM 2023 Mini Project"
    assert app_test.plot_w

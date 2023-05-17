"""
Tests for main.py
"""
import pytest
from main import App


@pytest.fixture
def test_app(qtbot):
    """
    Sets up application for testing
    """
    test_app = App()
    qtbot.addWidget(test_app)
    return test_app


def test_startup(test_app):
    """Tests window startup, ensuring it runs"""
    assert test_app.windowTitle() == "OnkoDICOM 2022 Mini Project"
    assert test_app.plot_w

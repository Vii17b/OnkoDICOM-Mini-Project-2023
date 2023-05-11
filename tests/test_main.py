"""
Tests for main.py
"""
import pytest
from main import App


@pytest.fixture
def test_app(qtbot):
    test_app = App()
    qtbot.addWidget(test_app)
    return test_app


def test_startup(test_app):
    assert test_app.windowTitle() == "OnkoDICOM 2023 Mini Project"
    assert test_app.plot_w

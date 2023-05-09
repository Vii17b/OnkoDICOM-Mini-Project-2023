"""
Tests for main.py
"""
import pytest


@pytest.fixture
def test_app(qtbot):
    test_app
    qtbot.addWidget(test_app)
    return test_app


def test_startup(test_app):
    assert test_app.windowTitle() == "OnkoDICOM 2023 Mini Project"
    assert test_app.plot_w

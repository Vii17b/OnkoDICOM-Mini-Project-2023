"""
Tests for main.py
"""

import pytest
from main import App, sys


@pytest.fixture(scope="session")
def test_app():
    return App


def test_startup(test_app):
    #assert test_app.windowTitle() == "OnkoDICOM 2023 Mini Project"
    #assert test_app.plot_w
    pass

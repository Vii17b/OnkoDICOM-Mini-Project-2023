"""
Tests for main_model.py
"""

from src.models.main_model import MainModel


def test_main_model():
    model_test = MainModel()
    assert model_test.image_index == 0

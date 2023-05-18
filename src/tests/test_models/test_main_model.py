"""
Tests for main_model.py
"""

from src.models import main_model


def test_main_model():
    model = main_model.MainModel()

    model.selected_dicom_directory = "new_dicom_directory"
    model.selected_image_file_path = "new_image_file_path"

    assert model.selected_dicom_directory == "new_dicom_directory"
    assert model.selected_image_file_path == "new_image_file_path"

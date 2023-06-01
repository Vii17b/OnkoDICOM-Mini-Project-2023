"""
Tests for image_popup.py
"""

from src.models.main_model import MainModel
from src.models.dicom import DicomParser
from src.controllers.main_controller import MainController
from src.views.image_popup import ImageView


def test_image_popup():
    model_test = MainModel()
    controller_test = MainController(model_test)
    file_dir = '/home/osboxes/mini_project/DICOM Files/DICOM-RT-01'
    parser_test = DicomParser(file_dir)

    image_view_test = ImageView(controller_test)
    test_img = parser_test.get_image(0)
    image_view_test.update(test_img, "Test Title")

    assert image_view_test.image_title.text() == "Test Title"

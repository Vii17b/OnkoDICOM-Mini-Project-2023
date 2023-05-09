"""
Shows the image from the controller
Has a slider to slide through the images
"""

from PySide6.QtWidgets import QWidget


class Popup(QWidget):
    """
    A popup view that displays the DICOM image
    If the slider is changed ore the left/right buttons are pressed
    the label should update to show (Image X/Y) and the image should update
    """
    def __init__(self, main_controller, parent=None) -> None:
        super().__init__(parent)
        self._main_controller = main_controller

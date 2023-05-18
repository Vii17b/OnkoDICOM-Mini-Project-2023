"""
The model stores state information,
in this case, dicom directory and open image index
Contains getters and setters for state information
"""

from PySide6.QtCore import QObject


class MainModel(QObject):
    """
    This model inherits from QObject so it can use signals
    to communicate with the views
    """

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.dicom_directory = None
        self.image_index = 0

"""
The UI for navigating to the image selector and directory selector
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QWidget,
    QFileDialog,
)
from PySide6.QtCore import QSize, QDir


class MainView(QMainWindow):
    """The UI for navigating to the image selector and directory selector"""

    def __init__(self, controller):
        """Creates the widgets and layout"""

        super().__init__()
        self.controller = controller

        self.resize(1000, 700)
        self.setWindowTitle("Mini Project")

        # Create widgets
        self.info = QLabel()
        self.info.setText("Options: ")
        self.info.setMinimumSize(QSize(200, 20))
        self.nav_directory = QPushButton("&Browse Files")
        self.nav_directory.clicked.connect(self.selection)
        self.nav_directory.setMinimumSize(QSize(200, 20))
        self.nav_image = QPushButton("&View File")
        self.nav_image.clicked.connect(self.controller.open_image_viewer)
        self.nav_image.setMinimumSize(QSize(200, 20))

        # Create layout
        self.layout_widget = QWidget(self)
        self.layout_widget.setMinimumSize(QSize(640, 60))
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.info)
        self.layout.addWidget(self.nav_directory)
        self.layout.addWidget(self.nav_image)
        self.layout_widget.setLayout(self.layout)

    def selection(self):
        """
        Opens the directory selection, returns the directory
        """

        if self.controller.dicom_parser == None:
            # This realistically shouldn't happen
            # However, pytest.
            return False
        directory = QFileDialog.getExistingDirectory(
            self, "Select Directory", QDir.currentPath()
        )
        self.controller.change_selected_directory(directory)
        return True

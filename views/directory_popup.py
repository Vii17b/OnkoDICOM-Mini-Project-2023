"""First time popup if the Config cannot find the hidden file
Updates the Config accordingly"""

from PySide6.QtWidgets import (
    QDialog, QFileDialog, QLabel, QPushButton, QHBoxLayout)
from PyQt6.QtCore import QDir


class DirectoryView(QDialog):
    """Popup view that prompts the user to supply a default directory"""

    def __init__(self, controller):

        """Creates the window for openening directory selection"""

        super().__init__()
        self.resize(400, 300)
        self.controller = controller

        self.setWindowTitle("Directory Selection")

        # Create widgets
        self.directory_info = QLabel()
        self.directory_info.setText("Select the default directory for DICOM:")
        self.select_directory = QPushButton("&Open")
        self.select_directory.clicked.connect(self.selection)

        # Create layout
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.directory_info)
        self.layout.addWidget(self.select_directory)
        self.setLayout(self.layout)

    def selection(self):

        """Opens the directory selection, returns the directory"""

        directory = QFileDialog.getExistingDirectory(
            self, "Select Directory", QDir.currentPath())
        self.controller.change_selected_directory(directory)

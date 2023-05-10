"""
The UI for navigating to the image selector and directory selector
"""

from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QHBoxLayout


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
        self.nav_directory = QPushButton("&Browse Files")
        self.nav_directory.clicked.connect(
            self.controller.default_directory_prompt)
        self.nav_image = QPushButton("&View File")
        self.nav_image.clicked.connect(self.controller.open_image_viewer)

        # Create layout
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.info)
        self.layout.addWidget(self.nav_directory)
        self.layout.addWidget(self.nav_image)
        self.setLayout(self.layout)

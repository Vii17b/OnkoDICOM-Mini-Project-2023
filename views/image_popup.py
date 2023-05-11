"""Shows the image from the controller
Has a slider to slide through the images"""

from PySide6.QtWidgets import QWidget, QLabel, QSlider, QGridLayout
from PySide6 import QtCore


class ImageView(QWidget):
    """Class for the image popup"""

    def __init__(self, controller):

        """ Creates the structure for the image window"""

        super().__init__()

        self.setWindowTitle("Image Display")

        # Create widgets
        self.image_title = QLabel()
        self.image = QLabel()
        self.slider = QSlider(self, QtCore.Qt.Horizontal)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.sliderMoved.connect(
            lambda: controller.update_image(self.slider.value()))

        # Create layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.image_title, 0, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.image, 1, 0, QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.slider, 2, 0, QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)

    def update(self, img, title):

        """ Updates the image window"""

        self.image.setPixmap(img)
        self.image_title.setText(title)

"""
Parses the dicom file to be read
Provides easy access to DICOM images
"""

import os
from pydicom import dcmread
from PIL import Image, ImageQt
from PySide6.QtGui import QPixmap


class DicomParser:
    """
    The model class for handling interactions with DICOM files
    """

    def __init__(self, file_dir) -> None:
        self.read_directory(file_dir)

    def read_directory(self, file_dir):
        """
        Attempts to parse the given directory as a DICOM file
        """
        self.files = list(
            dcmread(file_dir + "/" + f) for f in self.get_dcm_from_file(file_dir)
        )
        self.num_images = len(self.files)
        if self.num_images == 0:
            # Well that certainly isn't a dicom file then
            print("The supplied directory is not a dicom file.")
            return False

        # Search for supplied tags
        # This doesn't have an actual purpose, so we just sample the first
        # image for demonstation purposes
        tags_list = ["StudyInstanceUID", "fakeTestTag"]
        for tag in tags_list:
            try:
                print(self.files[0][tag])
            except KeyError:
                print(f"Tag {tag} not found in Dicom File.")
        return True

    def get_dcm_from_file(self, file_dir):
        """
        Returns a dict of all the image files in the directory
        This method assumes all files are named "*_#_*.dcm"
        """
        files_in_dir = os.listdir(file_dir)
        indexed_files = {}
        for file in files_in_dir:
            if file.endswith(".dcm"):
                try:
                    index = int(file.split("_")[1])
                    indexed_files[index] = file
                except ValueError:
                    # A valueError means the file doesn't match the
                    # "*_#_*.dcm" format and isn't an image
                    pass

        # Sorts the files, then returns them in an ordered list
        # This is so whatever the first file number is, it will have index 0
        # And the next will be 1, and so on
        # This prevents issues if CT_2_* is missing, for example
        return list(dict(sorted(indexed_files.items())).values())

    def get_image(self, index):
        """
        Returns the image of the index
        """
        if self.num_images == 0:
            print("No DICOM file opened.")
            return None

        # The tag corresponding to the image is .pixel_array
        # As the name implies, it is not in an image format
        pixels = self.files[index].pixel_array

        img = Image.fromarray(pixels)
        q_img = ImageQt.ImageQt(img)
        return QPixmap.fromImage(q_img)

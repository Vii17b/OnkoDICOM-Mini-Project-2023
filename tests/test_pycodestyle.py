# Import needed package
import pycodestyle

# Create a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(
    [
        "main.py",
        "main_view.py",
        "image_popup.py",
        "directory_popup.py",
        "dicom.py",
        "main_controller.py",
        "main_model.py",
    ]
)

# Print result of PEP 8 style check
print(result.messages)

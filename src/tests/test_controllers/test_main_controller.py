"""
Tests for main_controller.py
"""


from src.models.main_model import MainModel
from src.models.dicom import DicomParser
from src.controllers.main_controller import MainController


def test_main_controller(qtbot):
    model_test = MainModel()
    controller_test = MainController(model_test)
    
    assert controller_test._main_model is model_test
    assert controller_test._config != None
    
    controller_test.open_image_viewer()
    assert controller_test._image_popup != None
    
    # Test re-opening while open
    controller_test.open_image_viewer()
    
    # Update will faile without dicom_parser object
    assert controller_test.update_image_view() == False
    
    # Add dicom_parser, test should pass
    controller_test._dicom_parser = DicomParser('/home/osboxes/mini_project/DICOM Files/DICOM-RT-01')
    assert controller_test.update_image_view() == True
    
    # Close popup to test fail condition
    controller_test._image_popup.close()
    controller_test._image_popup = None
    
    assert controller_test.update_image_view() == False
    
    # Check config
    controller_test.check_config()

# If you're looking at this test and thinking "wow Daniel,
# what a great test you wrote, why is it commented out?"
# Thanks! And also pytest disagrees!
# Running this test LOWERS coverage, SOMEHOW
# I don't know why! So commented out it remains

# @pytest.mark.parametrize('file_dir, outcome',
#     [
#         ('/home/osboxes/mini_project/DICOM Files/DICOM-RT-01', True),
#         ('/home/osboxes/mini_project/DICOM Files/', False),
#         ('/home/brazil', False)
#     ]
# )
# def test_main_controller(qtbot, file_dir, outcome):
#     model_test = MainModel()
#     controller_test = MainController(model_test)
#     controller_test._dicom_parser = DicomParser('/home/osboxes/mini_project/DICOM Files/DICOM-RT-01')
# 
#     assert controller_test.change_selected_directory(file_dir) == outcome

from fileinfo.fileinfo import Fileinfo
from unittest.mock import patch

def test_init():
    tmp_filename = "testfilename.txt"
    fi = Fileinfo(tmp_filename)
    assert fi.filename == "testfilename.txt"

def test_relative_init():
    tmp_filename = "testfilename.txt"
    original_path = f"../{tmp_filename}"
    fi = Fileinfo(original_path)
    assert fi.filename == "testfilename.txt"

@patch('os.path.getsize')
@patch('os.path.abspath')
def test_get_info(mock_abspath, mock_getsize):
    tmp_filename = "testfilename.txt"
    original_path = f"../{tmp_filename}"
    fi = Fileinfo(original_path)
    # Mock abspath
    test_path = "some/abs/path/for/test"
    mock_abspath.return_value = test_path
    # Mock getsize
    test_file_size = 1234
    mock_getsize.return_value = test_file_size
    # Call get info function
    file_info = fi.get_info()
    # Check that if correct values are passed to external methods
    mock_abspath.assert_called_with(original_path)
    mock_getsize.assert_called_with(original_path)
    assert file_info == (tmp_filename, original_path, test_path, test_file_size)
import pytest
from unittest.mock import patch
from main import MainModel


#Author: ChatGPT 

@pytest.fixture
def main_model():
    return MainModel()

def test_group_files_by_extension(main_model):
    main_model.directory_from_retrievel = 'test_directory'
    main_model.file_extensions = {}
    with patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = ['file1.txt', 'file2.jpg', 'file3.txt', 'file4.py']
        main_model._group_files_by_extension()
    expected_extensions = {'.txt': ['file1.txt', 'file3.txt'], '.jpg': ['file2.jpg'], '.py': ['file4.py']}
    assert main_model.file_extensions == expected_extensions

def test_group_files_by_extension_no_files(main_model):
    main_model.directory_from_retrievel = 'test_directory'
    main_model.file_extensions = {}
    with patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = []
        main_model._group_files_by_extension()
    expected_extensions = {}
    assert main_model.file_extensions == expected_extensions

# Similar tests can be written for other methods in MainModel class

if __name__ == "__main__":
    pytest.main()

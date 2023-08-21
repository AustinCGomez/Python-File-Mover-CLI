import pytest
import os
from main import MainView, MainModel

# Fixture to create temporary directories for testing
@pytest.fixture
def temp_directories(tmp_path):
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    dest_dir = tmp_path / "destination"
    dest_dir.mkdir()
    return source_dir, dest_dir

def test_obtain_directory(monkeypatch, temp_directories):
    # Simulate user input for the file dialog
    monkeypatch.setattr('builtins.input', lambda _: str(temp_directories[0]) + "\n" + str(temp_directories[1]))

    from_directory, to_directory = MainView.obtainDirectory()
    assert from_directory == str(temp_directories[0])
    assert to_directory == str(temp_directories[1])

def test_move_the_files(temp_directories):
    source_dir, dest_dir = temp_directories
    extension_list = [".txt", ".jpg"]

    # Create dummy files with specified extensions
    for ext in extension_list:
        (source_dir / f"file{ext}").touch()

    # Create a MainModel instance and set the directories and extension list
    main_model = MainModel()
    main_model.directory_from_retrievel = source_dir
    main_model.directory_to_retrievel = dest_dir
    main_model.extension_list = extension_list

    # Call the move_the_files() method
    main_model.move_the_files()

    for extension in extension_list:
        assert len(os.listdir(source_dir)) == 0
        assert len(os.listdir(dest_dir)) == 1

def test_search_directory(temp_directories, capsys):
    source_dir, _ = temp_directories
    extension_list = [".txt", ".jpg"]

    # Create dummy files with specified extensions
    for ext in extension_list:
        (source_dir / f"file{ext}").touch()

    MainModel.search_directory(source_dir)

    captured = capsys.readouterr()
    assert all(ext in captured.out for ext in extension_list)

if __name__ == "__main__":
    pytest.main()

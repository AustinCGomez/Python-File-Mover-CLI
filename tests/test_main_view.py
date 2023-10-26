from unittest.mock import Mock
import pytest
import os
import shutil
import typer
import time
from tkinter import filedialog
from tkinter import *


'''
MIT LICENSE
Copyright (c) [2023] [Austin Christopher Galindo Gomez]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''





class MainView:

    app = typer.Typer()

    def __init__(self):
        self.userInput = None
        self.fromAddress = None
        self.toAddress = None

    @app.command("movefolder",help = "Move folders and subdirectories from Directory A to Directory B")
    def d():
        typer.echo("Executing command --d")
        BeginMovingFiles = MainModel()
        BeginMovingFiles.move_entire_directories()


    @app.command("movefiles",help = "Move files by specific extensiohn from Directory A to Directory B")
    def m():
        typer.echo("Executing command --m")
        BeginMovingFiles = MainModel()
        BeginMovingFiles.obtain_directory()



    @app.command("search",help = "Search the different types of Files for review purposes in the selected Directory.")
    def s():
        typer.echo("Executing command --s")
        #Create new FileSearcher Object
        newFileSearch = MainModel()
        newFileSearch.search_directory()

    @app.command(help = "Program license information")
    def l():
        typer.echo("Executing command --l")
        print("This program utilizes the MIT License for the program. Thank you.")


    @staticmethod
    def obtainDirectory():
        print("Opening a Graphical User Interface(GUI) to obtain your directory to move files FROM")
        root = Tk()
        root.withdraw()
        from_directory = filedialog.askdirectory()
        to_directory = filedialog.askdirectory()
        if not from_directory:
            print("Error: You did not set any FROM Directory")
            return None, None
        if not to_directory:
            print("Error: You did not set any TO Directory")
            return None, None
        else:
            print(f"Success: We have obtained the directory: {from_directory}")
            print(f"Success: We have obtained the directory: {to_directory}")
            return from_directory, to_directory
        root = Tk()
        root.withdraw()




    def main(self):
        self.app()



#This will be our MainModel for the program and it contains all of the code for the operations of the program  ```
class MainModel:
    def __init__(self):
        self.directory_from_retrievel = None
        self.directory_to_retrievel = None
        self.continue_or_terminate = None
        self.file_extensions = {}


    def obtain_directory(self):
        self.directory_from_retrievel, self.directory_to_retrievel = MainView.obtainDirectory()
        if self.directory_from_retrievel == None:
            print("It is crucial that you pick the right TO directory. We will allow you to attempt to pick a new directory")
            print("Waiting 5 seconds...")
            time.sleep(5)
            MainModel.obtain_directory(self)
        if self.directory_from_retrievel == None:
            print("It is crucial that you pick the right TO directory. We will allow you to attempt to pick a new directory")
            print("Waiting 5 seconds...")
            time.sleep(5)
            MainModel.obtain_directory(self)
        # Warning statement where if the user says no then we terminate.
        # Safety feature so that the user has to actually read what they are doing.
        print("WARNING! This program will DELETE files in Directory A and move them to Directory B. Do you wish to continue? WARNING! ")
        continue_or_terminate = input("Do you want to continue or not? Yes or No").lower()
        if continue_or_terminate == "yes":
            MainModel.move_the_files(self)
        elif continue_or_terminate =="no":
            print("Program terminated")
        else:
            print("We did not understand what you said. Do you know what you are doing?")
            print("Program Terminated....")

    def move_entire_directories(self):
        self.directory_from_retrievel, self.directory_to_retrievel = MainView.obtainDirectory()
        shutil.move(self.directory_from_retrievel, self.directory_to_retrievel)


    def move_the_files(self):
        self.extension_list = []
        while True:
            self.getInput = input("Please enter each file extension that you want to move from the directory. Please type 'quit' when you are done")

            if self.getInput == 'quit':
                break

            self.extension_list.append(self.getInput)

        # Display the list of all of the file extensions that the user entered.
        print("Here are all of the file extensions that you chose to move:")
        for extension in self.extension_list:
            print(extension)

        print("We will now attempt to move the files based on extension from the list given..")
        # This will need to be modified eventually so that it can interact with the other classes to already have the directories?
        # this is just our path that we are going to use for testing purposes.
        print("folder_from")
        print(self.directory_from_retrievel)
        for file in os.listdir(self.directory_from_retrievel):
            if any(file.endswith(ext) for ext in self.extension_list):
                src_path = os.path.join(self.directory_from_retrievel, file)
                dest_path = os.path.join(self.directory_to_retrievel, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {file} to {dest_path}")
                print(f"Removed {file} in {src_path}")


    def search_directory(self):
        self.directory_from_retrievel, self.directory_to_retrievel = MainView.obtainDirectory()
        print(self.directory_from_retrievel)
        print(self.directory_to_retrievel)
        print("Testing the static method")
        while True:
            if os.path.isdir(self.directory_from_retrievel):
                print("Listing all files grouped by their extensions in the specified directory:")
                print(self.directory_from_retrievel)
                print("Files catagorized by groups: ")
                self._group_files_by_extension()
                print("Files catagorized by files: ")
                self._print_files_by_extension()
                print("Fles catagorized by entire directories: ")
                self._print_entire_directories()
                break
            else:
                print("Invalid directory path. Please enter a valid one.")

    def _group_files_by_extension(self):
        for filename in os.listdir(self.directory_from_retrievel):
            if os.path.isfile(os.path.join(self.directory_from_retrievel, filename)):
                _, ext = os.path.splitext(filename)
                self.file_extensions.setdefault(ext, []).append(filename)

    def _print_files_by_extension(self):
        for ext, files in self.file_extensions.items():
            print(f"Extension: {ext}")
            print('\n'.join(files))
            print()

    def _print_entire_directories(self):
        for entry in os.scandir(self.directory_from_retrievel):
            if entry.is_dir():
                print(f"Folders: {entry}")






# Mock the typer.Typer instance
class MockTyper:
    def __init__(self):
        self.commands = {}

    def command(self, name, **kwargs):
        def decorator(func):
            self.commands[name] = func
            return func
        return decorator

    def __call__(self):
        pass

@pytest.fixture
def mock_typer(monkeypatch):
    mock = MockTyper()
    monkeypatch.setattr('main.typer.Typer', lambda: mock)
    return mock

@pytest.fixture
def main_view(mock_typer):
    return MainView()

#def test_d_command_execution(mock_typer, main_view):
#    main_view.app()
#    assert 'movefolder' in mock_typer.commands

#def test_m_command_execution(mock_typer, main_view):
#    main_view.app()
#    assert 'movefiles' in mock_typer.commands

#def test_s_command_execution(mock_typer, main_view):
#    main_view.app()
#    assert 'search' in mock_typer.commands

#def test_l_command_execution(mock_typer, main_view):
#    main_view.app()
#    assert 'l' in mock_typer.commands

#def test_obtain_directory_called(main_view, monkeypatch):
#    mock_obtain_dir = Mock(return_value=('/path/to/from', '/path/to/to'))
#    monkeypatch.setattr('your_script.MainView.obtainDirectory', mock_obtain_dir)
#    main_view.obtainDirectory()
#    mock_obtain_dir.assert_called_once()

# More tests can be added as needed

if __name__ == '__main__':
    pytest.main()

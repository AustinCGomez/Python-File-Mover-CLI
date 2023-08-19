import os
import shutil
from tkinter import filedialog
from tkinter import *

class CommandAndControl:
    def __init__(self):
        self.userInput = None
        self.fromAddress = None
        self.toAddress = None

    @staticmethod
    def obtainDirectory():
        print("Opening a Graphical User Interface(GUI) to obtain your directory to move files FROM")
        root = Tk()
        root.withdraw()
        from_directory = filedialog.askdirectory()
        print(f"Success: We have obtained the directory: {from_directory}")
        print("Opening a Graphical User Interface(GUI) to obtain your directory to move files FROM")
        root = Tk()
        root.withdraw()
        to_directory = filedialog.askdirectory()
        print(f"Success: We have obtained the directory: {to_directory}")
        return from_directory, to_directory

    def begin(self):
        print("Python File Mover CLI 0.1 Alpha")
        print("OPTIONS: -s Search directory and return all files in the specific directory || -m Move files from one directory to another directory")
        self.userInput = input("Please enter your desired command here: ").lower()
        #A simple input validation approach
        if self.userInput == "-s":
            #Create new FileSearcher Object
            newFileSearch = FileSearcher()
            newFileSearch.search_directory()

        elif self.userInput == '-m':
            #Create new MoveFiles Object
            newMove = MoveFiles()
            newMove.obtain_directory()
        else:
            print("Sorry, you did not enter valid information")


class FileSearcher:
    def __init__(self):
        self.directory_from_retrievel = None
        self.directory_to_retrievel = None
        self.file_extensions = {}

    def search_directory(self):
        self.directory_from_retrievel, self.directory_to_retrievel = CommandAndControl.obtainDirectory()
        print(self.directory_from_retrievel)
        print(self.directory_to_retrievel)
        print("Testing the static method")
        while True:
            if os.path.isdir(self.directory_from_retrievel):
                print("Listing all files grouped by their extensions in the specified directory:")
                print(self.directory_from_retrievel)
                print("Excellent news")
                self._group_files_by_extension()
                self._print_files_by_extension()
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


class MoveFiles:
    def __init__(self):
        self.folder_from = None
        self.folder_to = None

# This method will obtain the directory with the code already defined in the static method.
    def obtain_directory(self):
        self.folder_from, self.folder_to = CommandAndControl.obtainDirectory()
        MoveFiles.move_the_files(self)


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
        print(self.folder_from)
        for file in os.listdir(self.folder_from):
            if any(file.endswith(ext) for ext in self.extension_list):
                src_path = os.path.join(self.folder_from, file)
                dest_path = os.path.join(self.folder_to, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {file} to {dest_path}")
                print(f"Removed {file} in {src_path}")


if __name__ == "__main__":
    BeginProgram = CommandAndControl()
    BeginProgram.begin()

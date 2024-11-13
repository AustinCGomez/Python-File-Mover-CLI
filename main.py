'''
MIT LICENSE
Copyright (c) [2024] [Austin Gomez]

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
# This is a prototype of a new menu using Click
import os
import sys
import shutil
import typer
import time
from tkinter import filedialog
from tkinter import *
import click
from art import *
import send2trash

''' Static functions that give some information about our program'''
LOGO = text2art("Python File Mover")
GOODBYE = text2art("GOODBYE")
CONTRIBUTE = ("Want additional features? Spotted a bug? Head to our Github and lend a helping hand :) ->  https://github.com/AustinCGomez/Python-File-Mover-CLI")
VERSION = "Version 0.3.5.1"
LICENSE = "This software is published under the MIT License."
AUTHOR = "Program designed and Authored by Austin Gomez."
WARNING = "OK"


class DirectoryStructureInfoProcess():
    ''' This process will gather the information from each directory and deliver
        it right back to the class the requested the information. It will also
        handle proper formatting. '''
    def __init__(self, blank):
        self.blank = None
    def showFiles(self, dir_a, dir_b):
        print(f"Files found in {dir_a}: ")
        for dirA_files in os.listdir(dir_a):
            print(dirA_files)
        print(" ")
        print(f"Files found in {dir_b}: ")
        for dirB_files in os.listdir(dir_b):
            print(dirB_files)
    def showFolders(self, dir_a, dir_b):
        print(f"Folders found in {dir_a}:")
        for dirA_folders in os.listdir(dir_a):
            if os.path.isdir(dirA_folders):
                print(dirA_folders)
        for dirB_folders in os.listdir(dir_b):
            if os.path.isdir(dirB_folders):
                print(dirB_folders)

class GatherDirectoriesProcess():
    ''' We will use one class only to get our To and FROM directories since the program can use it for all functions.
        ALl of the code to get and verify the directories will be in this class only. Any other classes
        can therefore create an instance of it.  '''
    def __init__(self, directory_a, directory_b):
        self.directory_from = directory_a
        self.directory_to = directory_b
    def process_error_handling(self, error_reason):
        print(f"Please re-enter the directories so that they are not {error_reason}")
    def obtain_dirs(self):
        print("Please choose the source directory from which files will be moved via the Graphical User Interface.")
        print(" ")
        print("Opening the graphical user interface just one moment.")
        time.sleep(1)
        self.directory_from = filedialog.askdirectory()
        print("Directory selected!")
        print(" ")
        time.sleep(1)
        print("Please choose the destination directory from which files will be moved via the Graphical User Interface.")
        print(" ")
        print("Opening the graphical user interface just one moment")
        self.directory_to = filedialog.askdirectory()
        while not self.directory_from:
            self.directory_from = filedialog.askdirectory()
            if not self.directory_from:
                print("You will need to define a source folder before we can move forward.")
                time.sleep(2)
        while not self.directory_to:
            self.directory_to = filedialog.askdirectory()
            time.sleep(2)
            if not self.directory_to:
                print("You will need to define a destination folder before we can move forward.")
                time.sleep(2)

        if self.directory_from == self.directory_to:
            print("Error: Directory TO and Directory FROM cannot be the same!")
            self.obtain_dirs()


        return self.directory_from, self.directory_to
class ObtainFileExtensionListProcess():
    '''This service process will obtain our file extension list which will then be sent
    back to the MoveFileCommand() to be utilized for the operation of moving files by extension. '''
    def __init__(self, user_list=None):
        self.extension_list = []
    def obtain_file_list(self):
        while True:
            self.getInput = input("Please enter each file extension that you want to move files from | Type 'quit' when done.")

            if self.getInput == 'quit':
                break

            self.extension_list.append(self.getInput)

            print("List of user entered file extensions: ")

        return self.extension_list

class EndProgramProcess():
    '''This command will end the program when invoked. It's made into its class so that an instance can be made quickly from any
    class and therefore less code has to be written over and over again to end the program. '''
    def __init__(self):
        self.EndProgram = None
    def end(self):
        print("-" * 130)
        print(GOODBYE)
        print(CONTRIBUTE)
        print(LICENSE)
        print(AUTHOR)
        print("-" * 130)
        time.sleep(2)
        sys.exit()


class MainMenu():
    ''' This class displays all of our classes and allows the user to select what actions they want to take '''
    def __init__(self):
        self.directory_from = None
        self.directory_to = None
        self.file_path = None
    def main(self):
        print(LOGO)
        print(VERSION)
        print(LICENSE)
        print(" ")
        click.echo("Please choose the obtain below to begin: ")
        action = click.prompt(
        "--move-files - Move files by specific file extension from Directory A to Directory B!\n"
        "--move-folders - Move Entire Folders from Directory A to Directory B!\n"
        "--move-to-recycle-bin - Move file to the recycle bin!\n",
        "--quit - Exit out of the program",
        type = click.Choice(['--move-files', '--move-folders', '--move-to-recycle-bin', '--quit'])
        )

        if action == "--move-files".lower():
            self.move_files_by_extension()
        elif action == "--move-folders":
            self.move_entire_folders()
        elif action == '--move-to-recycle-bin':
            self.move_to_recycle_bin()
        elif action == '--quit':
            QuitProgram = EndProgramProcess()
            QuitProgram.end()
    def move_to_recycle_bin(self):
        new_file_move = MoveFilesToTrashCommand(self.file_path)
        new_file_move.process_move()

    def move_files_by_extension(self):
        new_file_move = MoveFilesCommand(self.directory_from, self.directory_to)
        new_file_move.start_command()
        #go_to_move_command.start_command(blank_dir_a, blank_dir_b)

    def move_entire_folders(self):
        #Create a new instance in the #MoveFoldersCommand
        new_folder_move = MoveFoldersCommand(self.directory_from, self.directory_to)
        new_folder_move.process_file_move()

class MoveFilesCommand():
    '''This class will mooove the files based on the user-defined extensions list.  '''
    def __init__(self, dir_a, dir_b):
        self.directory_from = None
        self.directory_to = None
        self.user_extensions = []

    def process_move(self):
        output_padding = " " * (len("Name") - len("Extension"))
        click.echo("Please choose the obtain below to begin: ")
        action = click.prompt(
            "--begin - Begin the process of moving files first by obtaining a list of file extensions. B\n"
            "--quit - Quit the Move command and return to the main menu.",
            type = click.Choice(['--begin', '--quit'])
        )

        if action == "--begin":
            retrieve_file_extensions = ObtainFileExtensionListProcess(self.user_extensions)
            self.user_extensions = retrieve_file_extensions.obtain_file_list()
            print(" ")
            print("User Selected Extensions: ")
            print("--------------------------")
            for extension in self.user_extensions:
                print(extension)
            time.sleep(2)
            print("ATTEMPTING to move files based on extension from Directory A to Directory B")
            time.sleep(1)

            # Normalize user extensions to lowercase
            normalized_extensions = [ext.lower() for ext in self.user_extensions]

            # Check for files in the source directory
            from_file_ext = [os.path.splitext(file)[-1].lstrip('.').lower() for file in os.listdir(self.directory_from)]
            for ext in normalized_extensions:
                if ext not in from_file_ext:
                    print(f'{ext} extension not found in directory {self.directory_from}. Please reenter the extension names.\n')
                    self.process_move()

            for file in os.listdir(self.directory_from):
                if any(file.lower().endswith(ext) for ext in normalized_extensions):  # Normalize case
                    src_path = os.path.join(self.directory_from, file)
                    dest_path = os.path.join(self.directory_to, file)
                    shutil.move(src_path, dest_path)
                    print(f"Name: {file}{output_padding} - Removed From: {src_path} and moved to: {dest_path}")
                    print(" ")
        elif action == "--quit":
            end_program = EndProgramProcess()
            EndProgramProcess.end(self.directory_from)


    def start_command(self):
        print(WARNING)
        print("Opening a Graphical User Interface(GUI) to obtain your directories to move files FROM A to B")
        # Create a new instance in Obtain_Directory to ensure that the directories arw what we want.
        verify_directories = GatherDirectoriesProcess(self.directory_from, self.directory_to)
        self.directory_from, self.directory_to = verify_directories.obtain_dirs()
        display_dir_info = DirectoryStructureInfoProcess("blank")
        display_dir_info.showFiles(self.directory_from, self.directory_to)
        self.process_move()

class MoveCategoriesCommand():
    def __init__(self, dir_a, dir_b):
        self.directory_from = None
        self.directory_to = None

class MoveFoldersCommand():
    def __init__(self, dir_a, dir_b):
        self.directory_from = None
        self.directory_to = None
        self.user_extensions = []
    def process_file_move(self):
        verify_directories = GatherDirectoriesProcess(self.directory_from, self.directory_to)
        #We will attempt to verify our directories to make sure that the user entered them in correctly.
        self.directory_from, self.directory_to = verify_directories.obtain_dirs()
        display_folder_info = DirectoryStructureInfoProcess("blank")
        display_folder_info.showFolders(self.directory_from, self.directory_to)
        shutil.move(self.directory_from, self.directory_to)
        print(f"SUCCESS: The Folder has been moved from {self.directory_from} to {self.directory_to}")
        print(" ")
        click.echo("Do you want to move more folders?")
        action = click.prompt( 
            "--no\n"
            "--yes",
        type = click.Choice(['--no', '--yes'])
        )
        if action == "--no":
            print("Sending you back to main menu..")
            time.sleep(1)
            print("One moment...reinitilizing")
            StartAgain = MainMenu()
            StartAgain.main()
            time.sleep(1)
        elif action == "--yes":
            print("One moment...reinitilizing")
            time.sleep(1)
            self.process_file_move()


class MoveFilesToTrashCommand():
    def __init__(self, file_path):
        self.file_path = file_path
        #self.directory_to = os.environ.get('SystemRoot') + r'\$Recycle.Bin'
        pass

    def process_move(self):
        output_padding = " " * (len("Name") - len("Extension"))
        #Obtain extensions from our Extension Process first.
        click.echo("Please choose the obtain below to begin: ")
        action = click.prompt(
        "--begin - Begin the process of moving files first by obtaining a list of file extensions. B\n"
        "--quit - Quit the Move command and return to the main menu.",
        type = click.Choice(['--begin', '--quit'])
        )

        if action == "--begin":
            print("This action will move files to the recycle bin!")
            file_path = filedialog.askopenfilename()

            if file_path:
                file_path = os.path.normpath(file_path)
            send2trash.send2trash(file_path)

        elif action == "--quit":
            # Create a new instance invoking that the user wants to end the program.
            end_program = EndProgramProcess()
            EndProgramProcess.end(self.directory_from)


if __name__ == "__main__":
    BeginProgram = MainMenu()
    BeginProgram.main()


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

''' Static functions that give some information about our program'''
LOGO = text2art("Python FIle Mover")
GOODBYE = text2art("GOODBYE")
Contribute = ("Want additional features? Spotted a bug? Head to our Github and lend a helping hand :) ->  https://github.com/AustinCGomez/Python-File-Mover-CLI")
VERSION = "Version 0.3.0 Beta."
LICENSE = "This software is published under the MIT License."
AUTHOR = "Austin Gomez."
WARNING = "!!WARNING!! This command will DELETE files from Directory A and move them to DIRECTORY B."

class GatherDirectoriesProcess():
    ''' We will use one class only to get our To and FROM directories since the program can use it for all functions.
        ALl of the code to get and verify the directories will be in this class only. Any other classes
        can therefore create an instance of it.  '''
    def __init__(self, directory_a, directory_b):
        self.directory_from = directory_a
        self.directory_to = directory_b
    def obtain_dirs(self):
        root = Tk()
        root.withdraw()
        self.directory_from = filedialog.askdirectory()
        self.directory_to = filedialog.askdirectory()
        while not self.directory_from:
            self.directory_from = filedialog.askdirectory()
            if not self.directory_from:
                print("Error: Please define an FROM directory.")
        while not self.directory_to:
            self.directory_to = filedialog.askdirectory()
            if not self.directory_to:
                print("Error: Please define an TO directory.")

        print(f"Obtained Directory A: {self.directory_from}")
        print(f"Obtained Directory B: {self.directory_to}")

        root.destroy()

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

class DefineCommands():
    ''' This class displays all of our classes and allows the user to select what actions they want to take '''
    def __init__(self):
        self.directory_from = None
        self.directory_to = None
    def main(self):
        print(LOGO)
        print(VERSION)
        print(LICENSE)
        print(" ")
        click.echo("Please choose the obtain below to begin: ")
        action = click.prompt(
        "--movefr - Move folders and subdirectories from Directory A to Directory B\n"
        "--movefs - Move files by specific extension from Directory A to Directory B\n"
        "--search - Search for different types of files for review purposes in the selected directories",
        type = click.Choice(['--movefr', '--movefs', '--search'])
        )

        if action == "--movefr":
            self.move_folders()
        elif action == "--movefs":
            self.move_files()
        elif action == '--search':
            self.search_directory()

    def move_folders(self):
        new_file_move = MoveFilesCommand(self.directory_from, self.directory_to)
        new_file_move.start_command()
        #go_to_move_command.start_command(blank_dir_a, blank_dir_b)

    def move_files(self):
        print("To Be Determined ")

    def searchFiles(self):
        print("To Be Determined ")

class MoveFilesCommand():

    def __init__(self, dir_a, dir_b):
        self.directory_from = None
        self.directory_to = None
        self.user_extensions = []

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
            #create new instance to create file extension page.

            retrieve_file_extensions = ObtainFileExtensionListProcess(self.user_extensions)
            self.user_extensions = retrieve_file_extensions.obtain_file_list()
            print(" ")
            print("User Selected Extensions: ")
            print("--------------------------")
            for extension in self.user_extensions:
                print(extension)
            time.sleep(2)
            print("ATTEMPTING to move files based on extension from Directory A to Directory B")
            print("TEST: Double Check Dirs")
            print(self.directory_from)
            print(self.directory_to)
            for file in os.listdir(self.directory_from):
                if any(file.endswith(ext) for ext in self.user_extensions):
                    src_path = os.path.join(self.directory_from, file)
                    dest_path = os.path.join(self.directory_to, file)
                    shutil.move(src_path, dest_path)
                    print(f"Name: {file}{output_padding} - Removed From: {src_path} and moved to: {dest_path}")
                    print(" ")



        elif action == "--quit":
            print("-" * 130)
            print(GOODBYE)
            print(Contribute)
            print("-" * 130)
            time.sleep(2)
            sys.exit()

    def start_command(self):
        print(WARNING)
        print("Opening a Graphical User Interface(GUI) to obtain your directories to move files FROM A to B")
        # Create a new instance in Obtain_Directory to ensure that the directories arw what we want.
        verify_directories = GatherDirectoriesProcess(self.directory_from, self.directory_to)
        self.directory_from, self.directory_to = verify_directories.obtain_dirs()
        # Our input will be validated at this point and can be moved down the process line.
        self.process_move()
        #move_files = MoveFilesCommand(self.directory_from, self.directory_to)
        #move_files.process_move()








if __name__ == "__main__":
    BeginProgram = DefineCommands()
    BeginProgram.main()

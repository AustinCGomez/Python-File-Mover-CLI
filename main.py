import os
import shutil
import typer
from tkinter import filedialog
from tkinter import *

class MainView:

    app = typer.Typer()

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
        print("Opening a Graphical User Interface(GUI) to obtain your directory to move files TO")
        root = Tk()
        root.withdraw()
        to_directory = filedialog.askdirectory()
        print(f"Success: We have obtained the directory: {to_directory}")
        return from_directory, to_directory


    @app.command()
    def m():
        typer.echo("Executing command --m")
        newMove = MoveFiles()
        newMove.obtain_directory()


    @app.command()
    def s():
        typer.echo("Executing command --s")
        #Create new FileSearcher Object
        newFileSearch = FileSearcher()
        newFileSearch.search_directory()

    def main(self):
        self.app()

# The Controller is the interface between the View and the Model.
class MainController:
    def __init__(self):
        self.userInput = None
        self.fromAddress = None
        self.toAddress = None



# The Model will define all of our actions and relay it to the controller.
class MainModel:
    def __init__(self):
        self.userInput = None
        self.fromAddress = None
        self.toAddress = None
        self.directory_from_retrievel = None
        self.directory_to_retrievel = None
        self.file_extensions = {}


if __name__ == "__main__":
    BeginProgram = MainView()
    BeginProgram.main()

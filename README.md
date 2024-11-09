![alt text](https://i.imgur.com/z1ogxT9.png)

# Version 0.3.5
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

This program provides a simple way to move massive amounts of files from one directory to another directory without having to manually go into your directories and move each file one by one. With PythonFileMover all you have to do is open up your command line and run our simple commands to move your files around on your computer with ease.  You can move massive amounts of files

Move massive amounts of files, either by extension(i.e. .txt ) or folder(i.e. WorkFiles) from one directory(I.E. C:/) to another directory (I.E. D:/) with only a few lines. Save yourself time from having to constantly copy and paste the files and get back to doing more important things!



# Features
- Move files from Directory A to Directory B with only a few commands.
- Move entire folders from Directory A to Directory B.

# Download and Install
Please download the code from our GitHub then launch the program using 'python main.py'. You will then be led to our very intuitive interactive mode! From the interactive mode, you can do the following
- ✨ Move large amounts of folders from Directory A to Directory B: `--move-files`
- ✨ Move large amounts of files from Directory A to Directory B: `--move-folders`

***Note: Currently our program only moves files within Windows PCs but we plan to expand to Linux and OSX in future versions.***  

The program currently must be build in order to run it. In addition, it is currently only tested for Windows PCs
- Step 1: Install Python 3+
- Step 2: Ensure you have the following dependencies installed(: os, shutil, typer, time, tkinter)
- Step 2: Download the recent release from Github.
- Step 3: Open a command line or powershell as an administrator on your Windows PC.
- Step 4: Navigate to the directory where the source code is stored and run `python main.py`. You will then open the interactive mode and be able to run the codes specified!

# Usage Example
Our program is built to be simple and straight to the point. We designed an interactive mode that walks you through the entire process as soon as you type `python main.py`.

**Sort and move files by extension**
By running the `--move-files` command you will be able to move all files within your Windows Directory from one directory to another directory. We open up a GUI dashboard that lets you select the directories so you do not have to worry about having to remember where the directories are at on your computer.

**Move folders from one directory to another directory**
By running the `--move-folders` command you will be able to more entire folders(and folders within folders) with just a few clicks of a button.  Just select your two directories with our convenient GUI for selecting directories and type --begin to launch the program.


# Contribute
Our maintainer is currently building a GUI interface to define future iterations of this project. Code contributions will be halted till the GUI is developed as there will be extensive changes to the code base and overal structure of the program. Bug reports are still appreciated and also documentation improvements. We expect the new GUI to be released around late November 2024.


### Want to report bugs or ask for additional features?  
Thank you for thinking of an idea or reporting a bug. You can place your idea or enhancement idea into our issues tab for consideration. All bug reports are appreciated along with enhancement ideas.

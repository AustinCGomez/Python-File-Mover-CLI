from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.3.0'
DESCRIPTION = 'Move files with ease.'
LONG_DESCRIPTION = 'Move python files with ease from one directory to another on your Windows PC.'

# Setting up
setup(
    name="pythonfilemover",
    version=VERSION,
    author="Austin Gomez",
    author_email="<doawriting@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['os','sys','shutil','typer','time','tkinter','click','art'],
    keywords=['python', 'move files', 'modify files', 'windows', 'windows 10', 'windows 11'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)

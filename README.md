# OnkoDICOM-Mini-Project-2023
PySide6 programme opens DICOM file and display the images. 

## Overview
- PySide6 program checks for the existence of a preferences configuration record at startup. If the record is found, it reads the configuration and proceeds accordingly. 
- The stored information includes details such as the default directory for locating DICOM files. This information is stored within a SQLite database.
- Program will proceed by opening a DICOM file in a fault tolerate way. A DICOM file can consist of multiple elements. 
- The program needs to check if specific elements. If any of these elements are missing, the program will prompt the user for further instructions on how to proceed. 

## Requirement
# The program must meet the following requirements
- Ensure complient using pycodestyle
- Use pylint
- Unit test with pytest ((80% test code coverage)

## Instructions on how to run (on Ubuntu)
Mini project programme requires python3-dev, git and poetry installed and can be installed by running these commands in the terminal.

`sudo apt update`

To install Python 3.10

`sudo apt-get install git gcc libopengl0`

Install all required prerequisite dependencies

`sudo apt-get install make build-essential libssl-dev zlib1g-dev  libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm  libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev`

Download and execute installation script

`curl https://pyenv.run | bash`

Add the following entries into your ~/.bashrc file

`# pyenv`

`export PATH="$HOME/.pyenv/bin:$PATH"`

`eval "$(pyenv init --path)"`

`eval "$(pyenv virtualenv-init -)"`

Restart your shell

`exec $SHELL`

Validate installation

`pyenv --version`

Find the latest python 3.10 version

`pyenv install --list  | grep -i 3.10`

Install the lastest version

`pyenv install 3.10.x`

To set a specific version of Python global (system-wide) use global flag

`pyenv global 3.10.x`

Mini project use Poetry, to download poetry

`curl -sSL https://install.python-poetry.org | python3 -`

Add Poetry to your PATH according to the instruction shows on the terminal.

# To run the program
Before running the program, download the DICOM files first from the ONKODicom Wiki [ONKODicom](https://github.com/didymo/OnkoDICOM/wiki/Data-to-pracise)

Clone the Mini Project repository: 

`git clone https://github.com/Vii17b/OnkoDICOM-Mini-Project-2023.git`

Go to the directory that contain the Mini Project

`cd OnkoDICOM-Mini-Project-2023`

Initiate the virtual environment using

`poetry shell`

Install the requirements

`pip install -r requirements.txt`

Run the program

`python3 MiniProject.py`

## Unit Test

All testing is to be done in the virtual environment from the Mini Project directory (clone from github, instruction above), if you are not in the directory, move to the directoy by 

`cd OnkoDICOM-Mini-Project-2023`

Initiate the virtual environment using

`poetry shell`

Test code coverage report with Pytest use this command:

`pytest --cov=src`

Test for Pylint complience:

`pylint --extension-pkg-whitelist=PyQt6,PySide6 src/`

Test for Pycodestyle complience:

`pycodestyle --show-source --show-pep8 src/`


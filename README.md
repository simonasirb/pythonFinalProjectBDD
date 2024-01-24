# pythonFinalProjectBDD

Application Under Test: Jules.app
Jules.app is a comprehensive online service designed to serve both homeowners and real estate companies. It encompasses a wide range of functionalities, catering to the diverse needs of its users. Each Jules service utilizes a vast database that houses information about homes, their associated properties, and the personal details of their residents.

Testing Methodology

## Technologies Used

* Python
* PyCham IDE

## Essential Requirements
Essential Requirements
To ensure successful application execution, please fulfill the following prerequisites:

### Prerequisite 1: Python 3.12

Verify Python Version:
> python --version

If the output displays a valid Python version (3.12 or later), Python is already installed and no further action is required. Otherwise, update python from the official website: https://www.python.org/downloads/

### Prerequisite 2: pip

Check pip Installation

> pip --version

If the output shows a pip version, pip is installed and no further action is necessary. Otherwise, proceed to the installation the latest version of pip using the official source: https://pypi.org/project/pip/

### Prerequisite 3: venv (Virtual Environment)
Create a Virtual Environment


## Test Scenarios Employed:

* Invalid Password Login
* Invalid Username Login
* Successful Login
* Main Page Popup Closure
* Adding a Person with First Name
* Adding a Person with Last Name
* Adding a Person with Complete Name
* Viewing Added People List
* Deleting First Added Person
* Logout

## Generating the report for the tests

You can run the tests and generate a report for them using the command:

> behave -f html -o report.html
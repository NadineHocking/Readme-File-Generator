# Readme-File-Generator 


A Python command-line tool that interactively asks about your GitHub project
(Project title, short project description, installation instructions, usage information, license dropdown, author, and contact info) and auto generates a GitHub `readme.md`.

## Table of contents

- [Project structure](#project-structure)
- [Compatibility warning](#compatibility-warning)
- [Setup](#setup)
- [Usage](#usage)
- [Running the Tests](#running-the-tests)
- [Author](#author)
- [Contact](#contact)


## Project structure


readme-generator/
├── requirements.txt
├── README.md
├── src/
│   ├── __pycache__
│   ├── __init__.py
│   ├── licenses.py      # License catalogue (badges + footer text)
│   ├── questions.py     # Questionnaire class (wraps PyInquirer prompts)
│   ├── generator.py     # ReadmeGenerator class (builds & writes markdown)
│   └── main.py          # CLI entry point
└── tests/
    ├── __init__.py
    └── test_generator.py

## Compatibility warning

Python Compatibility: `PyInquirer` **does not work** on Python 3.10 or newer due to internal dependency conflicts. 
Supported Versions: PyInquirer only runs reliably on **Python 3.6 to Python 3.9**

## Setup

1. Clone the repository

   ` ` `bash
   git clone https://github.com/NadineHocking/Readme-File-Generator.git
   cd Readme-File-Generator

   ` ` `

2. Setup a compatible Python environment

Because `PyInquirer` requires an older Python version, you should isolate it using a tool like `pyenv` combined with a virtual environment (`venv`).

Follow these steps to set it up:

**2.1. Install pyenv**
`pyenv` allows you to manage and switch between multiple versions of Python on a single machine.
Mac (via Homebrew): `brew install pyenv`
Linux: Use the automatic installer via `curl https://pyenv.run | bash`
Windows: Use `pyenv-win` via PowerShell: `Invoke-WebRequest -UseBasicParsing -Uri "https://github.com" | Invoke-Expression`

**2.2. Install a supported Python version**
Install Python 3.9 (the highest stable version supported by the library):
` ` `bash
pyenv install 3.9.19
` ` `

**2.3. Set your local Python version**
Navigate to your project directory and set it to use the newly installed version:
` ` `bash
cd your-project-directory
pyenv local 3.9.19
` ` `
Verify the change worked by running `python --version`.

**2.4. Create and Activate a Virtual Environment**
Create a clean isolated environment using the downgraded Python version:
```bash
# Create the environment
python -m venv .venv

# Activate it (Mac/Linux)
source .venv/bin/activate

# Activate it (Windows PowerShell)
.\.venv\Scripts\Activate.ps1
```

**2.5. Install PyInquirer**
Once your environment is active and running Python 3.9, install the package securely:
` ` `bash
pip install PyInquirer
` ` `

## Usage

Run the application as a module from the project root (with your
virtual environment activated):

` ` `bash
python -m src.main
` ` `

Answer each prompt as it appears. When finished, a `readme.md` file
will be written to the current directory and the tool will print its
full path.

To deactivate the virtual environment when you're done:

` ` `bash
deactivate
` ` `

## Running the Tests

The core markdown-generation logic is covered by unit tests that don't
require an interactive terminal:

` ` `bash
python -m unittest discover tests
` ` `

## Author

Nadine Hocking

## Contact

<nadinehocking@gmail.com>

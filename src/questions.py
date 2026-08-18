# Wraps PyInquirer prompts so main.py doesn't need to know prompt details.

from PyInquirer import prompt

from .licenses import license_choices


class Questionnaire:
    # Collects README details from the user via interactive CLI prompts."""

    def __init__(self):
        self._questions = [
            {
                "type": "input",
                "name": "title",
                "message": "Project title:",
                "validate": lambda result: len(result) > 0 or "Title cannot be empty",
            },
            {
                "type": "input",
                "name": "description",
                "message": "Short project description:",
                "validate": lambda result: len(result) > 0 or "Description cannot be empty",
            },
            {
                "type": "input",
                "name": "installation",
                "message": "Installation instructions (e.g. pip install -r requirements.txt):",
            },
            {
                "type": "input",
                "name": "usage",
                "message": "Usage information (how to run/use the project):",
            },
            {
                "type": "list",
                "name": "license",
                "message": "Choose a license:",
                "choices": license_choices(),
            },
            {
                "type": "input",
                "name": "author",
                "message": "Author name:",
                "validate": lambda result: len(result) > 0 or "Author name cannot be empty",
            },
            {
                "type": "input",
                "name": "contact",
                "message": "Contact information (email, GitHub URL, etc.):",
            },
        ]

    def ask(self) -> dict:
        return prompt(self._questions)
# Run with: python -m src.main

import sys

from .generator import ReadmeGenerator
from .questions import Questionnaire


def run(output_path: str = "readme.md") -> None:
    print("README Generator")
    print("-----------------")
    print("Answer the following questions to generate a readme.md\n")

    questionnaire = Questionnaire()
    answers = questionnaire.ask()

    if not answers:
        # InquirerPy returns None/empty if the user cancels (Ctrl+C).
        print("\nNo answers collected. Exiting without generating a readme.")
        sys.exit(1)

    generator = ReadmeGenerator(answers)
    path = generator.write(output_path)

    print(f"\nDone! README saved to {path.resolve()}")


if __name__ == "__main__":
    run()

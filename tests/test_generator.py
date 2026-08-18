# Run: python -m unittest discover tests

import unittest
from pathlib import Path
import tempfile
import shutil

from src.generator import ReadmeGenerator


SAMPLE_ANSWERS = {
    "title": "Awesome Project",
    "description": "A tool that does awesome things.",
    "installation": "pip install -r requirements.txt",
    "usage": "python -m src.main",
    "license": "MIT",
    "author": "Jane Doe",
    "contact": "jane@example.com",
}


class TestReadmeGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ReadmeGenerator(SAMPLE_ANSWERS)
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_title_appears_as_h1(self):
        output = self.generator.build()
        self.assertIn("# Awesome Project", output)

    def test_all_sections_present(self):
        output = self.generator.build()
        for heading in ["Description", "Installation", "Usage", "License", "Author", "Contact"]:
            self.assertIn(f"## {heading}", output)

    def test_installation_wrapped_in_code_block(self):
        output = self.generator.build()
        self.assertIn("```bash\npip install -r requirements.txt\n```", output)

    def test_license_badge_and_footer_included(self):
        output = self.generator.build()
        self.assertIn("License-MIT", output)
        self.assertIn("MIT License", output)

    def test_missing_optional_contact_omits_section(self):
        answers = {**SAMPLE_ANSWERS, "contact": ""}
        output = ReadmeGenerator(answers).build()
        self.assertNotIn("## Contact", output)

    def test_write_creates_file_on_disk(self):
        output_path = Path(self.tmpdir) / "README.md"
        result_path = self.generator.write(str(output_path))
        self.assertTrue(result_path.exists())
        self.assertIn("Awesome Project", result_path.read_text(encoding="utf-8"))

    def test_unknown_license_defaults_to_none(self):
        answers = {**SAMPLE_ANSWERS, "license": "Not A Real License"}
        output = ReadmeGenerator(answers).build()
        self.assertIn("No license has been specified", output)


if __name__ == "__main__":
    unittest.main()

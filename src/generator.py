# Builds the readme.md markdown from a dict of user answers.

from pathlib import Path

from .licenses import get_license


class ReadmeGenerator:
    # Builds and writes a readme.md file from collected project answers.

    def __init__(self, answers: dict):
        self.title = answers.get("title", "").strip()
        self.description = answers.get("description", "").strip()
        self.installation = answers.get("installation", "").strip()
        self.usage = answers.get("usage", "").strip()
        self.license = get_license(answers.get("license", "None"))
        self.author = answers.get("author", "").strip()
        self.contact = answers.get("contact", "").strip()

    def build(self) -> str:
        sections = [
            self._build_header(),
            self._build_table_of_contents(),
            self._build_section("Description", self.description),
            self._build_section("Installation", self._as_code_block(self.installation)),
            self._build_section("Usage", self.usage),
            self._build_license_section(),
            self._build_author_section(),
        ]
        # Filter out any empty sections and join with blank lines between them.
        return "\n\n".join(section for section in sections if section) + "\n"

    def _build_header(self) -> str:
        badge = self.license.badge_markdown
        header = f"# {self.title}"
        if badge:
            header += f"\n\n{badge}"
        return header

    def _build_table_of_contents(self) -> str:
        return (
            "## Table of Contents\n\n"
            "- [Description](#description)\n"
            "- [Installation](#installation)\n"
            "- [Usage](#usage)\n"
            "- [License](#license)\n"
            "- [Author](#author)\n"
            "- [Contact](#contact)"
        )

    def _build_section(self, heading: str, body: str) -> str:
        if not body:
            return ""
        return f"## {heading}\n\n{body}"

    def _build_license_section(self) -> str:
        return f"## License\n\n{self.license.footer_markdown}"

    def _build_author_section(self) -> str:
        lines = [f"## Author\n\n**{self.author}**"]
        if self.contact:
            lines.append(f"\n## Contact\n\n{self.contact}")
        return "\n".join(lines)

    @staticmethod
    def _as_code_block(text: str, language: str = "bash") -> str:
        """Wrap installation-style text in a fenced code block, one command per line."""
        if not text:
            return ""
        return f"```{language}\n{text}\n```"

    def write(self, output_path: str = "readme.md") -> Path:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.build(), encoding="utf-8")
        return path

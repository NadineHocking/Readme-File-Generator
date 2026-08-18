from typing import Dict, List
from dataclasses import dataclass


@dataclass(frozen=True)
class License:
    # Represents a single license choice."""

    name: str
    badge_markdown: str
    footer_markdown: str


# Ordered mapping of the licenses offered in the dropdown/select prompt.
# "Name" is what the user sees; the License object carries the markdown
# snippets used later when the README is generated.
LICENSES: Dict[str, License] = {
    "MIT": License(
        name="MIT",
        badge_markdown="![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)",
        footer_markdown="This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).",
    ),
    "Apache License 2.0": License(
        name="Apache License 2.0",
        badge_markdown="![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)",
        footer_markdown="This project is licensed under the [Apache License 2.0](https://opensource.org/licenses/Apache-2.0).",
    ),
    "GNU GPLv3": License(
        name="GNU GPLv3",
        badge_markdown="![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)",
        footer_markdown="This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0).",
    ),
    "BSD 3-Clause": License(
        name="BSD 3-Clause",
        badge_markdown="![License: BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-orange.svg)",
        footer_markdown="This project is licensed under the [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause).",
    ),
    "Unlicense": License(
        name="Unlicense",
        badge_markdown="![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)",
        footer_markdown="This project is released into the public domain under [The Unlicense](https://unlicense.org/).",
    ),
    "None": License(
        name="None",
        badge_markdown="",
        footer_markdown="No license has been specified for this project.",
    ),
}


def license_choices() -> List[str]:
    return list(LICENSES.keys())


def get_license(name: str) -> License:
    return LICENSES.get(name, LICENSES["None"])
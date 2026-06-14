import re
import sys
from pathlib import Path

REQUIRED_FRONTMATTER = ["name:", "description:"]
REQUIRED_SECTIONS = [
    "Purpose",
    "When To Use",
    "When Not To Use",
    "Output Contract",
    "Style Rules",
]

NAME_RE = re.compile(r"^name:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$", re.MULTILINE)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_skill.py <skill_dir>")
        raise SystemExit(1)

    skill_dir = Path(sys.argv[1])
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        print("FAILED: missing SKILL.md")
        raise SystemExit(1)

    text = skill_file.read_text(encoding="utf-8")

    if not text.startswith("---"):
        print("FAILED: missing YAML frontmatter")
        raise SystemExit(1)

    for item in REQUIRED_FRONTMATTER:
        if item not in text:
            print(f"FAILED: missing frontmatter field: {item}")
            raise SystemExit(1)

    match = NAME_RE.search(text)
    if not match:
        print("FAILED: invalid skill name")
        raise SystemExit(1)

    name = match.group(1)
    if skill_dir.name != name:
        print(
            f"FAILED: directory name '{skill_dir.name}' does not match skill name '{name}'"
        )
        raise SystemExit(1)

    for section in REQUIRED_SECTIONS:
        if re.search(rf"^#+\s+{re.escape(section)}\s*$", text, re.MULTILINE) is None:
            print(f"FAILED: missing section: {section}")
            raise SystemExit(1)

    print("PASS")


if __name__ == "__main__":
    main()

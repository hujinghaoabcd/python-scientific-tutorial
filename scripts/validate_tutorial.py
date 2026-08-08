from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_DIRS = [
    "01-python",
    "02-numpy",
    "03-pandas",
    "04-scipy",
    "05-statsmodels",
    "06-linearmodels",
]

# These forms are deliberately excluded from the 2026 edition because the APIs
# are removed or no longer recommended for new tutorial code.
FORBIDDEN_PATTERNS = {
    "removed scipy.interpolate.interp2d": re.compile(r"\binterp2d\b"),
    "removed sklearn load_boston": re.compile(r"\bload_boston\b"),
    "removed pandas fillna(method=...)": re.compile(r"\.fillna\(\s*method\s*="),
    "removed pandas pd.np alias": re.compile(r"\bpd\.np\b"),
}


def check_structure() -> list[str]:
    errors: list[str] = []
    for dirname in EXPECTED_DIRS:
        if not (ROOT / dirname / "README.md").is_file():
            errors.append(f"missing module README: {dirname}/README.md")
    return errors


def check_notebooks() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.ipynb"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - validation should report all parse errors
            errors.append(f"invalid notebook JSON: {path.relative_to(ROOT)}: {exc}")
            continue
        if data.get("nbformat") not in {4}:
            errors.append(f"unexpected notebook format: {path.relative_to(ROOT)}")
    return errors


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    link_re = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    fenced_code = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        # Markdown-looking expressions inside code fences (e.g. con['fun'](x))
        # are source code, not hyperlinks.
        text = fenced_code.sub("", text)
        for raw in link_re.findall(text):
            target = raw.strip().split()[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "data:")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                continue
            if not resolved.exists():
                errors.append(f"broken link: {md.relative_to(ROOT)} -> {raw}")
    return errors


def check_forbidden_apis() -> list[str]:
    errors: list[str] = []
    for path in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.py")):
        if path == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{label}: {path.relative_to(ROOT)}")
    return errors


def main() -> int:
    checks = [
        check_structure,
        check_notebooks,
        check_markdown_links,
        check_forbidden_apis,
    ]
    errors: list[str] = []
    for check in checks:
        errors.extend(check())

    if errors:
        print("Tutorial validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    md_count = sum(1 for _ in ROOT.rglob("*.md"))
    nb_count = sum(1 for _ in ROOT.rglob("*.ipynb"))
    print(f"Tutorial validation passed: {md_count} Markdown files, {nb_count} notebooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

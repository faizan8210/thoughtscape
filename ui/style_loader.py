from pathlib import Path


def load_style(filename: str) -> str:
    style_path = Path(__file__).parent / "styles" / filename

    with open(style_path, "r", encoding="utf-8") as file:
        return file.read()
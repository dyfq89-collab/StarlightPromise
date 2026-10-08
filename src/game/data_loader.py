"""Loading helpers for the JSON-authored game content."""

import json
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_data(name: str) -> dict:
    with (DATA_DIR / name).open(encoding="utf-8") as source:
        return json.load(source)


"""JSON save handling kept separate from Kivy UI state."""

import json
from pathlib import Path


class SaveManager:
    def __init__(self, directory: Path | None = None) -> None:
        self.path = (directory or Path.home() / ".starlight_promise") / "save.json"

    def save(self, state: dict) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

    def load(self) -> dict | None:
        if not self.path.exists():
            return None
        return json.loads(self.path.read_text(encoding="utf-8"))


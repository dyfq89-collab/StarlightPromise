"""Definitions and inventory presentation helpers."""

from .data_loader import load_data


class ItemManager:
    def __init__(self) -> None:
        self.definitions = load_data("items.json")

    def display_name(self, item_id: str) -> str:
        return self.definitions.get(item_id, {}).get("name", item_id)


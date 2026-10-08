"""Data-driven maps, transitions and collision queries."""

from .data_loader import load_data


class MapManager:
    def __init__(self) -> None:
        self.maps = load_data("maps.json")
        self.current_map_id = "starlight_house"

    @property
    def current_map(self) -> dict:
        return self.maps[self.current_map_id]

    def change_map(self, map_id: str) -> tuple[int, int]:
        if map_id not in self.maps:
            raise KeyError(f"Unknown map: {map_id}")
        self.current_map_id = map_id
        return tuple(self.current_map["spawn"])

    def blocked_tiles(self) -> set[tuple[int, int]]:
        return {tuple(tile) for tile in self.current_map.get("blocked", [])}

    def events_at(self, position: tuple[int, int]) -> list[dict]:
        return [event for event in self.current_map.get("events", []) if tuple(event["position"]) == position]


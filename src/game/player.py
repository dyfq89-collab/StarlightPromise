"""Player state and grid movement for Starlight Promise."""

from dataclasses import dataclass, field


@dataclass
class Player:
    """A player positioned on the current tile map."""

    x: int = 1
    y: int = 3
    inventory: dict[str, int] = field(default_factory=dict)

    def position(self) -> tuple[int, int]:
        return self.x, self.y

    def move(self, direction: str, width: int, height: int, blocked: set[tuple[int, int]]) -> bool:
        deltas = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        if direction not in deltas:
            return False
        dx, dy = deltas[direction]
        target = self.x + dx, self.y + dy
        if not (0 <= target[0] < width and 0 <= target[1] < height) or target in blocked:
            return False
        self.x, self.y = target
        return True

    def add_item(self, item_id: str, amount: int = 1) -> None:
        self.inventory[item_id] = self.inventory.get(item_id, 0) + amount

    def has_item(self, item_id: str, amount: int = 1) -> bool:
        return self.inventory.get(item_id, 0) >= amount


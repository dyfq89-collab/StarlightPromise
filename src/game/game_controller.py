"""Coordinates player input, content events and persistence-ready state."""

from .item_manager import ItemManager
from .map_manager import MapManager
from .player import Player
from .quest_manager import QuestManager


class GameController:
    def __init__(self) -> None:
        self.map_manager = MapManager()
        self.player = Player(*self.map_manager.current_map["spawn"])
        self.quests = QuestManager()
        self.items = ItemManager()
        self.completed_events: set[str] = set()
        self.message = "夜晚的星光落在窗边。调查桌上的信件，开始这段旅程。"

    def move_player(self, direction: str) -> str:
        game_map = self.map_manager.current_map
        if not self.player.move(direction, game_map["width"], game_map["height"], self.map_manager.blocked_tiles()):
            self.message = "前方无法通行。"
            return self.message
        self._trigger_events()
        return self.message

    def _trigger_events(self) -> None:
        for event in self.map_manager.events_at(self.player.position()):
            event_id = event["id"]
            if event.get("once", True) and event_id in self.completed_events:
                continue
            kind = event["kind"]
            if kind == "item":
                self.player.add_item(event["item"])
                self.completed_events.add(event_id)
                self.message = event["text"]
                if event.get("start_quest"):
                    self.quests.start(event["start_quest"])
                if event.get("complete_quest"):
                    self.quests.complete(event["complete_quest"])
            elif kind == "transition" and self._requirements_met(event):
                self.player.x, self.player.y = self.map_manager.change_map(event["target"])
                self.message = event["text"]
            elif kind == "message":
                self.message = event["text"]
                if event.get("start_quest"):
                    self.quests.start(event["start_quest"])

    def _requirements_met(self, event: dict) -> bool:
        quest_id = event.get("requires_complete")
        return not quest_id or self.quests.status.get(quest_id) == QuestManager.COMPLETE

    def state(self) -> dict:
        return {"map_id": self.map_manager.current_map_id, "position": self.player.position(), "inventory": self.player.inventory, "quests": self.quests.status, "events": sorted(self.completed_events)}

    def restore(self, state: dict) -> None:
        """Restore validated JSON state created by :meth:`state`."""
        map_id = state.get("map_id", self.map_manager.current_map_id)
        if map_id in self.map_manager.maps:
            self.map_manager.current_map_id = map_id
        x, y = state.get("position", self.map_manager.current_map["spawn"])
        self.player.x, self.player.y = int(x), int(y)
        self.player.inventory = {str(key): int(value) for key, value in state.get("inventory", {}).items()}
        for quest_id, status in state.get("quests", {}).items():
            if quest_id in self.quests.status and status in {"available", "active", "complete"}:
                self.quests.status[quest_id] = status
        self.completed_events = set(state.get("events", []))
        self.message = "已读取你的星光旅程。"


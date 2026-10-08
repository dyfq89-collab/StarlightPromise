"""Quest lifecycle management."""

from .data_loader import load_data


class QuestManager:
    AVAILABLE = "available"
    ACTIVE = "active"
    COMPLETE = "complete"

    def __init__(self) -> None:
        self.definitions = load_data("quests.json")
        self.status = {quest_id: self.AVAILABLE for quest_id in self.definitions}

    def start(self, quest_id: str) -> None:
        if quest_id in self.definitions and self.status[quest_id] == self.AVAILABLE:
            self.status[quest_id] = self.ACTIVE

    def complete(self, quest_id: str) -> bool:
        if self.status.get(quest_id) != self.ACTIVE:
            return False
        self.status[quest_id] = self.COMPLETE
        return True

    def active_quest(self) -> tuple[str, dict] | None:
        for quest_id, status in self.status.items():
            if status == self.ACTIVE:
                return quest_id, self.definitions[quest_id]
        return None


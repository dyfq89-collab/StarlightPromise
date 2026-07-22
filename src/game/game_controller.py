from game.player import Player
from game.quest_manager import QuestManager
from game.story_manager import StoryManager
from game.npc_manager import NPCManager
from game.item_manager import ItemManager
from game.event_manager import EventManager
from game.map_manager import MapManager



class GameController:


    def __init__(self):

        self.player = Player()

        self.quest = QuestManager()

        self.story = StoryManager()

        self.npc = NPCManager()

        self.items = ItemManager()

        self.events = EventManager()
        
        self.map = MapManager()



    # 游戏开始

    def start_game(self):

        return self.story.get_story(
            "chapter1_start"
        )



    # 与NPC对话

    def talk_npc(self,npc_id):

        npc = self.npc.get_npc(
            npc_id
        )

        return npc["dialog"]



    # 接受任务

    def accept_first_quest(self):

        return self.quest.get_quest(
            "find_letter"
        )



    # 找到信件

    def find_letter(self):

        self.player.add_item(
            "old_letter"
        )

        self.quest.complete_quest(
            "find_letter"
        )


        return self.events.trigger(
            "old_letter_found"
        )
        
     def move_player(self,direction):


        self.player.move(direction)


        x,y = self.player.get_position()


        current_map = self.map.get_map()


        for obj in current_map["objects"].values():

            if obj["x"] == x and obj["y"] == y:

                return self.events.trigger(
                    obj["event"]
                )


        return (
            f"当前位置：{x},{y}"
        )

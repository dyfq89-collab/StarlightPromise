class QuestManager:


self.quests = {


    "first_meet":
    {
        "name":"寻找星光信件",
        "description":
        "在星光小屋寻找隐藏的信件。",
        "finished":False
    },


    "find_letter":
    {
        "name":"寻找旧信件",
        "description":
        "在星光小屋寻找隐藏的旧信件。",
        "finished":False
    },


    "memory_forest":
    {
        "name":"穿越回忆森林",
        "description":
        "找到森林深处的秘密。",
        "finished":False
    },


    "star_lake":
    {
        "name":"星光湖的约定",
        "description":
        "在星光湖完成最终约定。",
        "finished":False
    }

}



    def complete_quest(self,quest_id):

        if quest_id in self.quests:

            self.quests[quest_id]["finished"] = True



    def get_quest(self,quest_id):

        return self.quests.get(
            quest_id
        )



    def get_all_quests(self):

        return self.quests

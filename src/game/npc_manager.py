class NPCManager:


    def __init__(self):

        self.npcs = {


            "xiaoxing":

            {
                "name":"小星",

                "location":
                "star_light_house",

                "dialog":
                "请帮我寻找遗失的信件。"
            }


        }



    def get_npc(self,npc_id):

        return self.npcs.get(
            npc_id
        )

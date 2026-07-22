class EventManager:


    def __init__(self):

        self.events = {


            "old_letter_found":

            "你发现了一封旧信件，里面记录着重要的回忆。",



            "forest_secret":

            "你发现森林深处隐藏的星光碎片。",



            "final":

            "所有回忆汇聚成星光。"


        }



    def trigger(self,event):

        return self.events.get(
            event,
            ""
        )

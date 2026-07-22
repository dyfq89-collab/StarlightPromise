class DialogManager:


    def __init__(self):

        self.dialogs = {


            "start":

            "在一个星光闪耀的夜晚，"
            "一段重要的约定开始了。",



            "forest":

            "穿过森林，"
            "你找到了藏在回忆里的秘密。",



            "ending":

            "谢谢你一直陪伴在我的身边。"

        }



    def get_dialog(self,key):

        return self.dialogs.get(
            key,
            ""
        )

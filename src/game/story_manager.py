class StoryManager:


    def __init__(self):

        self.chapter = 1


        self.story = {


            "chapter1_start":

            """
            夜晚。

            天空中闪耀着无数星光。

            你来到了一座安静的小屋。

            这里藏着一段重要的回忆。
            """,



            "npc_star":

            """
            小星：

            好久不见。

            我一直在等待你的到来。

            可以帮我找回那封遗失的信吗？
            """,



            "letter_found":

            """
            你打开旧信件。

            里面写着：

            无论未来发生什么，
            请记得这片星空。

            """

        }



    def get_story(self,key):

        return self.story.get(
            key,
            ""
        )

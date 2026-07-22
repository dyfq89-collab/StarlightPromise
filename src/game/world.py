class World:


    def __init__(self):

        self.locations = {


            "star_light_house":
            {
                "name":"星光小屋",

                "description":
                "这里保存着许多珍贵的回忆。",

                "items":
                [
                    "old_letter"
                ]
            },


            "memory_forest":
            {
                "name":"回忆森林",

                "description":
                "森林里隐藏着过去的秘密。",

                "items":
                [
                    "star_fragment"
                ]
            },


            "star_light_lake":
            {
                "name":"星光湖",

                "description":
                "湖面倒映着满天星光。",

                "items":
                []
            }


        }



    def get_location(self,name):

        return self.locations.get(name)

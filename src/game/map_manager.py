class MapManager:


    def __init__(self):

        self.maps = {


            "star_light_house":
            {
                "name":"星光小屋",
                "description":
                "故事开始的地方。"
            },


            "star_light_village":
            {
                "name":"星光村",
                "description":
                "充满回忆的小村庄。"
            },


            "memory_forest":
            {
                "name":"回忆森林",
                "description":
                "隐藏着过去的秘密。"
            },


            "star_light_lake":
            {
                "name":"星光湖",
                "description":
                "可以看到最亮的星星。"
            },


            "star_garden":
            {
                "name":"星光花园",
                "description":
                "最终约定的地方。"
            }

        }


        self.current_map = "star_light_house"



    def change_map(self,map_id):

        if map_id in self.maps:

            self.current_map = map_id



    def get_current_map(self):

        return self.maps[self.current_map]

class MapManager:


    def __init__(self):

        self.current_map = "star_house"


        self.maps = {


            "star_house":
            {
                "name":"星光小屋",

                "width":5,

                "height":5,


                "objects":
                {

                    "desk":
                    {
                        "x":2,
                        "y":2,
                        "event":"find_letter"
                    },


                    "window":
                    {
                        "x":4,
                        "y":1,
                        "event":"look_star"
                    }

                }

            },


            "memory_forest":
            {
                "name":"回忆森林",

                "width":8,

                "height":8,


                "objects":
                {

                    "tree":
                    {
                        "x":5,
                        "y":5,
                        "event":"forest_memory"
                    }

                }

            }

        }



    def get_map(self):

        return self.maps[
            self.current_map
        ]



    def change_map(self,map_id):

        if map_id in self.maps:

            self.current_map = map_id

            return True


        return False

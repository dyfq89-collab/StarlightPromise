class MapManager:


    def __init__(self):


        self.current_map = "star_light_house"



        self.maps = {


            "star_light_house":
            {

                "name":"星光小屋",


                "width":5,

                "height":5,


                "objects":
                {


                    "old_letter":
                    {

                        "x":2,

                        "y":3,

                        "symbol":"📜",

                        "event":"find_letter"

                    },


                    "box":
                    {

                        "x":4,

                        "y":4,

                        "symbol":"📦",

                        "event":"open_box"

                    },


                    "window":
                    {

                        "x":1,

                        "y":1,

                        "symbol":"⭐",

                        "event":"look_star"

                    }

                }

            }

        }



    def get_map(self):

        return self.maps[
            self.current_map
        ]

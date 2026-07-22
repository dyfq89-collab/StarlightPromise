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

                        "tile":"letter",

                        "event":"old_letter_found"

                    },


                    "box":
                    {

                        "x":4,

                        "y":4,

                        "tile":"box",

                        "event":"open_box"

                    },


                    "window":
                    {

                        "x":1,

                        "y":1,

                        "tile":"star",

                        "event":"look_star"

                    }

                }

            }

        }



    def get_map(self):

        return self.maps[
            self.current_map
        ]

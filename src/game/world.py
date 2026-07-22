class World:


    def __init__(self):

        self.maps = {


            "star_light_forest":

            {

                "name":"星光森林",


                "width":5,

                "height":5,


                "objects":{


                    "old_letter":

                    {

                        "x":2,

                        "y":3,

                        "event":"find_letter"

                    },


                    "star_box":

                    {

                        "x":4,

                        "y":4,

                        "event":"open_box"

                    },


                    "star_tree":

                    {

                        "x":1,

                        "y":1,

                        "event":"look_star"

                    }


                }

            }


        }



    def get_map(self,map_id):

        return self.maps.get(map_id)

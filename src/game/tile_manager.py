class TileManager:

    def __init__(self):

        self.tiles = {

            "grass": {
                "name": "草地",
                "walkable": True,
                "image": "assets/grass.png"
            },


            "wall": {
                "name": "墙",
                "walkable": False,
                "image": "assets/wall.png"
            },


            "house": {
                "name": "房子",
                "walkable": False,
                "image": "assets/house.png"
            },


            "player": {
                "name": "玩家",
                "walkable": True,
                "image": "assets/player.png"
            },


            "letter": {
                "name": "信件",
                "walkable": True,
                "image": "assets/letter.png"
            },


            "box": {
                "name": "宝箱",
                "walkable": True,
                "image": "assets/box.png"
            },


            "star": {
                "name": "星光",
                "walkable": True,
                "image": "assets/star.png"
            }

        }


    def get_tile(self,tile_id):

        return self.tiles.get(
            tile_id,
            self.tiles["grass"]
        )


    def is_walkable(self,tile_id):

        tile = self.get_tile(tile_id)

        return tile["walkable"]

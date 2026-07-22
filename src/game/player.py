class Player:

    def __init__(self):

        self.name = "Traveler"

        # 玩家位置
        self.x = 0
        self.y = 0

        # 当前地图
        self.current_map = "star_light_house"

        # 背包
        self.inventory = []


    def move(self, direction):

        if direction == "up":
            self.y += 1

        elif direction == "down":
            self.y -= 1

        elif direction == "left":
            self.x -= 1

        elif direction == "right":
            self.x += 1



    def add_item(self,item):

        self.inventory.append(item)



    def remove_item(self,item):

        if item in self.inventory:
            self.inventory.remove(item)



    def has_item(self,item):

        return item in self.inventory


    def get_position(self):

        return (
            self.x,
            self.y
        )

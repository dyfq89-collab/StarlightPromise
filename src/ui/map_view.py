from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout



class MapView(GridLayout):


    def __init__(self, controller, **kwargs):

        super().__init__(**kwargs)


        self.controller = controller


        self.cols = 5
        self.rows = 5


        self.cells = []


        self.create_map()



    def create_map(self):


        for y in range(5):

            row=[]


            for x in range(5):

                cell = Image(
                   source="assets/grass.png",
                   allow_stretch=True,
                   keep_ratio=False
                )


                row.append(cell)

                self.add_widget(cell)


            self.cells.append(row)



        self.update_map()



    def update_map(self):


        # 清空

        for row in self.cells:

            for cell in row:

                cell.source="assets/grass.png"

        current_map = (
    self.controller.map.get_map()
)



for obj in current_map["objects"].values():


    x = obj["x"]

    y = obj["y"]


self.cells[y][x].source = self.get_image(obj["event"])



        # 获取玩家位置

# 获取玩家位置

x,y = self.controller.player.get_position()


if 0 <= x < self.cols and 0 <= y < self.rows:

    self.cells[y][x].source = "assets/player.png"



# 玩家脚下检测

for obj in current_map["objects"].values():

    if obj["x"] == x and obj["y"] == y:

        # 触发事件，不改变图片
        result = self.controller.events.trigger(
            obj["event"]
        )
        return result


def get_image(self,event):

    images = {

        "find_letter":
            "assets/letter.png",

        "old_letter_found":
            "assets/letter.png",

        "open_box":
            "assets/box.png",

        "look_star":
            "assets/star.png",

    }


    return images.get(
        event,
        "assets/grass.png"
    )

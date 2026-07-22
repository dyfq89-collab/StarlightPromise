from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image



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


    ox = obj["x"]

    oy = obj["y"]


    self.cells[y][x].source = (
    "assets/"
    + obj["symbol"]
    + ".png"
)



        # 获取玩家位置

# 获取玩家位置

x,y = self.controller.player.get_position()


if 0 <= x < self.cols and 0 <= y < self.rows:

    self.cells[y][x].text = "😊"



# 玩家脚下检测

for obj in current_map["objects"].values():

    if obj["x"] == x and obj["y"] == y:

        self.cells[y][x].text = "😊" + obj["symbol"]

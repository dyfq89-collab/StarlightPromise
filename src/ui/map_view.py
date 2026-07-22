from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label



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

                cell = Label(
                    text="·",
                    font_size=30
                )


                row.append(cell)

                self.add_widget(cell)


            self.cells.append(row)



        self.update_map()



    def update_map(self):


        # 清空

        for row in self.cells:

            for cell in row:

                cell.text="·"



        # 获取玩家位置

        x,y = self.controller.player.get_position()



        if x < 5 and y < 5:


            self.cells[y][x].text="😀"

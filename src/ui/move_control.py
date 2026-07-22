from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button



class MoveControl(GridLayout):


    def __init__(self, callback, **kwargs):

        super().__init__(**kwargs)


        self.cols = 3

        self.callback = callback



        # 空位置

        self.add_widget(Button(
            text=""
        ))


        up = Button(
            text="↑"
        )

        up.bind(
            on_press=lambda x:
            self.callback("up")
        )


        self.add_widget(up)



        self.add_widget(Button(
            text=""
        ))



        left = Button(
            text="←"
        )


        left.bind(
            on_press=lambda x:
            self.callback("left")
        )



        self.add_widget(left)



        down = Button(
            text="↓"
        )


        down.bind(
            on_press=lambda x:
            self.callback("down")
        )



        self.add_widget(down)



        right = Button(
            text="→"
        )


        right.bind(
            on_press=lambda x:
            self.callback("right")
        )


        self.add_widget(right)

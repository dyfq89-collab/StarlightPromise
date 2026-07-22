from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label



class BagScreen(Screen):


    def __init__(self,**kwargs):

        super().__init__(**kwargs)


        self.add_widget(
            Label(
                text=
                "背包\n\n暂无物品",
                font_size=30
            )
        )

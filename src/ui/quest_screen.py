from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label



class QuestScreen(Screen):


    def __init__(self,**kwargs):

        super().__init__(**kwargs)


        self.add_widget(
            Label(
                text=
                "任务\n\n"
                "寻找星光信件\n\n"
                "状态：进行中",
                font_size=30
            )
        )

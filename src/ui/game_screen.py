from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button



class GameScreen(Screen):


    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        self.layout = BoxLayout(
            orientation="vertical"
        )


        self.location = Label(
            text="星光小屋",
            font_size=35
        )


        self.info = Label(
            text=
            "这里保存着许多珍贵的回忆。",
            font_size=25
        )


        self.up = Button(
            text="↑"
        )


        self.down = Button(
            text="↓"
        )


        self.left = Button(
            text="←"
        )


        self.right = Button(
            text="→"
        )


        self.explore = Button(
            text="探索"
        )


        self.layout.add_widget(
            self.location
        )


        self.layout.add_widget(
            self.info
        )


        self.layout.add_widget(
            self.up
        )


        self.layout.add_widget(
            self.left
        )


        self.layout.add_widget(
            self.right
        )


        self.layout.add_widget(
            self.down
        )


        self.layout.add_widget(
            self.explore
        )


        self.add_widget(
            self.layout
        )

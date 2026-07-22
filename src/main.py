from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout



class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        layout = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=50
        )


        title = Label(
            text="🌌 星光之约\nStarlight Promise",
            font_size=40
        )


        start_button = Button(
            text="开始游戏",
            font_size=30
        )


        start_button.bind(
            on_press=self.start_game
        )


        layout.add_widget(title)

        layout.add_widget(start_button)


        self.add_widget(layout)



    def start_game(self, instance):

        self.manager.current="game"




class GameScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        self.add_widget(
            Label(
                text="欢迎来到星光世界\n寻找属于你的星光。",
                font_size=35
            )
        )




class StarlightPromiseApp(App):

    def build(self):

        sm = ScreenManager()


        sm.add_widget(
            MenuScreen(
                name="menu"
            )
        )


        sm.add_widget(
            GameScreen(
                name="game"
            )
        )


        return sm




if __name__=="__main__":

    StarlightPromiseApp().run()

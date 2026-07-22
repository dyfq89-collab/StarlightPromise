from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from ui.game_screen import GameScreen
from ui.bag_screen import BagScreen

from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout



class MenuScreen(Screen):


    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        layout = BoxLayout(
            orientation="vertical"
        )


        title = Label(
            text=
            "🌌 星光之约\n\nStarlight Promise",
            font_size=40
        )


        start = Button(
            text="开始旅程",
            font_size=30
        )


        start.bind(
            on_press=self.start_game
        )


        layout.add_widget(title)

        layout.add_widget(start)


        self.add_widget(layout)



    def start_game(self,instance):

        self.manager.current="game"





class StarlightPromiseApp(App):


    def build(self):


        manager = ScreenManager()


        manager.add_widget(
            MenuScreen(
                name="menu"
            )
        )


        manager.add_widget(
            GameScreen(
                name="game"
            )
        )


        manager.add_widget(
            BagScreen(
                name="bag"
            )
        )


        return manager




if __name__=="__main__":

    StarlightPromiseApp().run()

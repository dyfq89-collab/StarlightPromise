from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


# RPG系统导入

from game.player import Player
from game.map_manager import MapManager
from game.dialog_manager import DialogManager
from game.quest_manager import QuestManager
from game.item_manager import ItemManager
from game.save_manager import SaveManager



# 游戏核心

player = Player()

maps = MapManager()

dialogs = DialogManager()

quests = QuestManager()

items = ItemManager()

save = SaveManager()



class MenuScreen(Screen):


    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        layout = BoxLayout(
            orientation="vertical",
            spacing=20
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

        self.manager.current="story"




class StoryScreen(Screen):


    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        text = dialogs.get_dialog(
            "start"
        )


        self.add_widget(
            Label(
                text=text,
                font_size=30
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
            StoryScreen(
                name="story"
            )
        )


        return sm



if __name__=="__main__":

    StarlightPromiseApp().run()

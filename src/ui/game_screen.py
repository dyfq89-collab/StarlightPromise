from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from ui.move_control import MoveControl
from ui.map_view import MapView


from game.game_controller import GameController



class GameScreen(Screen):


    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        self.controller = GameController()


        self.layout = BoxLayout(
            orientation="vertical"
        )

        
        self.map_view = MapView(
            self.controller
        )


        self.layout.add_widget(
            self.map_view
        )


        self.title = Label(
            text="星光小屋",
            font_size=35
        )


        self.story = Label(
            text="",
            font_size=25
        )


        self.talk = Button(
            text="与小星对话"
        )


        self.quest = Button(
            text="接受任务"
        )


        self.find = Button(
            text="寻找信件"
        )


        self.talk.bind(
            on_press=self.talk_npc
        )


        self.quest.bind(
            on_press=self.accept_quest
        )


        self.find.bind(
            on_press=self.find_letter
        )


        self.layout.add_widget(
            self.title
        )


        self.layout.add_widget(
            self.story
        )


        self.layout.add_widget(
            self.talk
        )


        self.layout.add_widget(
            self.quest
        )


        self.layout.add_widget(
            self.find
        )

        
        self.move_control = MoveControl(
            self.move_player
        )
        

        self.layout.add_widget(
            self.move_control
        )
        

        self.add_widget(
            self.layout
        )


        # 开始剧情

        self.story.text = (
            self.controller.start_game()
        )



    def talk_npc(self,instance):

        self.story.text = (
            self.controller.talk_npc(
                "xiaoxing"
            )
        )



    def accept_quest(self,instance):

        quest = (
            self.controller.accept_first_quest()
        )


        self.story.text = (
            "任务："
            +
            quest["name"]
            +
            "\n"
            +
            quest["description"]
        )



    def find_letter(self,instance):

        result = (
            self.controller.find_letter()
        )


        self.story.text = result


        
def move_player(self,direction):


    result = self.controller.move_player(
        direction
    )


    self.map_view.update_map()


    self.story.text=result

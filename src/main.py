"""Android-friendly Kivy entry point for Starlight Promise."""

from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

from game.game_controller import GameController
from game.save_manager import SaveManager


class MenuScreen(Screen):
    def start(self) -> None:
        self.manager.current = "game"


class GameScreen(Screen):
    message = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = GameController()
        self.saves = SaveManager()
        root = BoxLayout(orientation="vertical", padding=dp(16), spacing=dp(8))
        self.map_name = Label(font_size="26sp", size_hint_y=None, height=dp(48))
        self.map_grid = GridLayout(cols=8, rows=6, spacing=dp(2), size_hint_y=0.55)
        self.message_label = Label(font_size="18sp", halign="center", valign="middle")
        self.message_label.bind(size=self._fit_message)
        root.add_widget(self.map_name)
        root.add_widget(self.map_grid)
        root.add_widget(self.message_label)
        root.add_widget(self._controls())
        save = Button(text="保存进度", size_hint_y=None, height=dp(42))
        save.bind(on_release=self.save_game)
        root.add_widget(save)
        back = Button(text="返回主菜单", size_hint_y=None, height=dp(48))
        back.bind(on_release=lambda *_: setattr(self.manager, "current", "menu"))
        root.add_widget(back)
        self.add_widget(root)
        self.refresh()

    def _controls(self) -> GridLayout:
        grid = GridLayout(cols=3, rows=2, size_hint_y=None, height=dp(160), spacing=dp(6))
        for text, direction in (("", None), ("↑", "up"), ("", None), ("←", "left"), ("↓", "down"), ("→", "right")):
            button = Button(text=text, disabled=direction is None)
            if direction:
                button.bind(on_release=lambda _, value=direction: self.move(value))
            grid.add_widget(button)
        return grid

    def _fit_message(self, widget, _size) -> None:
        widget.text_size = widget.size

    def move(self, direction: str) -> None:
        self.controller.move_player(direction)
        self.refresh()

    def refresh(self) -> None:
        self.map_name.text = self.controller.map_manager.current_map["name"]
        x, y = self.controller.player.position()
        self.message_label.text = f"{self.controller.message}\n\n位置：{x + 1}, {y + 1}"
        self.map_grid.clear_widgets()
        game_map = self.controller.map_manager.current_map
        event_positions = {tuple(event["position"]): "✦" for event in game_map["events"]}
        for row in range(game_map["height"]):
            for column in range(game_map["width"]):
                if (column, row) == (x, y):
                    text, color = "●", (0.98, 0.82, 0.35, 1)
                elif (column, row) in self.controller.map_manager.blocked_tiles():
                    text, color = "", (0.12, 0.15, 0.28, 1)
                else:
                    text, color = event_positions.get((column, row), ""), (0.12, 0.30, 0.36, 1)
                tile = Button(text=text, disabled=True, background_normal="", background_color=color)
                self.map_grid.add_widget(tile)

    def save_game(self, _button) -> None:
        self.saves.save(self.controller.state())
        self.controller.message = "旅程已保存。"
        self.refresh()


class StarlightPromiseApp(App):
    def build(self):
        manager = ScreenManager()
        menu = MenuScreen(name="menu")
        layout = BoxLayout(orientation="vertical", padding=dp(24), spacing=dp(16))
        layout.add_widget(Label(text="星光之约\nStarlight Promise", font_size="32sp"))
        start = Button(text="开始旅程", font_size="22sp", size_hint_y=None, height=dp(64))
        start.bind(on_release=lambda *_: menu.start())
        layout.add_widget(start)
        menu.add_widget(layout)
        manager.add_widget(menu)
        manager.add_widget(GameScreen(name="game"))
        return manager


if __name__ == "__main__":
    StarlightPromiseApp().run()


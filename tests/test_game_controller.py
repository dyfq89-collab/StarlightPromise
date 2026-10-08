from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from game.game_controller import GameController


def walk(game, *directions):
    for direction in directions:
        game.move_player(direction)


class GameControllerTests(unittest.TestCase):
    def test_letter_starts_and_completes_the_prologue(self):
        game = GameController()
        walk(game, "right", "right")
        self.assertTrue(game.player.has_item("old_letter"))
        self.assertEqual(game.quests.status["find_starlight"], "complete")

    def test_main_path_reaches_the_starlight_garden(self):
        game = GameController()
        walk(game, "right", "right", "right", "right", "right")
        self.assertEqual(game.map_manager.current_map_id, "starlight_village")

        walk(game, "up", "right", "right", "down", "right", "right", "right", "right")
        self.assertEqual(game.map_manager.current_map_id, "memory_forest")

        walk(game, "up", "right", "right", "down", "right", "right", "right", "right")
        self.assertEqual(game.map_manager.current_map_id, "starlight_lake")

        walk(game, "up", "right", "right", "down", "right", "right", "right", "right")
        self.assertEqual(game.map_manager.current_map_id, "starlight_garden")


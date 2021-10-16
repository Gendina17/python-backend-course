import unittest
from main import TicTacGame


class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame()

    def test_number_valid(self):
        self.assertTrue(self.game.validate_input('5'))

    def test_number_invalid_range(self):
        self.assertFalse(self.game.validate_input('456456'))

    def test_number_invalid_already_exist(self):
        self.game.numbers.append('4')
        self.assertIsNone(self.game.validate_input('4'))

    def test_number_invalid_str(self):
        with self.assertRaises(ValueError):
            self.game.validate_input('python very good')

    def test_check_winner_player1_victory(self):
        self.game.board = [["X", "X", "X"],
                           ["4", "O", "6"],
                           ["O", "8", "9"]]
        self.assert_(self.game.check_winner(), "X")

    def test_check_winner_draw(self):
        self.assertFalse(self.game.check_winner())

    def test_check_winner_none_victory(self):
        self.game.board = [["X", "O", "X"],
                           ["X", "X", "O"],
                           ["O", "X", "O"]]
        self.assertTrue(self.game.check_winner())

    def test_end_game(self):
        self.game.board = [["X", "O", "X"],
                           ["X", "X", "O"],
                           ["O", "X", "O"]]
        self.assert_(self.game.end_game(), "У вас ничья! Спасибо за игру!")


if __name__ == '__main__':
    unittest.main()

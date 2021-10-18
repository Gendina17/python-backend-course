import unittest
from main import TicTacGame


class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame()

    def test_number_valid(self):
        for i in range(1, 9):
            self.assertTrue(self.game.validate_input(str(i)))

    def test_number_invalid_range(self):
        self.assertFalse(self.game.validate_input('0'))
        self.assertFalse(self.game.validate_input('456456'))

    def test_number_invalid_already_exist(self):
        for i in range(1, 9):
            self.game.numbers.append('4')
            self.assertIsNone(self.game.validate_input('4'))

    def test_number_invalid_str(self):
        with self.assertRaises(ValueError):
            self.game.validate_input('python very good')

    def test_check_winner_player1_victory(self):
        self.game.board = [["X", "X", "X"],
                           ["4", "O", "6"],
                           ["O", "8", "9"]]
        self.assertTrue(self.game.check_winner(), "X")

        self.game.board = [["X", "O", "X"],
                           ["4", "X", "6"],
                           ["O", "8", "X"]]
        self.assertTrue(self.game.check_winner(), "X")

        self.game.board = [["X", "O", "X"],
                           ["X", "O", "6"],
                           ["X", "8", "9"]]
        self.assertTrue(self.game.check_winner(), "X")

    def test_check_winner_player2_victory(self):
        self.game.board = [["X", "X", "O"],
                           ["4", "O", "6"],
                           ["O", "8", "9"]]
        self.assertTrue(self.game.check_winner(), "O")

    def test_check_winner_none_victory(self):
        self.game.board = [["1", "O", "X"],
                           ["X", "5", "O"],
                           ["O", "X", "O"]]
        self.assertFalse(self.game.check_winner())

    def test_check_winner_draw(self):
        self.game.board = [["X", "O", "X"],
                           ["X", "X", "O"],
                           ["O", "X", "O"]]
        self.assertTrue(self.game.check_winner())


if __name__ == '__main__':
    unittest.main()

"""Игра Крестики Нолики"""

import re


class TicTacGame:

    """Класс реализации игры"""

    def __init__(self):
        self.numbers = []
        element = iter(list(range(1, 10)))
        self.board = [[next(element) for j in range(3)] for i in range(3)]

    def show_board(self):

        """Вывод игрового поля"""

        line_board = [elem for el in self.board for elem in el]
        print("""
        {} | {} | {}
        ----------
        {} | {} | {}
        ----------
        {} | {} | {}
        """.format(*line_board))

    def print_greeting(self):

        """Приветствие и ввод пользователей"""

        self.player_1 = input("Приветствуем вас в нашей супер игре КРЕСТИКИ НОЛИКИ!\n"
                              "Для начала введите имя первый игрок:  ")
        self.player_2 = input("Спасибо! Теперь второй: ")
        print("Перед вами игровое поле, для того чтобы сделать ход введите цифру!")
        self.moves = {'X': self.player_1, "O": self.player_2}

    def validate_input(self, number):

        """Валидация введенных данных"""

        if re.fullmatch(r'\d+', number):
            if number in self.numbers:
                return None
            if int(number) in range(1, 10):
                self.numbers.append(number)
                return True
            return False
        raise ValueError('invalid number')

    def start_game(self):

        """Основной ход игры"""

        current = "X"
        self.print_greeting()
        self.show_board()

        while not self.check_winner():
            number = input(f"\n{self.moves[current]}, сделайте пожалуйста ваш ход:  ")
            try:
                validation = self.validate_input(number)
                if validation is True:
                    number = int(number) - 1
                    self.board[number // 3][number % 3] = current
                    current = "O" if current == "X" else "X"
                    self.show_board()
                elif validation is None:
                    print("Данное число уже вводилось ранее, введите другое!")
                else:
                    print("Число должно быть в диапазоне от 1 до 10!")
            except ValueError:
                print("Введите, пожалуйста число!")
        self.end_game()

    def end_game(self):

        """Завершение игры"""

        step = self.check_winner()
        if step is True:
            print("У вас ничья! Спасибо за игру!")
            return True
        winner = self.moves[step]
        print(f"Игра окончена! победил(а) {winner}! ПОЗДРАВЛЯЕМ!!!!")

    def check_winner(self):

        """Определение победителя или ничьи"""

        main_diagonal = [self.board[i][i] for i in range(3)]
        side_diagonal = [self.board[i][2 - i] for i in range(3)]
        transposed_board = list(zip(*self.board))

        for row in self.board + transposed_board + [main_diagonal] + [side_diagonal]:
            if len(set(row)) == 1:
                return set(row).pop()

        values = [elem for el in self.board for elem in el]
        values = set(values)
        return values == {"X", "O"}


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()

import unittest
from main import calculating_distance
import random
import string


class TestCalculatingDistance(unittest.TestCase):
    def random_str(self):
        return ''.join(random.choices(string.ascii_lowercase, k=10))

    def test_equal_string(self):
        str = self.random_str()
        self.assertEqual(0, calculating_distance(str, str))

    def test_addition_to_the_second_word(self):
        str = self.random_str()
        self.assertEqual(1, calculating_distance(str, str + 'w'))
        self.assertEqual(1, calculating_distance(str, 'w' + str))
        self.assertEqual(3, calculating_distance(str, str + 'wer'))
        self.assertEqual(3, calculating_distance(str, 'wer' + str))

    def test_addition_to_the_first_word(self):
        str = self.random_str()
        self.assertEqual(1, calculating_distance(str + 'w', str))
        self.assertEqual(1, calculating_distance('w' + str, str))

    def test_adding_to_the_middle(self):
        str = 'qqqqq'
        str2 = 'qqwqq'
        self.assertEqual(1, calculating_distance(str, str2))
        str = 'qqqqq'
        str2 = 'wwwww'
        self.assertEqual(5, calculating_distance(str, str2))
        str = 'qqqqq'
        str2 = 'qqweq'
        self.assertEqual(2, calculating_distance(str, str2))

    def test_different_combinations(self):
        first = 'mama'
        second = 'mom'
        self.assertEqual(2, calculating_distance(first, second))
        first = 'd'
        second = 'ded'
        self.assertEqual(2, calculating_distance(first, second))
        first = 'pkokp'
        second = 'kok'
        self.assertEqual(2, calculating_distance(first, second))
        first = 'qwer'
        second = 'wer'
        self.assertEqual(1, calculating_distance(first, second))
        first = 'qwerty'
        second = 'awert'
        self.assertEqual(2, calculating_distance(first, second))

    def test_empty_string(self):
        str = self.random_str()
        self.assertEqual(len(str), calculating_distance('', str))


if __name__ == '__main__':
    unittest.main()

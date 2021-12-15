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

    def test_1end(self):
        str = self.random_str()
        self.assertEqual(1, calculating_distance(str, str+'w'))
        self.assertEqual(1, calculating_distance(str, 'w' + str))
        self.assertEqual(3, calculating_distance(str, str + 'wer'))
        self.assertEqual(3, calculating_distance(str, 'wer' + str))
    def test_1_beg(self):
        str = self.random_str()
        self.assertEqual(1, calculating_distance(str + 'w', str))
        self.assertEqual(1, calculating_distance('w' + str, str))

    def test_chan(self):
        str = 'qqqqq'
        str2 = 'qqwqq'
        self.assertEqual(1, calculating_distance(str, str2))
        str = 'qqqqq'
        str2 = 'wwwww'
        self.assertEqual(5, calculating_distance(str, str2))
        str = 'qqqqq'
        str2 = 'qqweq'
        self.assertEqual(2, calculating_distance(str, str2))

    def test_comb(self):
        a = 'mama'
        b = 'mom'
        c = 'd'
        e = 'ded'
        f = 'pkokp'
        t = 'kok'
        u = 'qwer'
        p = 'wer'
        o = 'qwerty'
        x = 'awert'
        self.assertEqual(2, calculating_distance(a, b))
        self.assertEqual(2, calculating_distance(c, e))
        self.assertEqual(2, calculating_distance(f, t))
        self.assertEqual(1, calculating_distance(u, p))
        self.assertEqual(2, calculating_distance(o, x))

if __name__ == '__main__':
    unittest.main()

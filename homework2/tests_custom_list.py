import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.long_custom_list = CustomList([i for i in range(6)])
        self.short_custom_list = CustomList([i for i in range(4, 8)])
        self.long_normal_list = CustomList([i for i in range(6)])
        self.short_normal_list = [i for i in range(4, 8)]

    def test_addition_long_custom_list_with_list(self):
        self.assertListEqual(self.long_custom_list + self.short_normal_list, [4, 6, 8, 10, 4, 5])

    def test_addition_short_custom_list_with_list(self):
        self.assertListEqual(self.short_custom_list + self.long_normal_list, [4, 6, 8, 10, 4, 5])

    def test_addition_equals_custom_list_and_list(self):
        self.assertListEqual(self.short_custom_list + self.short_normal_list, [8, 10, 12, 14])

    def test_addition_long_list_with_custom_list(self):
        self.assertListEqual(self.long_normal_list + self.short_custom_list, [4, 6, 8, 10, 4, 5])

    def test_addition_short_list_with_custom_list(self):
        self.assertListEqual(self.short_normal_list + self.long_custom_list, [4, 6, 8, 10, 4, 5])

    def test_addition_equals_list_and_custom_list(self):
        self.assertListEqual(self.short_normal_list + self.short_custom_list, [8, 10,12, 14])

    def test_addition_custom_list_with_custom_list(self):
        self.assertListEqual(self.long_custom_list + self.short_custom_list, [4, 6, 8, 10, 4, 5])

    def test_subtraction_long_custom_list_with_list(self):
        self.assertListEqual(self.long_custom_list - self.short_normal_list, [-4, -4, -4, -4, 4, 5])

    def test_subtraction_short_custom_list_with_list(self):
        self.assertListEqual(self.short_custom_list - self.long_normal_list, [4, 4, 4, 4, -4, -5])

    def test_subtraction_equals_custom_list_and_list(self):
        self.assertListEqual(self.short_custom_list - self.short_normal_list, [0, 0, 0, 0])

    def test_subtraction_long_list_with_custom_list(self):
        self.assertListEqual(self.long_normal_list - self.short_custom_list, [-4, -4, -4, -4, 4, 5])

    def test_subtraction_short_list_with_custom_list(self):
        self.assertListEqual(self.short_normal_list - self.long_custom_list, [4, 4, 4, 4, -4, -5])

    def test_subtraction_equals_list_and_custom_list(self):
        self.assertListEqual(self.short_normal_list - self.short_custom_list, [0, 0, 0, 0])

    def test_subtraction_custom_list_with_custom_list(self):
        self.assertListEqual(self.long_custom_list - self.short_custom_list, [-4, -4, -4, -4, 4, 5])

    def test_equals(self):
        self.assertTrue(self.long_custom_list == self.long_normal_list)
        self.assertFalse(self.long_custom_list == self.short_custom_list)

    def test_no_equals(self):
        self.assertFalse(self.long_custom_list != self.long_normal_list)
        self.assertTrue(self.long_custom_list != self.short_custom_list)

    def test_more(self):
        self.assertFalse(self.long_custom_list > self.long_normal_list)
        self.assertTrue(self.short_custom_list > self.long_custom_list)
        self.assertFalse(self.long_custom_list > self.short_normal_list)

    def test_less(self):
        self.assertFalse(self.long_custom_list < self.long_normal_list)
        self.assertFalse(self.short_custom_list < self.long_custom_list)
        self.assertTrue(self.long_custom_list < self.short_normal_list)

    def test_not_more(self):
        self.assertTrue(self.long_custom_list <= self.long_normal_list)
        self.assertFalse(self.short_custom_list <= self.long_custom_list)
        self.assertTrue(self.long_custom_list <= self.short_normal_list)

    def test_not_less(self):
        self.assertTrue(self.long_custom_list >= self.long_normal_list)
        self.assertTrue(self.short_custom_list >= self.long_custom_list)
        self.assertFalse(self.long_custom_list >= self.short_normal_list)
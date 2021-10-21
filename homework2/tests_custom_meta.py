import unittest
from custom_meta import CustomClass


class TestCustomMeta(unittest.TestCase):
    def setUp(self) -> None:
        self.custom = CustomClass()

    def test_invalid_instance_variable_name(self):
        with self.assertRaises(AttributeError):
            self.custom.val

    def test_valid_instance_variable_name(self):
        self.assertEqual(self.custom.custom_val, 99)

    def test_invalid_new_variable_name(self):
        self.custom.new_variable = 10000
        self.assertEqual(self.custom.custom_new_variable, 10000)

    def test_valid_new_instance_variable_name(self):
        self.custom.new_variable = 10000
        with self.assertRaises(AttributeError):
            self.custom.new_variable

    def test_wrong_class_variable_name_in_instance(self):
        with self.assertRaises(AttributeError):
            self.custom.x

    def test_wrong_class_variable_name(self):
        with self.assertRaises(AttributeError):
            CustomClass.x

    def test_correct_class_variable_name(self):
        self.assertEqual(self.custom.custom_x, 50)

    def test_valid_method_name(self):
        self.assertEqual(self.custom.custom_line(), 100)

    def test_invalid_method_name(self):
        with self.assertRaises(AttributeError):
            self.custom.line()

    def test_new_variable_in_metgod_valid(self):
        self.custom.custom_foo()
        self.assertEqual(self.custom.custom_val2, 123)

    def test_new_variable_in_metgod_invalid(self):
        self.custom.custom_foo()
        with self.assertRaises(AttributeError):
            self.custom.val2



import unittest
from string_calculator import add


class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(add("1,2,3,4"), 10)

    def test_newline_delimiters(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_negative_number(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2,3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2")

    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2,-3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -3")


if __name__ == "__main__":
    unittest.main()

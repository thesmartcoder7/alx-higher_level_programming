#!/usr/bin/python3

import unittest


# islower function test
class TestIsLower(unittest.TestCase):
    def test_islower(self):
        islower = __import__('7-islower').islower
        array = [
            "a is {}".format("lower" if islower("a") else "upper"),
            "H is {}".format("lower" if islower("H") else "upper"),
            "A is {}".format("lower" if islower("A") else "upper"),
            "3 is {}".format("lower" if islower("3") else "upper"),
            "g is {}".format("lower" if islower("g") else "upper"),
        ]

        expected = [
            "a is lower",
            "H is upper",
            "A is upper",
            "3 is upper",
            "g is lower",
        ]

        self.assertEqual(array, expected)


# to uppercase test
class TestUppercase(unittest.TestCase):
    def test_uppercase(self):
        uppercase = __import__('8-uppercase').uppercase

        sample = [
            uppercase("best"),
            uppercase("Best School 98 Battery street")
        ]

        expected = [
            "BEST",
            "BEST SCHOOL 98 BATTERY STREET"
        ]

        self.assertEqual(sample, expected)


# print last digit test
class TestPrintLastDigit(unittest.TestCase):
    def test_print_last_digit(self):
        print_last_digit = __import__('9-print_last_digit').print_last_digit

        digits = [
            print_last_digit(98),
            print_last_digit(0),
            print_last_digit(-1024),
        ]

        expected = [8, 0, 4]

        self.assertEqual(digits, expected)


if __name__ == "__main__":
    unittest.main()

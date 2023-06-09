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


# add test
class TestAdd(unittest.TestCase):
    def test_add(self):
        add = __import__('10-add').add

        result = [
            add(1, 2),
            add(98, 0),
            add(100, -2),
        ]

        expected = [3, 98, 98]

        self.assertEqual(result, expected)


# pow test
class TestPow(unittest.TestCase):
    def test_pow(self):
        pow = __import__('11-pow').pow

        result = [
            pow(2, 2),
            pow(98, 2),
            pow(98, 0),
            pow(100, -2),
            pow(-4, 5),
        ]

        expected = [4, 9604, 1, 0.0001, -1024]

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3

import unittest

islower = __import__('7-islower').islower


class TestIsLower(unittest.TestCase):
    def test_islower(self):
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


if __name__ == "__main__":
    unittest.main()

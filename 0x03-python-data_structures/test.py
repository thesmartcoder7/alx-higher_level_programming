#!/usr/bin/python3 


import unittest


# print integers test
class TestPrintListIntegers(unittest.TestCase):
    def test_print_list_integers(self):
        print_list = __import__("0-print_list_integer").print_list_integer 
        my_list = [1, 2, 3, 4, 5]
        result = print_list(my_list)

        self.assertEqual(my_list, result)



if __name__ == "__main__":
    unittest.main()

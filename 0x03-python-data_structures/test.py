#!/usr/bin/python3 


import unittest


# print integers test
class TestPrintListIntegers(unittest.TestCase):
    def test_print_list_integers(self):
        print_list = __import__("0-print_list_integer").print_list_integer 
        my_list = [1, 2, 3, 4, 5]
        result = print_list(my_list)

        self.assertEqual(my_list, result)



# find element at a specific index
class TestElementAt(unittest.TestCase):
    def test_element_at(self):
        element_at = __import__("1-element_at").element_at
        my_list = [1, 2, 3, 4, 5]
        idx = 3
        element = element_at(my_list, idx)

        self.assertEqual(element, 4)
        



if __name__ == "__main__":
    unittest.main()

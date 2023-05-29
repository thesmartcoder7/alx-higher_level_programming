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



# replace item in list
class TestReplaceInList(unittest.TestCase):
    def test_replace_at(self):
        replace_in_list = __import__('2-replace_in_list').replace_in_list

        my_list = [1, 2, 3, 4, 5]
        idx = 3
        new_element = 9
        new_list = replace_in_list(my_list, idx, new_element)
        expected_list = [1, 2, 3, 9, 5]

        self.assertEqual(new_list, expected_list)



# new in list test
class TestNewInList(unittest.TestCase):
    def test_new_in_list(self):
        new_in_list = __import__('4-new_in_list').new_in_list

        my_list = [1, 2, 3, 4, 5]
        idx = 3
        new_element = 9
        new_list = new_in_list(my_list, idx, new_element)

        self.assertIsInstance(new_list, list)
        self.assertListEqual(new_list, [1, 2, 3, 9, 5])



# remove character from list
class TestRemoveChar(unittest.TestCase):
    def test_remove_char(self):
        no_c = __import__('5-no_c').no_c

        result = [no_c("Best School"), no_c("Chicago"), no_c("C is fun!")]
        expected = [
            "Best Shool",
            "hiago",
            " is fun!"
        ]

        self.assertIsInstance(expected, list)
        self.assertEqual(result, expected)

        

# add tuple
class TestAddTuple(unittest.TestCase):
    def test_add_tuple(self):
        add_tuple = __import__('7-add_tuple').add_tuple

        tuple_a = (1, 89)
        tuple_b = (88, 11)
        new_tuple = add_tuple(tuple_a, tuple_b)

        self.assertIsInstance(new_tuple, tuple)
        self.assertEqual(new_tuple, (89,100))



# multiple returns
class TestMultipleReturn(unittest.TestCase):
    def test_multiple_returns(self):
        multiple_returns = __import__('8-multiple_returns').multiple_returns

        sentence = "At school, I learnt C!"
        length, first = multiple_returns(sentence)

        self.assertIsInstance(length, int)
        self.assertIsInstance(first, str)
        self.assertEqual((length, first), (22, "A"))



# return max integer from list
class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        max_integer = __import__('9-max_integer').max_integer

        my_list = [1, 90, 2, 13, 34, 5, -13, 3]
        max_value = max_integer(my_list)

        self.assertIsInstance(max_value, int)
        self.assertEqual(max_value, 90)



# delete at index 
class TestDeleteAtIndex(unittest.TestCase):
    def test_delete_at_index(self):
        delete_at = __import__('11-delete_at').delete_at

        my_list = [1, 2, 3, 4, 5]
        idx = 3
        new_list = delete_at(my_list, idx)
        expected = [1, 2, 3, 5]

        self.assertIsInstance(new_list, list)
        self.assertEqual(new_list, expected)






if __name__ == "__main__":
    unittest.main()

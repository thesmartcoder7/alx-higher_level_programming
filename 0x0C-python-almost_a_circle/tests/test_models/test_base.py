import unittest
import os, pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """
    Test class for Base class.
    """

    def setUp(self):
        """
        Set up method to reset the counter before each test.
        """
        Base._Base__nb_objects = 0

    def test_base_id_increment(self):
        """
        Test case to create new instances and check for id incrementation.
        """
        b0 = Base()
        self.assertEqual(b0.id, 1)

    def test_base_type_instance(self):
        """
        Test case to check the type and instance of Base object.
        """
        b0 = Base()
        self.assertEqual(type(b0), Base)
        self.assertTrue(isinstance(b0, Base))

    def test_to_json_string(self):
        """
        Test case for static method to_json_string.
        """
        d = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_d = Base.to_json_string([d])
        self.assertTrue(isinstance(d, dict))
        self.assertTrue(isinstance(json_d, str))
        self.assertCountEqual(json_d, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        json_d_1 = Base.to_json_string([])
        self.assertEqual(json_d_1, "[]")
        json_d_2 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")

    def test_to_json_string_wrong_types(self):
        """
        Test case for static method to_json_string with wrong types.
        """
        with self.assertRaises(TypeError) as x:
            Base.to_json_string(9)
        self.assertEqual("list_dictionaries must be a list of dictionaries", str(x.exception))
        # Add more tests for other types

    def test_to_json_string_wrong_args(self):
        """
        Test case for static method to_json_string with wrong number of arguments.
        """
        s1 = "to_json_string() missing 1 required positional argument: 'list_dictionaries'"
        with self.assertRaises(TypeError) as x:
            Base.to_json_string()
        self.assertEqual(s1, str(x.exception))
        # Add more tests for wrong number of arguments

    def test_save_to_file(self):
        """
        Test case for class method save_to_file with normal types.
        """
        r0 = Rectangle(10, 7, 2, 8)
        r1 = Rectangle(2, 4)
        Rectangle.save_to_file([r0, r1])
        # Add assertions for file existence and contents


    def test_save_to_file_empty(self):
        """
        Test case for class method save_to_file with empty list.
        """
        Rectangle.save_to_file([])
        # Add assertions for file existence and contents

    def test_create_rectangle(self):
        """
        Test case for class method create with Rectangle.
        """
        r_dict = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 8)

    class TestPEP8(unittest.TestCase):
        """Test class to check PEP8 validity of the code."""

    def test_pep8_conformance(self):
        """
        Test case to check if the code conforms to PEP8 style guidelines.
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py', 'models/rectangle.py', 'models/square.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")


if __name__ == '__main__':
    unittest.main()

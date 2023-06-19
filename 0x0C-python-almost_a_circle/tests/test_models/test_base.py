#!/usr/bin/python3
"""Unittest base.
Test cases for Base class.
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test class for Base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_instance(self):
        """Create new instances: check for id."""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_instance_type(self):
        """Test for type and instance."""
        b = Base()
        self.assertEqual(type(b), Base)
        self.assertTrue(isinstance(b, Base))

    def test_to_json_string_regular_dict(self):
        """Test static method to_json_string with regular dict."""
        d = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_d = Base.to_json_string([d])
        self.assertTrue(isinstance(d, dict))
        self.assertTrue(isinstance(json_d, str))
        self.assertCountEqual(
            json_d, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        json_d_1 = Base.to_json_string([])
        self.assertEqual(json_d_1, "[]")
        json_d_2 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")

    def test_to_json_string_wrong_args(self):
        """Test static method to_json_string with wrong number of args."""
        s1 = ("to_json_string() missing 1 required positional argument: "
              "'list_dictionaries'")
        with self.assertRaises(TypeError) as x:
            Base.to_json_string()
        self.assertEqual(s1, str(x.exception))
        s2 = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(s2, str(x.exception))

    def test_save_to_file_normal_types(self):
        """Test class method save_to_file with normal types."""
        r0 = Rectangle(10, 7, 2, 8)
        r1 = Rectangle(2, 4)
        Rectangle.save_to_file([r0, r1])
        res = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
               ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))
        Rectangle.save_to_file(None)
        res = "[]"
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)
        os.remove("Rectangle.json")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)
        s0 = Square(9, 3, 1, 12)
        s1 = Square(6, 7)
        Square.save_to_file([s0, s1])
        res = ('[{"id": 12, "size": 9, "y": 1, "x": 3},' +
               ' {"id": 1, "size": 6, "y": 0, "x": 7}]')
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), len(res))
        Square.save_to_file(None)
        res = "[]"
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)
        os.remove("Square.json")
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), res)

    def test_save_to_file_wrong_args(self):
        """Test class method save_to_file with wrong types of arguments."""
        s1 = ("save_to_file() missing 1 required positional argument: "
              "'list_objs'")
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file()
        self.assertEqual(s1, str(x.exception))
        s2 = "save_to_file() takes 2 positional arguments but 3 were given"
        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file([1, 2], [3, 4])
        self.assertEqual(s2, str(x.exception))

    def test_load_from_file(self):
        """Test class method load_from_file."""
        Rectangle.save_to_file([])
        list_objs_r = Rectangle.load_from_file()
        self.assertEqual(list_objs_r, [])
        Rectangle.save_to_file(None)
        list_objs_r = Rectangle.load_from_file()
        self.assertEqual(list_objs_r, [])
        r = Rectangle(3, 4)
        r.save_to_file([r])
        list_objs_r = Rectangle.load_from_file()
        self.assertEqual(len(list_objs_r), 1)
        self.assertIsInstance(list_objs_r[0], Rectangle)
        self.assertEqual(list_objs_r[0].width, 3)
        self.assertEqual(list_objs_r[0].height, 4)
        self.assertEqual(list_objs_r[0].x, 0)
        self.assertEqual(list_objs_r[0].y, 0)
        r = Rectangle(3, 4)
        r.save_to_file(None)
        list_objs_r = Rectangle.load_from_file()
        self.assertEqual(len(list_objs_r), 0)
        os.remove("Rectangle.json")
        Square.save_to_file([])
        list_objs_s = Square.load_from_file()
        self.assertEqual(list_objs_s, [])
        Square.save_to_file(None)
        list_objs_s = Square.load_from_file()
        self.assertEqual(list_objs_s, [])
        s = Square(3)
        s.save_to_file([s])
        list_objs_s = Square.load_from_file()
        self.assertEqual(len(list_objs_s), 1)
        self.assertIsInstance(list_objs_s[0], Square)
        self.assertEqual(list_objs_s[0].size, 3)
        self.assertEqual(list_objs_s[0].x, 0)
        self.assertEqual(list_objs_s[0].y, 0)
        s = Square(3)
        s.save_to_file(None)
        list_objs_s = Square.load_from_file()
        self.assertEqual(len(list_objs_s), 0)
        os.remove("Square.json")

    def test_load_from_file_csv(self):
        """Test class method load_from_file_csv."""
        Rectangle.save_to_file_csv([])
        list_objs_r = Rectangle.load_from_file_csv()
        self.assertEqual(list_objs_r, [])
        Rectangle.save_to_file_csv(None)
        list_objs_r = Rectangle.load_from_file_csv()
        self.assertEqual(list_objs_r, [])
        r = Rectangle(3, 4, 0, 0, 12)
        r.save_to_file_csv([r])
        list_objs_r = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_objs_r), 1)
        self.assertIsInstance(list_objs_r[0], Rectangle)
        self.assertEqual(list_objs_r[0].width, 3)
        self.assertEqual(list_objs_r[0].height, 4)
        self.assertEqual(list_objs_r[0].x, 0)
        self.assertEqual(list_objs_r[0].y, 0)
        self.assertEqual(list_objs_r[0].id, 12)
        r = Rectangle(3, 4, 0, 0, 12)
        r.save_to_file_csv(None)
        list_objs_r = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_objs_r), 0)
        os.remove("Rectangle.csv")
        Square.save_to_file_csv([])
        list_objs_s = Square.load_from_file_csv()
        self.assertEqual(list_objs_s, [])
        Square.save_to_file_csv(None)
        list_objs_s = Square.load_from_file_csv()
        self.assertEqual(list_objs_s, [])
        s = Square(3, 0, 0, 12)
        s.save_to_file_csv([s])
        list_objs_s = Square.load_from_file_csv()
        self.assertEqual(len(list_objs_s), 1)
        self.assertIsInstance(list_objs_s[0], Square)
        self.assertEqual(list_objs_s[0].size, 3)
        self.assertEqual(list_objs_s[0].x, 0)
        self.assertEqual(list_objs_s[0].y, 0)
        self.assertEqual(list_objs_s[0].id, 12)
        s = Square(3, 0, 0, 12)
        s.save_to_file_csv(None)
        list_objs_s = Square.load_from_file_csv()
        self.assertEqual(len(list_objs_s), 0)
        os.remove("Square.csv")


if __name__ == '__main__':
    unittest.main()

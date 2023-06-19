import unittest
import io, pycodestyle
import contextlib
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """Test Rectangle class: check for id assignment."""
        rect1 = Rectangle(1, 2)
        self.assertEqual(rect1.id, 1)

        rect2 = Rectangle(2, 3)
        self.assertEqual(rect2.id, 2)

        rect3 = Rectangle(3, 4)
        self.assertEqual(rect3.id, 3)

        rect4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect4.id, 12)

        rect5 = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(rect5.id, 34)

        rect6 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(rect6.id, -5)

        rect7 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(rect7.id, 9)

    def test_attributes(self):
        """Test Rectangle class: check for attribute values."""
        rect1 = Rectangle(10, 2)
        self.assertEqual(rect1.width, 10)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)

        rect2 = Rectangle(10, 2, 4, 5, 24)
        self.assertEqual(rect2.width, 10)
        self.assertEqual(rect2.height, 2)
        self.assertEqual(rect2.x, 4)
        self.assertEqual(rect2.y, 5)

    def test_missing_arguments(self):
        """Test Rectangle class: check for missing arguments."""
        with self.assertRaises(TypeError) as context:
            rect1 = Rectangle(5)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'", str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect2 = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments: 'width' and 'height'", str(context.exception))

    def test_inheritance(self):
        """Test Rectangle class: check for inheritance."""
        rect1 = Rectangle(9, 3)
        self.assertIsInstance(rect1, Base)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertNotIsInstance(Rectangle, Base)

    def test_wrong_attributes(self):
        """Test Rectangle class: check for wrong attributes."""
        with self.assertRaises(TypeError) as context:
            rect1 = Rectangle("Hello", 2)
        self.assertEqual("width must be an integer", str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect2 = Rectangle(2, "World")
        self.assertEqual("height must be an integer", str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect3 = Rectangle(1, 2, "Foo", 3)
        self.assertEqual("x must be an integer", str(context.exception))

        with self.assertRaises(TypeError) as context:
            rect4 = Rectangle(1, 2, 2, "Bar")
        self.assertEqual("y must be an integer", str(context.exception))

        with self.assertRaises(ValueError) as context:
            rect5 = Rectangle(0, 2)
        self.assertEqual("width must be > 0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            rect6 = Rectangle(2, 0)
        self.assertEqual("height must be > 0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            rect7 = Rectangle(2, -3)
        self.assertEqual("height must be > 0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            rect8 = Rectangle(2, 5, -5, 6)
        self.assertEqual("x must be >= 0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            rect9 = Rectangle(2, 8, 9, -65)
        self.assertEqual("y must be >= 0", str(context.exception))

    def test_area(self):
        """Test for public method area with normal types."""
        rect1 = Rectangle(3, 2)
        self.assertEqual(rect1.area(), 6)

        rect2 = Rectangle(75, 2)
        self.assertEqual(rect2.area(), 150)

        rect3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rect3.area(), 56)

    def test_area_wrong_args(self):
        """Test for public method area with wrong args."""
        rect1 = Rectangle(3, 2)
        with self.assertRaises(TypeError) as context:
            rect1.area("Hello")
        self.assertEqual(
            "area() takes 1 positional argument but 2 were given", str(context.exception))

    def test_display(self):
        """Test for public method display."""
        f = io.StringIO()
        rect1 = Rectangle(4, 5)
        with contextlib.redirect_stdout(f):
            rect1.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n####\n"
        self.assertEqual(s, res)

    def test_display_wrong_args(self):
        """Test for public method display with wrong args."""
        rect1 = Rectangle(9, 6)
        with self.assertRaises(TypeError) as context:
            rect1.display(9)
        self.assertEqual(
            "display() takes 1 positional argument but 2 were given", str(context.exception))

    def test_to_string(self):
        """Test for __str__ representation."""
        f = io.StringIO()
        rect1 = Rectangle(4, 6, 2, 1, 12)
        with contextlib.redirect_stdout(f):
            print(rect1)
        s = f.getvalue()
        res = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(s, res)

    def test_display_with_x_and_y(self):
        """Test for public method display with x and y."""
        f = io.StringIO()
        rect1 = Rectangle(2, 3, 2, 2)
        with contextlib.redirect_stdout(f):
            rect1.display()
        s = f.getvalue()
        res = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, res)

    def test_update(self):
        """Test for public method update."""
        rect1 = Rectangle(10, 10, 10, 10)
        rect1.update(89)
        self.assertEqual(rect1.id, 89)

        rect1.update(89, 2)
        self.assertEqual(rect1.width, 2)

        rect1.update(89, 2, 3)
        self.assertEqual(rect1.height, 3)

        rect1.update(89, 2, 3, 4)
        self.assertEqual(rect1.x, 4)

        rect1.update(89, 2, 3, 4, 5)
        self.assertEqual(rect1.y, 5)

        rect1.update()
        self.assertEqual(str(rect1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_with_kwargs(self):
        """Test for public method update with kwargs."""
        rect1 = Rectangle(10, 10, 10, 10)
        rect1.update(height=1)
        self.assertEqual(rect1.height, 1)

        rect1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(rect1.y, 3)
        self.assertEqual(rect1.width, 4)
        self.assertEqual(rect1.x, 1)
        self.assertEqual(rect1.height, 2)

    def test_to_dictionary(self):
        """Test for public method to_dictionary."""
        rect1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = rect1.to_dictionary()
        r_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(len(r1_dictionary), len(r_dictionary))
        self.assertEqual(type(r1_dictionary), dict)

        rect2 = Rectangle(1, 1)
        rect2.update(**r1_dictionary)
        r2_dictionary = rect2.to_dictionary()
        self.assertEqual(len(r1_dictionary), len(r2_dictionary))
        self.assertEqual(type(r2_dictionary), dict)
        self.assertFalse(rect1 == rect2)

    def test_to_dictionary_wrong_args(self):
        """Test for public method to_dictionary with wrong args."""
        with self.assertRaises(TypeError) as context:
            rect1 = Rectangle(10, 2, 1, 9)
            rect1.to_dictionary("Hi")
        self.assertEqual(
            "to_dictionary() takes 1 positional argument but 2 were given", str(context.exception))

    class TestPEP8(unittest.TestCase):
        """Test class to check PEP8 validity of the code."""

    def test_pep8_conformance(self):
        """
        Test case to check if the code conforms to PEP8 style guidelines.
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(
            ['models/base.py', 'models/rectangle.py', 'models/square.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")


if __name__ == '__main__':
    unittest.main()

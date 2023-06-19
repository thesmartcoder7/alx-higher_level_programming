#!/usr/bin/python3
"""
This module provides the Rectangle class, a subclass of the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle and inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's
            position. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's
            position. Defaults to 0.
            id (int, optional): The ID of the rectangle. Defaults to None.
        """
        super().__init__(id)

        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, param):
        """
        Sets the width of the rectangle.

        Args:
            param (int): The new width of the rectangle.
        """
        self.check_integer_parameter(param, 'width')

        self.__width = param

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, param):
        """
        Sets the height of the rectangle.

        Args:
            param (int): The new height of the rectangle.
        """
        self.check_integer_parameter(param, 'height')

        self.__height = param

    @property
    def x(self):
        """
        Gets the x-coordinate of the rectangle's position.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, param):
        """
        Sets the x-coordinate of the rectangle's position.

        Args:
            param (int): The new x-coordinate of the rectangle's position.
        """
        self.check_integer_parameter(param, 'x')

        self.__x = param

    @property
    def y(self):
        """
        Gets the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, param):
        """
        Sets the y-coordinate of the rectangle's position.

        Args:
            param (int): The new y-coordinate of the rectangle's position.
        """
        self.check_integer_parameter(param, 'y')

        self.__y = param

    def check_integer_parameter(self, value, param):
        """
        Checks if the given value is a valid integer parameter.

        Args:
            value (any): The value to be checked.
            param (str): The parameter name.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not within the
            valid range for the parameter.
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle by printing it as a series of '#' characters.
        """
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Args:
            *args (any): Variable length argument list.
            **kwargs (any): Arbitrary keyword arguments.
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.

        Returns:
            dict: The dictionary representation of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

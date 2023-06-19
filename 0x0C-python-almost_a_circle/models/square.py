#!/usr/bin/python3
"""
This module provides the Square class, a subclass of the Rectangle class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a square and inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's
            position. Defaults to 0.
            y (int, optional): The y-coordinate of the square's
            position. Defaults to 0.
            id (int, optional): The ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.

        Args:
            *args (any): Variable length argument list.
            **kwargs (any): Arbitrary keyword arguments.
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for key, value in kwargs.items():
                if key in modif_attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
            dict: The dictionary representation of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

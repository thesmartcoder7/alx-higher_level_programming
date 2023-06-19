#!/usr/bin/python3
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Represents a square shape.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate of the square's
             position. Defaults to 0.
            y (int, optional): Y-coordinate of the square's
             position. Defaults to 0.
            id (int, optional): Unique ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: String representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Size property of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size property of the square.

        Args:
            value (int): New value for the size.

        Raises:
            ValueError: If the value is not greater than 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the square's attributes with the provided arguments.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Raises:
            TypeError: If the number of arguments is not between 1 and 4.
            KeyError: If an invalid attribute name is provided.
        """
        if len(args) > 4:
            error = """
            Square.update() takes 1 to 4 keyword,
             or 1 to 4 non-keyword arguments
            """
            raise TypeError(error)
        for i, arg in enumerate(args):
            if i == 0:
                if self.id != arg:
                    temp = self.id
                    self.id = arg
                    Base._Base__assigned_ids.remove(temp)
                    Base._Base__assigned_ids.add(arg)
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg
        if args and len(args) <= 4:
            return
        if not args and not kwargs:
            error = """
            Square.update() takes 1 to 4 keyword,
             or 1 to 4 non-keyword arguments
            """
            raise TypeError(error)
        for key, value in kwargs.items():
            if key == 'id':
                if self.id != value:
                    temp = self.id
                    self.id = value
                    Base._Base__assigned_ids.remove(temp)
                    Base._Base__assigned_ids.add(value)
            elif key == 'size':
                self.size = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value
            else:
                raise KeyError(f"Invalid attribute name: {key}")

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
            dict: Dictionary representation of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }

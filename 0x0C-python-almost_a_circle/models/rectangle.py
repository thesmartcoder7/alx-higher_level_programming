#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    Represents a rectangle shape.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the rectangle's
            position. Defaults to 0.
            y (int, optional): Y-coordinate of the rectangle's
            position. Defaults to 0.
            id (int, optional): Unique ID of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate_integer(self, attr, value):
        """
        Validates that the given value is an integer and satisfies
        specific conditions.

        Args:
            attr (str): Attribute name being validated.
            value (int): Value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value does not satisfy the specified conditions.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attr} must be an integer")
        if attr in ('width', 'height') and value <= 0:
            raise ValueError(f"{attr} must be > 0")
        elif attr in ('x', 'y') and value < 0:
            raise ValueError(f"{attr} must be >= 0")

    @property
    def width(self):
        """
        Width property of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width property of the rectangle.

        Args:
            value (int): New value for the width.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        self.validate_integer('width', value)
        self.__width = value

    @property
    def height(self):
        """
        Height property of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height property of the rectangle.

        Args:
            value (int): New value for the height.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        self.validate_integer('height', value)
        self.__height = value

    @property
    def x(self):
        """
        X-coordinate property of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x-coordinate property of the rectangle's position.

        Args:
            value (int): New value for the x-coordinate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than or equal to 0.
        """
        self.validate_integer('x', value)
        self.__x = value

    @property
    def y(self):
        """
        Y-coordinate property of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y-coordinate property of the rectangle's position.

        Args:
            value (int): New value for the y-coordinate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than or equal to 0.
        """
        self.validate_integer('y', value)
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Displays the rectangle by printing its representation
        using '#' characters.
        The position and dimensions of the rectangle are
        taken into account.
        """
        display = '\n' * self.y + \
            '\n'.join([' ' * self.x + '#' * self.width] * self.height)
        print(display)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        x, y = self.x, self.y
        w, h = self.width, self.height

        return f"[Rectangle] ({self.id}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Args:
            *args: Non-keyword arguments representing the attributes
            in the following order:
                - ID
                - Width
                - Height
                - X-coordinate
                - Y-coordinate
            **kwargs: Keyword arguments representing the attributes with
            their corresponding values.

        Raises:
            TypeError: If the number of arguments is greater than 5 or no
            valid arguments are provided.
            KeyError: If an invalid attribute name is specified.
        """
        if len(args) > 5:
            error = """Rectangle.update() takes 1 to 5 keyword,
             or 1 to 5 non-keyword arguments"""
            raise TypeError(error)
        for i, arg in enumerate(args):
            if i == 0:
                if self.id != arg:
                    self.id = arg
                    Base._Base__assigned_ids.add(arg)
            elif i == 1:
                self.width = arg
            elif i == 2:
                self.height = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg
        if args and len(args) <= 5:
            return
        if not args and not kwargs:
            error = """Rectangle.update() takes 1 to 5 keyword,
             or 1 to 5 non-keyword arguments"""
            raise TypeError(error)
        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
                Base._Base__assigned_ids.add(value)
            elif key == 'width':
                self.width = value
            elif key == 'height':
                self.height = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value
            else:
                raise KeyError(f"Invalid attribute name: {key}")

    def to_dictionary(self):
        """
        Converts the rectangle object into a dictionary representation.

        Returns:
            dict: Dictionary representation of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }

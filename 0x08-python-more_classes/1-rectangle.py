#!/usr/bin/python3
"""
A module with a Rectangle that does nothing
"""


class Rectangle:
    """
        An empty Rectangle class
    """

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """
            Checks the parameters and initializes some values.

            Arguments:
                width: The width of the Rectangle.
                height: The height of the Rectangle.
        """

        self.__check_valid_width(width)
        self.__check_valid_height(height)

        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """
            Returns the width of the Rectangle
        """

        return self.__width

    @width.setter
    def width(self, value) -> None:
        """
            Checks the parameters and set the size of the Rectangle.

            Arguments:
                value (int): The width of the Rectangle.

            Raises:
                TypeError: If `value` type is not `int`.
                ValueError: If `value` is less than `0`.
        """

        self.__check_valid_width(value)
        self.__width = value

    @property
    def height(self) -> None:
        """
        Returns the width of the Rectangle
        """

        return self.__height

    @height.setter
    def height(self, value) -> None:
        """
            Checks the parameters and set the size of the Rectangle.

            Arguments:
                value (int): The height of the Rectangle.

            Raises:
                TypeError: If `value` type is not `int`.
                ValueError: If `value` is less than `0`.
        """

        self.__check_valid_height(value)
        self.__height = value

    def __check_valid_width(self, width) -> bool:
        """
            Checks if the width is a valid integer.

            Arguments:
                width (int): The width of the Rectangle.

            Raises:
                TypeError: If `width` type is not an integer.
                ValueError: If `width` is less than `0`.
        """

        if self.__check_int_value(width) is False:
            raise TypeError('width must be an integer')

        if self.__check_positive_value(width) is False:
            raise ValueError('width must be >= 0')

    def __check_valid_height(self, height) -> bool:
        """
            Checks if the height is a valid integer.

            Arguments:
                height (int): The height of the Rectangle.

            Raises:
                TypeError: If `height` type is not an integer.
                ValueError: If `height` is less than `0`.
        """

        if self.__check_int_value(height) is False:
            raise TypeError('height must be an integer')

        if self.__check_positive_value(height) is False:
            raise ValueError('height must be >= 0')

    def __check_int_value(self, value) -> bool:
        """
            Checks if the value is an integer.

            Arguments:
                value (int): The number to verify

            Returns:
                int: If is a int `True`, `False` otherwise.
        """

        if type(value) is int:
            return True

        return False

    def __check_positive_value(self, value: int) -> bool:
        """
            Checks if the value is a positive integer.

            Arguments:
                value (int): The number to verify

            Returns:
                int: `True` If value is greater than
                or equal to 0, `False` otherwise.
        """

        if value >= 0:
            return True

        return False

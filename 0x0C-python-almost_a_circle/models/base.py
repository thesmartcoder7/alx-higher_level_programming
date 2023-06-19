#!/usr/bin/python3

"""
This module provides a Base class and its related
methods for managing objects.
"""

import json
import csv


class Base:
    """
    The Base class serves as the foundation for managing
    objects and provides various utility methods.
    """

    __nb_objects = 0
    __true_nb_objects = 0
    __assigned_ids = set()

    def __init__(self, id=None):
        """
        Initializes a Base object with an optional ID.
        If ID is not provided, a unique ID is assigned.

        Args:
            id (int, optional): The ID of the object.
            Defaults to None.
        """
        if id is not None:
            self.id = id
            Base.__true_nb_objects += 1
            self.serial = Base.__true_nb_objects
            Base.__assigned_ids.add(self.id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            Base.__true_nb_objects += 1
            self.serial = Base.__true_nb_objects
            Base.__assigned_ids.add(self.id)

    @property
    def id(self):
        """
        Get the ID of the object.

        Returns:
            int: The ID of the object.
        """
        return self.__id

    @id.setter
    def id(self, value):
        """
        Set the ID of the object.

        Args:
            value (int): The ID value to set.

        Raises:
            ValueError: If the ID value is not positive.
        """
        if value < 1:
            raise ValueError('id must be positive')
        self.__id = value

    @property
    def serial(self):
        """
        Get the serial number of the object.

        Returns:
            int: The serial number of the object.
        """
        return self.__serial

    @serial.setter
    def serial(self, value):
        """
        Set the serial number of the object.

        Args:
            value (int): The serial number value to set.
        """
        self.__serial = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): The list of dictionaries to convert.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): The list of objects to save.
        """
        list_objs = [] if list_objs is None else list_objs
        list_dicts = [item.to_dictionary() for item in list_objs]
        json_dict = cls.to_json_string(list_dicts)
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_dict)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): The JSON string to convert.

        Returns:
            list: The list of dictionaries.
        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an object based on a dictionary of attributes.

        Args:
            **dictionary: The dictionary containing the
            attributes of the object.

        Returns:
            Base: The created object.
        """
        if cls.__name__ == 'Rectangle':
            temp = cls(1, 1)
        elif cls.__name__ == 'Square':
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """
        Load a list of objects from a JSON file.

        Returns:
            list: The list of loaded objects.
        """
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                json_str = file.read()
                obj_list = cls.from_json_string(json_str)
                instance_list = [cls.create(**item) for item in obj_list]
                return instance_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a CSV file.

        Args:
            list_objs (list): The list of objects to save.
        """
        list_objs = [] if list_objs is None else list_objs
        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')
        list_dicts = [item.to_dictionary() for item in list_objs]
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', encoding='utf-8') as file:
            csv_writer = csv.DictWriter(file, keys)
            csv_writer.writeheader()
            csv_writer.writerows(list_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of objects from a CSV file.

        Returns:
            list: The list of loaded objects.
        """
        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                instance_list = []
                for row in csv_reader:
                    for key in keys:
                        row[key] = int(row[key])
                    instance_list.append(cls.create(**row))
                return instance_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw a list of rectangles and squares using turtle graphics.

        Args:
            list_rectangles (list): The list of rectangles to draw.
            list_squares (list): The list of squares to draw.
        """
        import turtle
        import time
        from random import randrange

        t = turtle.Turtle()
        t.color("beige")
        turtle.bgcolor("violet")
        t.shape("square")
        t.pensize(8)

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """
        Draw a rectangle using turtle graphics.

        Args:
            t (Turtle): The turtle object for drawing.
            rect (Rectangle or Square): The rectangle or square
            object to draw.
        """
        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)

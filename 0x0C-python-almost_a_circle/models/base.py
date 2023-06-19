#!/usr/bin/python3

import json
import os
import csv


class Base:
    """Base class for other classes in the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of a Base instance.

        Args:
            - id: id of the instance (default is None)
        Raises:
            - TypeError: If id is not an integer
        """
        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON representation of list_dictionaries.

        Args:
            - list_dictionaries: list of dictionaries
        Returns:
            - JSON representation of the list
        Raises:
            - TypeError: If list_dictionaries is not a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            - list_objs: list of instances that inherit from Base
        """
        if list_objs is None or list_objs == []:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries from the JSON string representation.

        Args:
            - json_string: string to convert to a list
        Returns:
            - List of dictionaries
        Raises:
            - TypeError: If json_string is not a string
        """
        result = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            result = json.loads(json_string)
        return result

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            - dictionary: used as **kwargs
        Returns:
            - Instance created
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.

        Returns:
            - List of instances
        """
        filename = cls.__name__ + ".json"
        result = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    result.append(cls.create(**d))
        return result

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs in CSV format and saves it to a file.

        Args:
            - list_objs: list of instances that inherit from Base
        Raises:
            - TypeError: If list_objs is not a list of instances
        """
        if (type(list_objs) != list and
           list_objs is not None or
           not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes a CSV file and returns a list of instances.

        Returns:
            - List of instances
        """
        filename = cls.__name__ + ".csv"
        result = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        result.append(i)
        return result

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws the rectangles and squares using the turtle module.

        Args:
            - list_rectangles: list of Rectangle instances
            - list_squares: list of Square instances
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
        Draws a rectangle using the turtle module.

        Args:
            - t: turtle object
            - rect: Rectangle instance
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

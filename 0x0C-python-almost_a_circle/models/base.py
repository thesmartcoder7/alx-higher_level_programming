#!/usr/bin/python3
from os import path
import json
import csv

"""
This module provides a Base class for object manipulation and drawing.
"""


class Base:
    """
    The Base class represents the base object with common functionalities.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The ID of the instance (optional). If not provided,
                      the ID is automatically assigned.

        Attributes:
            id (int): The ID of the instance.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.

        Raises:
            TypeError: If list_dictionaries is not a list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        if not isinstance(list_dictionaries, list) or not all(isinstance(x, dict) for x in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances to be saved.
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
        Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): The JSON string to be converted.

        Returns:
            list: The list of dictionaries represented by the JSON string.
        """
        l = []
        if json_string is not None and json_string != '':
            if not isinstance(json_string, str):
                raise TypeError("json_string must be a string")
            l = json.loads(json_string)
        return l

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of the class based on a dictionary of attributes.

        Args:
            dictionary (dict): The dictionary of attributes.

        Returns:
            object: The newly created instance of the class.
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
        Loads objects from a JSON file and creates instances of the class.

        Returns:
            list: The list of instances created from the JSON file.
        """
        filename = cls.__name__ + ".json"
        l = []
        list_dicts = []
        if path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    l.append(cls.create(**d))
        return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the CSV representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances to be saved.
        """
        if not isinstance(list_objs, list) or (list_objs is not None and not all(isinstance(x, cls) for x in list_objs)):
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
        Loads objects from a CSV file and creates instances of the class.

        Returns:
            list: The list of instances created from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        l = []
        if path.exists(filename):
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
                        l.append(i)
        return l

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws rectangles and squares using the turtle graphics module.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.
        """
        import turtle

        # Calculate the screen size
        screen_width = 620
        padding = 10
        row_width = padding
        row_height = 0
        screen_height = padding
        color_list = ['red', 'orange', 'yellow',
                      'green', 'blue', 'indigo', 'violet']
        color_size = len(color_list)
        color_index = 0

        # Calculate the required screen dimensions based on the objects
        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if row_width == padding or potential_width < screen_width:
                row_width += rect.width + rect.x + padding
                if row_height < rect.height + rect.y:
                    row_height = rect.height + rect.y
            else:
                screen_height += row_height + padding
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y

        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if row_width == padding or potential_width < screen_width:
                row_width += square.size + square.x + padding
                if row_height < square.size + square.y:
                    row_height = square.size + square.y
            else:
                screen_height += row_height + padding
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y

        # Set up the turtle graphics window
        turtle.screensize(canvwidth=screen_width, canvheight=screen_height)
        turtle.pu()
        turtle.left(180)
        turtle.forward(screen_width / 2 - padding)
        turtle.right(90)
        turtle.forward(screen_height / 2 - padding)
        turtle.right(90)
        row_width = padding
        row_height = 0

        # Draw the rectangles
        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if row_width == padding or potential_width < screen_width:
                row_width += rect.width + rect.x + padding
                if row_height < rect.height + rect.y:
                    row_height = rect.height + rect.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(rect.x)
            turtle.right(90)
            turtle.forward(rect.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(rect.width + padding)
            turtle.left(90)
            turtle.forward(rect.y)
            turtle.right(90)

        # Draw the squares
        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if row_width == padding or potential_width < screen_width:
                row_width += square.size + square.x + padding
                if row_height < square.size:
                    row_height = square.size + square.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(square.x)
            turtle.right(90)
            turtle.forward(square.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(square.size + padding)
            turtle.left(90)
            turtle.forward(square.y)
            turtle.right(90)

        turtle.getscreen()._root.mainloop()

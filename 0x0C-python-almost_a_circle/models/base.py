#!/usr/bin/python3

"""

Base class for managing id attribute in future classes.
"""

import csv
import json


class Base:
    """

    Base class for managing id attribute in future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """

        Initialize a Base object.
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert list_dictionaries to JSON string
        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write JSON string representation of list_objs to a file
        args:
            list_objs (list): list of instances that inherit from Base
        """

        filename = cls.__name__ + ".json"

        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_objs)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        return list of the JSON string representation json_string
        args:
            json_string (str): string representing a list of dictionaries
        returns:
            list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        return an instance with all attributes already set
        args:
            dictionary (dict): dictionary of attributes to set
        returns:
            instance with all attributes set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        return a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = cls.from_json_string(file.read())
            return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []

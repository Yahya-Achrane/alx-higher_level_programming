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

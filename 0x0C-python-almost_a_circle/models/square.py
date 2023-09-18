#!/usr/bin/python3

"""
Module: square
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Class representing a square, inheriting from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The side length of the square.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The object ID. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A string in the format "[Square] (id) x/y - size".
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Gets the size of the Square.

        Returns:
            int: The side length of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the Square.

        Args:
            value (int): The new side length of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update method"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

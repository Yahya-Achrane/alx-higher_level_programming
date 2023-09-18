#!/usr/bin/python3

"""
Unit tests for square.py
"""

import unittest
import sys
import io
from models.base import Base
from models.square import Square


def capture_output(func):
    """
    Captures and returns the standard output of a function.

    Args:
        func (function): The function to capture output from.

    Returns:
        str: Captured output as a string.
    """
    previous_stdout = sys.stdout
    output = io.StringIO()
    sys.stdout = output
    func()
    sys.stdout = previous_stdout
    return output.getvalue()


class TestSquare(unittest.TestCase):
    """
    Test cases for Square class.
    """

    def test_init_with_id(self):
        """
        Tests initialization of Square with provided ID.
        """
        s1 = Square(10, 0, 0, 12)
        self.assertEqual(s1.id, 12)

    def test_init_without_id(self):
        """
        Test initialization of Square without provided ID.

        Sets the global object count to 0, creates a Square instance with size 10 and coordinates (2, 0).
        Checks if the ID of the Square is 1 as expected.
        """
        Base._Base__nb_objects = 0
        s2 = Square(10, 2)
        self.assertEqual(s2.id, 1)

    def test_number_of_objects(self):
        """
        Test number of objects after creating Square instances.

        Sets the global object count to 0, creates two Square instances with size 10 and coordinates (2, 0).
        Checks if the ID of the second Square is 2 and verifies if the object count is updated correctly.
        """
        Base._Base__nb_objects = 0
        s3 = Square(10, 2)
        s4 = Square(10, 2)
        self.assertEqual(s4.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_size(self):
        """
        Test size.

        Creates a Square instance with size 10 and coordinates (2, 0).
        Checks if the size attribute is set to 10.
        """
        s5 = Square(10, 2)
        self.assertEqual(s5.size, 10)

    def test_size_setter(self):
        """
        Test size setter.

        Creates a Square instance with size 10 and coordinates (2, 0).
        Sets the size to 20 and checks if the size attribute is updated accordingly.
        """
        s6 = Square(10, 2)
        s6.size = 20
        self.assertEqual(s6.size, 20)

    def test_size_setter_with_string(self):
        """
        Test size setter with string.

        Attempts to create a Square instance with a string as the size argument.
        Expects a TypeError to be raised.
        """
        with self.assertRaises(TypeError):
            s7 = Square("hello", 2)

    def test_size_setter_with_zero(self):
        """
        Test size setter with zero.

        Attempts to create a Square instance with a size of 0.
        Expects a ValueError to be raised.
        """
        with self.assertRaises(ValueError):
            s8 = Square(0, 2)

    def test_size_setter_with_negative(self):
        """
        Test size setter with negative.

        Attempts to create a Square instance with a negative size.
        Expects a ValueError to be raised.
        """
        with self.assertRaises(ValueError):
            s9 = Square(-1, 2)

    def test_x(self):
        """
        Test x.

        Creates a Square instance with size 10 and x-coordinate 2.
        Checks if the x-coordinate is set to 2.
        """
        s10 = Square(10, 2)
        self.assertEqual(s10.x, 2)

    def test_x_setter(self):
        """
        Test x setter.

        Creates a Square instance with size 10 and x-coordinate 2.
        Sets the x-coordinate to 20 and checks if it is updated accordingly.
        """
        s11 = Square(10, 2)
        s11.x = 20
        self.assertEqual(s11.x, 20)

    def test_x_setter_with_string(self):
        """
        Test x setter with string.

        Attempts to create a Square instance with a string as the x-coordinate argument.
        Expects a TypeError to be raised.
        """
        with self.assertRaises(TypeError):
            s12 = Square(10, "hello")

    def test_x_setter_with_negative(self):
        """
        Test x setter with negative.

        Attempts to create a Square instance with a negative x-coordinate.
        Expects a ValueError to be raised.
        """
        with self.assertRaises(ValueError):
            s13 = Square(10, -1)

    def test_y(self):
        """
        Test y.

        Creates a Square instance with size 10, x-coordinate 2, and y-coordinate 3.
        Checks if the y-coordinate is set to 3.
        """
        s14 = Square(10, 2, 3)
        self.assertEqual(s14.y, 3)

if __name__ == "__main__":
    unittest.main()

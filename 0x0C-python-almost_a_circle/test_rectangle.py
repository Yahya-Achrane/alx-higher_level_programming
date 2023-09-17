#!/usr/bin/python3

"""Unittest for rectangle.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_init_with_id(self):
        """Test __init__ with id"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)

    def test_init_without_id(self):
        """Test __init__ without id"""
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, 1)

    def test_init_with_string(self):
        """Test __init__ with string"""
        r3 = Rectangle(10, 2, 0, 0, "hello")
        self.assertEqual(r3.id, "hello")

    def test_init_with_float(self):
        """Test __init__ with float"""
        r4 = Rectangle(10, 2, 0, 0, 3.14)
        self.assertEqual(r4.id, 3.14)

    def test_init_with_one_arg(self):
        """Test init with one arg"""
        with self.assertRaises(TypeError):
            r5 = Rectangle(1)

    def test_init_with_two_args(self):
        """Test init with two args"""
        r6 = Rectangle(1, 2)
        self.assertEqual(r6.width, 1)
        self.assertEqual(r6.height, 2)

    def test_width(self):
        """Test width"""
        r7 = Rectangle(10, 2)
        self.assertEqual(r7.width, 10)

    def test_width_setter(self):
        """Test width setter"""
        r8 = Rectangle(10, 2)
        r8.width = 20
        self.assertEqual(r8.width, 20)

    def test_width_setter_with_string(self):
        """Test width setter with string"""
        with self.assertRaises(TypeError):
            r9 = Rectangle(10, 2)
            r9.width = "hello"

    def test_height(self):
        """Test height"""
        r12 = Rectangle(10, 2)
        self.assertEqual(r12.height, 2)

    def test_height_setter(self):
        """Test height setter"""
        r13 = Rectangle(10, 2)
        r13.height = 20
        self.assertEqual(r13.height, 20)

    def test_height_setter_with_string(self):
        """Test height setter with string"""
        with self.assertRaises(TypeError):
            r14 = Rectangle(10, 2)
            r14.height = "hello"
    def test_area(self):
        """Test area"""
        r25 = Rectangle(3, 2)
        self.assertEqual(r25.area(), 6)


if __name__ == "__main__":
    unittest.main()

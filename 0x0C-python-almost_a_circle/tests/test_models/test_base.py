#!/usr/bin/python3
"""
Unittest for base
"""

import unittest
from models.base import Base
from models.square import Square


class TestBase(unittest.TestCase):
    """class"""
    def test_base(self):
        """def"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        self.assertIsInstance(b1, Base)
        self.assertIsInstance(b1, Square)


if __name__ == "__main__":
    unittest.main()
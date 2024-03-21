#!/usr/bin/python3

"""
This module contains unit tests for the City class. Tests cover initialization and attribute setting behaviors, ensuring expected functionality.
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def test_initialization(self):
        """
        Tests that a newly created City instance has default attribute values.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


    def test_set_attributes(self):
        """
        Tests that attributes can be correctly set on a City instance.
        """
        city = City()
        city.state_id = "state_123"
        city.name = "New York"
        self.assertEqual(city.state_id, "state_123")
        self.assertEqual(city.name, "New York")

    def test_save_method(self):
        """Tests that the save method updates the updated_at attribute."""
        city = City()
        old_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
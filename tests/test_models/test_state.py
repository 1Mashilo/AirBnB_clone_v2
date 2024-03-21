#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_initialization(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_set_name(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

if __name__ == '__main__':
    unittest.main()
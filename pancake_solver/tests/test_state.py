"""Test search algorithms and related helper functions."""

# Standard library
import unittest

# Local source
import pancake_solver.common.state as h
from pancake_solver.data.node import PancakeNode


class TestState(unittest.TestCase):

    def setUp(self) -> None:
        self.pancakes = '4123'

    def test_flip_pancakes(self):
        self.assertEqual(h.flip_pancakes(self.pancakes, 1), '4321')
        self.assertEqual(h.flip_pancakes(self.pancakes, 0), '3214')
        self.assertEqual(h.flip_pancakes(self.pancakes, 2), '4132')
        self.assertEqual(h.flip_pancakes(self.pancakes, 3), '4123')  # Shouldn't flip
        self.assertEqual(h.flip_pancakes(self.pancakes, 4), '4123')  # Shouldn't flip

    def test_get_states(self):
        possible_states = h.get_states(PancakeNode(self.pancakes))
        state_pancakes = [possible_state.pancakes for possible_state in possible_states]
        self.assertEqual(state_pancakes, ['3214', '4321', '4132'])


if __name__ == '__main__':
    unittest.main()

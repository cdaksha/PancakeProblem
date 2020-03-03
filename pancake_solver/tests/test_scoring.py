"""Test cost and heuristic function functionalities."""

# Standard library
import unittest

# Local source
from pancake_solver.common.cost import backward_cost, heuristic, break_tie


class TestScoring(unittest.TestCase):

    def setUp(self) -> None:
        self.pancakes = '4123'

    def test_cost(self):
        self.assertEqual(backward_cost(len(self.pancakes), flip_index=1), 3)
        self.assertEqual(backward_cost(len(self.pancakes), flip_index=2), 2)

    def test_heuristic(self):
        self.assertEqual(heuristic(self.pancakes), 3)
        self.assertEqual(heuristic('1432'), 4)
        self.assertEqual(heuristic('4312'), 2)
        self.assertEqual(heuristic('4321'), 0)
        self.assertEqual(heuristic('4132'), 3)

    def test_break_tie(self):
        self.assertEqual(break_tie('4321', '3421'), '4321')


if __name__ == '__main__':
    unittest.main()

"""Test input parsing functionality."""

# Standard library
import unittest

# Local source
from pancake_solver.data.loader import parse_input


class TestInput(unittest.TestCase):

    def test_parse_input(self):
        self.assertEqual(parse_input('4123d'), ('4123', 'd'))
        self.assertEqual(parse_input('4123D'), ('4123', 'd'))
        self.assertEqual(parse_input('4123a'), ('4123', 'a'))
        self.assertEqual(parse_input('4123A'), ('4123', 'a'))
        self.assertEqual(parse_input(' 4123d'), ('4123', 'd'))
        self.assertEqual(parse_input('4123d '), ('4123', 'd'))
        self.assertEqual(parse_input(' 4123d '), ('4123', 'd'))

        with self.assertRaises(ValueError):
            parse_input('4123')
        with self.assertRaises(ValueError):
            parse_input('4123z')


if __name__ == '__main__':
    unittest.main()

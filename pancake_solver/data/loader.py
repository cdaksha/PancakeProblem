#!/usr/bin/env python
"""Provides functionality to parse user input into data object to store Pancakes' representation.
Pancakes' representation = integer list. Bigger integer represents larger pancake.
"""

# Standard library
from typing import Tuple

# 3rd party packages

# Local source


def parse_input(pancake_string: str) -> Tuple[str, str]:
    """Given a string containing N-digits and one character at the very end, return the pancakes string
    and the search type.
    The last character should be 'd' or 'a', referring to DFS or A* search, respectively.

    Throws ValueError if search_strategy != 'd' or 'a'.
    Throws ValueError if conversion from pancake chars to integer fails.
    """
    cleaned_string = pancake_string.strip()
    search_strategy = cleaned_string[-1].lower()
    if search_strategy not in {'d', 'a'}:
        raise ValueError("Improper search argument provided. Use 'd' for DFS and 'a' for A*.")

    try:
        pancakes = cleaned_string[:-1]
    except ValueError:
        raise ValueError("Improper pancake character detected. Conversion from pancake characters to integers failed.")

    return pancakes, search_strategy

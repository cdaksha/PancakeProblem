#!/usr/bin/env python
"""Provides functionality to convert from string <-> List[int] representation of Pancakes state.
"""

# Standard library
from typing import List

# 3rd party packages

# Local source


def string_to_pancakes(pancake_string: str) -> List[int]:
    return [int(char) for char in pancake_string]


def pancakes_to_string(pancakes: List[int]) -> str:
    return "".join([str(i) for i in pancakes])

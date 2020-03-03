#!/usr/bin/env python
"""Contains helper functions for search models."""

# Standard library
from typing import Generator

# 3rd party packages

# Local source
from pancake_solver.data.node import PancakeNode


def flip_pancakes(pancakes: str, flip_index: int) -> str:
    """Return list of pancakes after flipping at the specified flip_index.
    For example, given pancakes = '4123' and flip_index = 1, return '4321'
    """
    return pancakes[0:flip_index] + pancakes[flip_index:][::-1]


def get_states(pancake_node: PancakeNode) -> Generator:
    """Get all possible states that can occur from flipping one pancake state.
    Note that flipping at len(pancakes) - 1 is not necessary.
    Reversing a single element is the single element itself.
    """
    # return (flip_pancakes(pancakes, flip_index=i) for i in range(len(pancakes) - 1))
    for i in range(len(pancake_node.pancakes) - 1):
        yield PancakeNode(flip_pancakes(pancake_node.pancakes, flip_index=i),
                          parent=pancake_node,
                          flip_index=i)


def get_goal_state(num_pancakes: int) -> PancakeNode:
    """Identify the goal state of pancakes based on the number of pancakes.
    Ex: If # pancakes = 4, then goal state = '4321'; if # pancakes = 5, then goal state = '54321'.
    """
    return PancakeNode("".join([str(i) for i in range(num_pancakes, 0, -1)]))

#!/usr/bin/env python
"""Contains cost/heuristic functions used in algorithm(s)."""

# Standard library

# 3rd party packages

# Local source


def backward_cost(num_pancakes: int, flip_index: int) -> int:
    """The true cost value of a flip = # pancakes being flipped.
    Example: cost of one flip between pancakes 4 and 1 from the state "4123" to "4321" is equal to 3.
    The flip between 4 and 1 corresponds to a flip_index = 1.
    Note that 0 <= flip_index <= num_pancakes is required (cost >= 0).
    """
    return num_pancakes - flip_index


def heuristic(pancakes: str) -> int:
    """Heuristic function returns the ID of the largest pancake that is still out of place."""
    return max((int(pancake) for i, pancake in enumerate(pancakes[::-1], start=1) if i != int(pancake)), default=0)


def break_tie(state1: str, state2: str) -> str:
    """Break the tie between two states (i.e., two lists of pancakes).
    When there is a tie between two states/nodes, the node with a larger numerical ID will be chosen.
    Ex: If pancakes = '4321', then ID = 4321.
    TO BE USED only when there is a tie in terms of the total cost between two states.
    """
    better_state = max(int(state1), int(state2))
    return str(better_state)

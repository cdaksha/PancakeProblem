#!/usr/bin/env python
"""Contains data structure for Pancakes representation."""

# Standard library
from dataclasses import dataclass, field

# 3rd party packages

# Local source
import pancake_solver.common.cost as cost


class PancakeNode:

    def __init__(self, pancakes: str, parent=None, flip_index: int = None):
        """Node to store current pancakes, parent pancakes, and flip_index which was used to get
        from the parent pancakes to the current pancakes.

        Parameters
        ----------
        pancakes: str
        parent: PancakeNode, default=None
        flip_index: int
        """
        self.pancakes = pancakes
        self.parent = parent
        self.flip_index = flip_index

        increment = self.parent.cumulative_backward_cost if self.parent else 0
        self.cumulative_backward_cost = self.backward_cost() + increment

    def backward_cost(self):
        return cost.backward_cost(len(self.pancakes), self.flip_index) if self.flip_index is not None else 0

    def forward_cost(self):
        return cost.heuristic(self.pancakes)

    def total_cost(self):
        return self.cumulative_backward_cost + self.forward_cost()

    def __eq__(self, other):
        return self.pancakes == other.pancakes

    def __str__(self):
        pancakes = self.parent.pancakes[0:self.flip_index] + '|' + self.parent.pancakes[self.flip_index:]
        return pancakes + ' g={}, h={}'.format(self.cumulative_backward_cost, self.forward_cost())

    def __repr__(self):
        return "PancakeNode(pancakes='{}', parent='{}', flip_index={})" \
            .format(self.pancakes,
                    self.parent.pancakes if self.parent else None,
                    self.flip_index)


@dataclass(order=True)
class PrioritizedPancakeNode:
    first_priority: int
    second_priority: int
    uninformed_state: PancakeNode = field(compare=False)

    def __init__(self, state: PancakeNode):
        """Wrapper class to add priorities to the state of a pancake. Used for informed search problems."""
        self.uninformed_state = state
        self.first_priority = self.uninformed_state.total_cost()
        # Priority queue implementation prioritizes smaller (i.e. more negative) values - flipping sign to reverse
        self.second_priority = -1 * int(self.uninformed_state.pancakes)

    def __str__(self):
        return self.uninformed_state.__str__()

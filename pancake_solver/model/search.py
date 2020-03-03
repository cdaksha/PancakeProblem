#!/usr/bin/env python
"""Contains uninformed and informed search algorithms."""

# Standard library
from collections import deque
from queue import PriorityQueue

# 3rd party packages

# Local source
import pancake_solver.common.state as s
from pancake_solver.data.node import PancakeNode, PrioritizedPancakeNode

PRINT_FORMAT = '-'*25


def depth_first_search(initial_state: str):
    """Depth first search algorithm for pancake problem. Return a solution, otherwise False if none exists.
    Uses graph version of the algorithm to avoid visiting the nodes multiple times.
    Fringe is a LIFO stack (deque) implementation.
    """
    print("{fmt}Depth First Search{fmt}".format(fmt=PRINT_FORMAT))
    goal_state = s.get_goal_state(num_pancakes=len(initial_state))
    visited = []
    print("Initial State: {}".format(initial_state))
    fringe = deque([PancakeNode(initial_state)])
    while fringe:
        current_state = fringe.pop()
        visited.append(current_state)
        if current_state == goal_state:
            print("Final State: {}".format(current_state.pancakes))
            return current_state.pancakes
        else:
            children = [state for state in s.get_states(current_state) if state not in visited]
            children = sorted(children, key=lambda state: int(state.pancakes))
            fringe.extend(children)
        print(fringe[-1])
    return False


def a_star_search(initial_state: str):
    """A* (informed) search algorithm for pancake problem. Return a solution, otherwise False if none exists.
    Uses graph version of the algorithm to avoid visiting the nodes multiple times.
    Fringe is a priority queue implementation.
    """
    print("{fmt}A* Search{fmt}".format(fmt=PRINT_FORMAT))
    goal_state = s.get_goal_state(num_pancakes=len(initial_state))
    visited = []
    print("Initial State: {}".format(initial_state))
    fringe = PriorityQueue()
    fringe.put(PrioritizedPancakeNode(PancakeNode(initial_state)))
    while not fringe.empty():
        current_state = fringe.get()
        visited.append(current_state.uninformed_state)
        if current_state.uninformed_state == goal_state:
            print("Final State: {}".format(current_state.uninformed_state.pancakes))
            return current_state.uninformed_state.pancakes
        else:
            for state in s.get_states(current_state.uninformed_state):
                if state not in visited:
                    fringe.put(PrioritizedPancakeNode(state))
        print(fringe.queue[0])
    return False


# factory
algorithm = {
    'd': depth_first_search,
    'a': a_star_search,
}

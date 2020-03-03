#!/usr/bin/env python
"""Reads user input and runs respective search algorithm (DFS or A*)."""

# Standard library

# 3rd party packages

# Local source
import pancake_solver.data.loader as loader
import pancake_solver.model.search as search


def run():
    user_input = input("Initialize pancakes and search algorithm (ex: 4132d):")
    initial_state, search_strategy = loader.parse_input(user_input)
    final_state = search.algorithm[search_strategy](initial_state)
    return final_state


if __name__ == "__main__":
    run()

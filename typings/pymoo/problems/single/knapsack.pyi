"""
This type stub file was generated by pyright.
"""

from pymoo.model.problem import Problem

class Knapsack(Problem):
    def __init__(self, n_items, W, P, C) -> None:
        ...
    


class MultiObjectiveKnapsack(Knapsack):
    def __init__(self, *args) -> None:
        ...
    


def create_random_knapsack_problem(n_items, seed=..., variant=...):
    ...


"""
This type stub file was generated by pyright.
"""

from pymoo.operators.repair.bounds_repair import BoundsRepair

def set_to_bounds_if_outside(X, xl, xu):
    ...

def set_to_bounds_if_outside_by_problem(problem, X):
    ...

class ToBoundOutOfBoundsRepair(BoundsRepair):
    def repair_out_of_bounds(self, problem, X):
        ...
    



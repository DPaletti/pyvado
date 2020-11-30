"""
This type stub file was generated by pyright.
"""

import numpy as np
from pymoo.operators.repair.bounds_repair import BoundsRepair

def inverse_penality(x, p, xl, xu, alpha=...):
    ...

def inverse_penality_by_problem(problem, x, p, **kwargs):
    ...

class InversePenaltyOutOfBoundsRepair(BoundsRepair):
    def repair_out_of_bounds(self, problem, X, P=..., **kwargs):
        ...
    


if __name__ == '__main__':
    xl = np.zeros(2)
    xu = np.ones(2)
    p = np.array([0.5, 0.6])
    c = np.array([- 0.1, 1])
    data = []
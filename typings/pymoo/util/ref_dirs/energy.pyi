"""
This type stub file was generated by pyright.
"""

from pymoo.util.reference_direction import ReferenceDirectionFactory

class RieszEnergyReferenceDirectionFactory(ReferenceDirectionFactory):
    def __init__(self, n_dim, n_points, ref_points=..., return_as_tuple=..., n_max_iter=..., n_until_optimizer_reset=..., sampling=..., norm_gradients=..., verify_gradient=..., freeze_edges=..., precision=..., restarts=..., X=..., d=..., callback=..., **kwargs) -> None:
        ...
    
    def calc_ref_points(self, X, ref_points):
        ...
    


def squared_dist(A, B):
    ...

def calc_potential_energy(A, d):
    ...

def calc_potential_energy_with_grad(x, d, return_mutual_dist=...):
    ...


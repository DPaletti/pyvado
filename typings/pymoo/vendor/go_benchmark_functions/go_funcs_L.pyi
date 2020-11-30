"""
This type stub file was generated by pyright.
"""

from .go_benchmark import Benchmark

class Langermann(Benchmark):
    r"""
    Langermann objective function.

    This class defines the Langermann [1]_ global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\text{Langermann}}(x) = - \sum_{i=1}^{5} 
        \frac{c_i \cos\left\{\pi \left[\left(x_{1}- a_i\right)^{2}
        + \left(x_{2} - b_i \right)^{2}\right]\right\}}{e^{\frac{\left( x_{1}
        - a_i\right)^{2} + \left( x_{2} - b_i\right)^{2}}{\pi}}}


    Where:

    .. math::

        \begin{matrix}
        a = [3, 5, 2, 1, 7]\\
        b = [5, 2, 1, 4, 9]\\
        c = [1, 2, 5, 2, 3] \\
        \end{matrix}


    Here :math:`x_i \in [0, 10]` for :math:`i = 1, 2`.

    *Global optimum*: :math:`f(x) = -5.1621259`
    for :math:`x = [2.00299219, 1.006096]`

    .. [1] Gavana, A. Global Optimization Benchmarks and AMPGO retrieved 2015

    TODO: Langermann from Gavana is _not the same_ as Jamil #68.
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


class LennardJones(Benchmark):
    r"""
    LennardJones objective function.

    This class defines the Lennard-Jones global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\text{LennardJones}}(\mathbf{x}) = \sum_{i=0}^{n-2}\sum_{j>1}^{n-1}
        \frac{1}{r_{ij}^{12}} - \frac{1}{r_{ij}^{6}}


    Where, in this exercise:

    .. math::

        r_{ij} = \sqrt{(x_{3i}-x_{3j})^2 + (x_{3i+1}-x_{3j+1})^2)
        + (x_{3i+2}-x_{3j+2})^2}


    Valid for any dimension, :math:`n = 3*k, k=2 , 3, 4, ..., 20`. :math:`k`
    is the number of atoms in 3-D space constraints: unconstrained type:
    multi-modal with one global minimum; non-separable

    Value-to-reach: :math:`minima[k-2] + 0.0001`. See array of minima below;
    additional minima available at the Cambridge cluster database:

    http://www-wales.ch.cam.ac.uk/~jon/structures/LJ/tables.150.html

    Here, :math:`n` represents the number of dimensions and
    :math:`x_i \in [-4, 4]` for :math:`i = 1 ,..., n`.

    *Global optimum*:

    .. math::

        \text{minima} = [-1.,-3.,-6.,-9.103852,-12.712062,-16.505384,\\
                         -19.821489, -24.113360, -28.422532,-32.765970,\\
                         -37.967600,-44.326801, -47.845157,-52.322627,\\
                         -56.815742,-61.317995, -66.530949, -72.659782,\\
                         -77.1777043]\\


    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def change_dimensions(self, ndim):
        ...
    
    def fun(self, x, *args):
        ...
    


class Leon(Benchmark):
    r"""
    Leon objective function.

    This class defines the Leon [1]_ global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\text{Leon}}(\mathbf{x}) = \left(1 - x_{1}\right)^{2} 
        + 100 \left(x_{2} - x_{1}^{2} \right)^{2}


    with :math:`x_i \in [-1.2, 1.2]` for :math:`i = 1, 2`.

    *Global optimum*: :math:`f(x) = 0` for :math:`x = [1, 1]`

    .. [1] Jamil, M. & Yang, X.-S. A Literature Survey of Benchmark Functions
    For Global Optimization Problems Int. Journal of Mathematical Modelling
    and Numerical Optimisation, 2013, 4, 150-194.
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


class Levy03(Benchmark):
    r"""
    Levy 3 objective function.

    This class defines the Levy 3 [1]_ global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\text{Levy03}}(\mathbf{x}) = \sin^2(\pi y_1)+\sum_{i=1}^{n-1}(y_i-1)^2[1+10\sin^2(\pi y_{i+1})]+(y_n-1)^2

    Where, in this exercise:

    .. math::

        y_i=1+\frac{x_i-1}{4}


    Here, :math:`n` represents the number of dimensions and :math:`x_i \in [-10, 10]` for :math:`i=1,...,n`.

    *Global optimum*: :math:`f(x_i) = 0` for :math:`x_i = 1` for :math:`i=1,...,n`

    .. [1] Mishra, S. Global Optimization by Differential Evolution and
    Particle Swarm Methods: Evaluation on Some Benchmark Functions.
    Munich Personal RePEc Archive, 2006, 1005

    TODO: not clear what the Levy function definition is.  Gavana, Mishra,
    Adorio have different forms. Indeed Levy 3 docstring from Gavana
    disagrees with the Gavana code!  The following code is from the Mishra
    listing of Levy08.
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


class Levy05(Benchmark):
    r"""
    Levy 5 objective function.

    This class defines the Levy 5 [1]_ global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\text{Levy05}}(\mathbf{x}) = \sum_{i=1}^{5} i \cos \left[(i-1)x_1 + i \right] \times \sum_{j=1}^{5} j \cos \left[(j+1)x_2 + j \right] + (x_1 + 1.42513)^2 + (x_2 + 0.80032)^2

    Here, :math:`n` represents the number of dimensions and :math:`x_i \in [-10, 10]` for :math:`i=1,...,n`.

    *Global optimum*: :math:`f(x_i) = -176.1375779` for :math:`\mathbf{x} = [-1.30685, -1.42485]`.

    .. [1] Mishra, S. Global Optimization by Differential Evolution and
    Particle Swarm Methods: Evaluation on Some Benchmark Functions.
    Munich Personal RePEc Archive, 2006, 1005
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


class Levy13(Benchmark):
    r"""
    Levy13 objective function.

    This class defines the Levy13 [1]_ global optimization problem. This is a
    multimodal minimization problem defined as follows:

    .. math::

        f_{\text{Levy13}}(x) = \left(x_{1} -1\right)^{2} \left[\sin^{2}
        \left(3 \pi x_{2}\right) + 1\right] + \left(x_{2} 
        - 1\right)^{2} \left[\sin^{2}\left(2 \pi x_{2}\right)
        + 1\right] + \sin^{2}\left(3 \pi x_{1}\right)


    with :math:`x_i \in [-10, 10]` for :math:`i = 1, 2`.

    *Global optimum*: :math:`f(x) = 0` for :math:`x = [1, 1]`

    .. [1] Mishra, S. Some new test functions for global optimization and
    performance of repulsive particle swarm method.
    Munich Personal RePEc Archive, 2006, 2718
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


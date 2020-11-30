"""
This type stub file was generated by pyright.
"""

from .go_benchmark import Benchmark

class XinSheYang01(Benchmark):
    r"""
    Xin-She Yang 1 objective function.

    This class defines the Xin-She Yang 1 [1]_ global optimization problem.
    This is a multimodal minimization problem defined as follows:

    .. math::

        f_{\text{XinSheYang01}}(x) = \sum_{i=1}^{n} \epsilon_i \lvert x_i 
                                     \rvert^i


    The variable :math:`\epsilon_i, (i = 1, ..., n)` is a random variable
    uniformly distributed in :math:`[0, 1]`.

    Here, :math:`n` represents the number of dimensions and
    :math:`x_i \in [-5, 5]` for :math:`i = 1, ..., n`.

    *Global optimum*: :math:`f(x) = 0` for :math:`x_i = 0` for
    :math:`i = 1, ..., n`

    .. [1] Jamil, M. & Yang, X.-S. A Literature Survey of Benchmark Functions
    For Global Optimization Problems Int. Journal of Mathematical Modelling
    and Numerical Optimisation, 2013, 4, 150-194.
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


class XinSheYang02(Benchmark):
    r"""
    Xin-She Yang 2 objective function.

    This class defines the Xin-She Yang 2 [1]_ global optimization problem.
    This is a multimodal minimization problem defined as follows:

    .. math::

        f_{\text{XinSheYang02}}(\x) = \frac{\sum_{i=1}^{n} \lvert{x_{i}}\rvert}
                                      {e^{\sum_{i=1}^{n} \sin\left(x_{i}^{2.0}
                                      \right)}}

    Here, :math:`n` represents the number of dimensions and
    :math:`x_i \in [-2\pi, 2\pi]` for :math:`i = 1, ..., n`.

    *Global optimum*: :math:`f(x) = 0` for :math:`x_i = 0` for
    :math:`i = 1, ..., n`

    .. [1] Jamil, M. & Yang, X.-S. A Literature Survey of Benchmark Functions
    For Global Optimization Problems Int. Journal of Mathematical Modelling
    and Numerical Optimisation, 2013, 4, 150-194.
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


class XinSheYang03(Benchmark):
    r"""
    Xin-She Yang 3 objective function.

    This class defines the Xin-She Yang 3 [1]_ global optimization problem.
    This is a multimodal minimization problem defined as follows:

    .. math::

        f_{\text{XinSheYang03}}(x) = e^{-\sum_{i=1}^{n} (x_i/\beta)^{2m}}
                                     - 2e^{-\sum_{i=1}^{n} x_i^2}
                                     \prod_{i=1}^{n} \cos^2(x_i)


    Where, in this exercise, :math:`\beta = 15` and :math:`m = 3`.

    Here, :math:`n` represents the number of dimensions and
    :math:`x_i \in [-20, 20]` for :math:`i = 1, ..., n`.

    *Global optimum*: :math:`f(x) = -1` for :math:`x_i = 0` for
    :math:`i = 1, ..., n`

    .. [1] Jamil, M. & Yang, X.-S. A Literature Survey of Benchmark Functions
    For Global Optimization Problems Int. Journal of Mathematical Modelling
    and Numerical Optimisation, 2013, 4, 150-194.
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


class XinSheYang04(Benchmark):
    r"""
    Xin-She Yang 4 objective function.

    This class defines the Xin-She Yang 4 [1]_ global optimization problem.
    This is a multimodal minimization problem defined as follows:

    .. math::

        f_{\text{XinSheYang04}}(x) = \left[ \sum_{i=1}^{n} \sin^2(x_i)
                                     - e^{-\sum_{i=1}^{n} x_i^2} \right ]
                                     e^{-\sum_{i=1}^{n} \sin^2 \sqrt{ \lvert
                                     x_i \rvert }}

    Here, :math:`n` represents the number of dimensions and
    :math:`x_i \in [-10, 10]` for :math:`i = 1, ..., n`.

    *Global optimum*: :math:`f(x) = -1` for :math:`x_i = 0` for
    :math:`i = 1, ..., n`

    .. [1] Jamil, M. & Yang, X.-S. A Literature Survey of Benchmark Functions
    For Global Optimization Problems Int. Journal of Mathematical Modelling
    and Numerical Optimisation, 2013, 4, 150-194.
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


class Xor(Benchmark):
    r"""
    Xor objective function.

    This class defines the Xor [1]_ global optimization problem. This is a
    multimodal minimization problem defined as follows:

    .. math::

        f_{\text{Xor}}(x) = \left[ 1 + \exp \left( - \frac{x_7}{1 +
        \exp(-x_1 - x_2 - x_5)} - \frac{x_8}{1 + \exp(-x_3 - x_4 - x_6)}
        - x_9 \right ) \right ]^{-2} \\
        + \left [ 1 + \exp \left( -\frac{x_7}{1 + \exp(-x_5)}
        - \frac{x_8}{1 + \exp(-x_6)} - x_9 \right ) \right] ^{-2} \\
        + \left [1 - \left\{1 + \exp \left(-\frac{x_7}{1 + \exp(-x_1 - x_5)}
        - \frac{x_8}{1 + \exp(-x_3 - x_6)} - x_9 \right ) \right\}^{-1}
        \right ]^2 \\
        + \left [1 - \left\{1 + \exp \left(-\frac{x_7}{1 + \exp(-x_2 - x_5)}
        - \frac{x_8}{1 + \exp(-x_4 - x_6)} - x_9 \right ) \right\}^{-1}
        \right ]^2


    with :math:`x_i \in [-1, 1]` for :math:`i=1,...,9`.

    *Global optimum*: :math:`f(x) = 0.9597588` for
    :math:`\x = [1, -1, 1, -1, -1, 1, 1, -1, 0.421134]`

    .. [1] Gavana, A. Global Optimization Benchmarks and AMPGO retrieved 2015
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    



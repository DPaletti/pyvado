"""
This type stub file was generated by pyright.
"""

from statsmodels.tsa.statespace import mlemodel

"""
(Internal) AR(1) model for monthly growth rates aggregated to quarterly freq.

Author: Chad Fulton
License: BSD-3
"""
class QuarterlyAR1(mlemodel.MLEModel):
    r"""
    AR(1) model for monthly growth rates aggregated to quarterly frequency

    Parameters
    ----------
    endog : array_like
        The observed time-series process :math:`y`

    Notes
    -----
    This model is internal, used to estimate starting parameters for the
    DynamicFactorMQ class. The model is:

    .. math::

        y_t & = \begin{bmatrix} 1 & 2 & 3 & 2 & 1 \end{bmatrix} \alpha_t \\
        \alpha_t & = \begin{bmatrix}
            \phi & 0 & 0 & 0 & 0 \\
               1 & 0 & 0 & 0 & 0 \\
               0 & 1 & 0 & 0 & 0 \\
               0 & 0 & 1 & 0 & 0 \\
               0 & 0 & 0 & 1 & 0 \\
        \end{bmatrix} +
        \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix} \varepsilon_t

    The two parameters to be estimated are :math:`\phi` and :math:`\sigma^2`.

    It supports fitting via the usual quasi-Newton methods, as well as using
    the EM algorithm.

    """
    def __init__(self, endog) -> None:
        ...
    
    @property
    def param_names(self):
        ...
    
    @property
    def start_params(self):
        ...
    
    def fit(self, *args, **kwargs):
        ...
    
    def fit_em(self, start_params=..., transformed=..., cov_type=..., cov_kwds=..., maxiter=..., tolerance=..., em_initialization=..., mstep_method=..., full_output=..., return_params=..., low_memory=...):
        ...
    
    def transform_params(self, unconstrained):
        ...
    
    def untransform_params(self, constrained):
        ...
    
    def update(self, params, **kwargs):
        ...
    



"""
This type stub file was generated by pyright.
"""

from statsmodels.compat.pandas import Appender
from .mlemodel import MLEModel, MLEResults, MLEResultsWrapper

"""
Linear exponential smoothing models

Author: Chad Fulton
License: BSD-3
"""
class ExponentialSmoothing(MLEModel):
    """
    Linear exponential smoothing models

    Parameters
    ----------
    endog : array_like
        The observed time-series process :math:`y`
    trend : bool, optional
        Whether or not to include a trend component. Default is False.
    damped_trend : bool, optional
        Whether or not an included trend component is damped. Default is False.
    seasonal : int, optional
        The number of periods in a complete seasonal cycle for seasonal
        (Holt-Winters) models. For example, 4 for quarterly data with an
        annual cycle or 7 for daily data with a weekly cycle. Default is
        no seasonal effects.
    initialization_method : str, optional
        Method for initialize the recursions. One of:

        * 'estimated'
        * 'concentrated'
        * 'heuristic'
        * 'known'

        If 'known' initialization is used, then `initial_level` must be
        passed, as well as `initial_slope` and `initial_seasonal` if
        applicable. Default is 'estimated'.
    initial_level : float, optional
        The initial level component. Only used if initialization is 'known'.
    initial_trend : float, optional
        The initial trend component. Only used if initialization is 'known'.
    initial_seasonal : array_like, optional
        The initial seasonal component. An array of length `seasonal`
        or length `seasonal - 1` (in which case the last initial value
        is computed to make the average effect zero). Only used if
        initialization is 'known'.
    bounds : iterable[tuple], optional
        An iterable containing bounds for the parameters. Must contain four
        elements, where each element is a tuple of the form (lower, upper).
        Default is (0.0001, 0.9999) for the level, trend, and seasonal
        smoothing parameters and (0.8, 0.98) for the trend damping parameter.
    concentrate_scale : bool, optional
        Whether or not to concentrate the scale (variance of the error term)
        out of the likelihood.

    Notes
    -----
    The parameters and states of this model are estimated by setting up the
    exponential smoothing equations as a special case of a linear Gaussian
    state space model and applying the Kalman filter. As such, it has slightly
    worse performance than the dedicated exponential smoothing model,
    :class:`statsmodels.tsa.holtwinters.ExponentialSmoothing`, and it does not
    support multiplicative (nonlinear) exponential smoothing models.

    However, as a subclass of the state space models, this model class shares
    a consistent set of functionality with those models, which can make it
    easier to work with. In addition, it supports computing confidence
    intervals for forecasts and it supports concentrating the initial
    state out of the likelihood function.

    References
    ----------
    [1] Hyndman, Rob, Anne B. Koehler, J. Keith Ord, and Ralph D. Snyder.
        Forecasting with exponential smoothing: the state space approach.
        Springer Science & Business Media, 2008.
    """
    def __init__(self, endog, trend=..., damped_trend=..., seasonal=..., initialization_method=..., initial_level=..., initial_trend=..., initial_seasonal=..., bounds=..., concentrate_scale=..., dates=..., freq=..., missing=...) -> None:
        ...
    
    def clone(self, endog, exog=..., **kwargs):
        ...
    
    @property
    def state_names(self):
        ...
    
    @property
    def param_names(self):
        ...
    
    @property
    def start_params(self):
        ...
    
    @property
    def k_params(self):
        ...
    
    def transform_params(self, unconstrained):
        ...
    
    def untransform_params(self, constrained):
        ...
    
    def update(self, params, transformed=..., includes_fixed=..., complex_step=...):
        ...
    
    @Appender(MLEModel.loglike.__doc__)
    def loglike(self, params, *args, **kwargs):
        ...
    
    @Appender(MLEModel.filter.__doc__)
    def filter(self, params, cov_type=..., cov_kwds=..., return_ssm=..., results_class=..., results_wrapper_class=..., *args, **kwargs):
        ...
    
    @Appender(MLEModel.smooth.__doc__)
    def smooth(self, params, cov_type=..., cov_kwds=..., return_ssm=..., results_class=..., results_wrapper_class=..., *args, **kwargs):
        ...
    


class ExponentialSmoothingResults(MLEResults):
    """
    Results from fitting a linear exponential smoothing model
    """
    def __init__(self, model, params, filter_results, cov_type=..., **kwargs) -> None:
        ...
    
    @Appender(MLEResults.summary.__doc__)
    def summary(self, alpha=..., start=...):
        ...
    


class ExponentialSmoothingResultsWrapper(MLEResultsWrapper):
    _attrs = ...
    _wrap_attrs = ...
    _methods = ...
    _wrap_methods = ...



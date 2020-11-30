"""
This type stub file was generated by pyright.
"""

"""
Innovations algorithm for MA(q) and SARIMA(p,d,q)x(P,D,Q,s) model parameters.

Author: Chad Fulton
License: BSD-3
"""
def innovations(endog, ma_order=..., demean=...):
    """
    Estimate MA parameters using innovations algorithm.

    Parameters
    ----------
    endog : array_like or SARIMAXSpecification
        Input time series array, assumed to be stationary.
    ma_order : int, optional
        Maximum moving average order. Default is 0.
    demean : bool, optional
        Whether to estimate and remove the mean from the process prior to
        fitting the moving average coefficients. Default is True.

    Returns
    -------
    parameters : list of SARIMAXParams objects
        List elements correspond to estimates at different `ma_order`. For
        example, parameters[0] is an `SARIMAXParams` instance corresponding to
        `ma_order=0`.
    other_results : Bunch
        Includes one component, `spec`, containing the `SARIMAXSpecification`
        instance corresponding to the input arguments.

    Notes
    -----
    The primary reference is [1]_, section 5.1.3.

    This procedure assumes that the series is stationary.

    References
    ----------
    .. [1] Brockwell, Peter J., and Richard A. Davis. 2016.
       Introduction to Time Series and Forecasting. Springer.
    """
    ...

def innovations_mle(endog, order=..., seasonal_order=..., demean=..., enforce_invertibility=..., start_params=..., minimize_kwargs=...):
    """
    Estimate SARIMA parameters by MLE using innovations algorithm.

    Parameters
    ----------
    endog : array_like
        Input time series array.
    order : tuple, optional
        The (p,d,q) order of the model for the number of AR parameters,
        differences, and MA parameters. Default is (0, 0, 0).
    seasonal_order : tuple, optional
        The (P,D,Q,s) order of the seasonal component of the model for the
        AR parameters, differences, MA parameters, and periodicity. Default
        is (0, 0, 0, 0).
    demean : bool, optional
        Whether to estimate and remove the mean from the process prior to
        fitting the SARIMA coefficients. Default is True.
    enforce_invertibility : bool, optional
        Whether or not to transform the MA parameters to enforce invertibility
        in the moving average component of the model. Default is True.
    start_params : array_like, optional
        Initial guess of the solution for the loglikelihood maximization. The
        AR polynomial must be stationary. If `enforce_invertibility=True` the
        MA poylnomial must be invertible. If not provided, default starting
        parameters are computed using the Hannan-Rissanen method.
    minimize_kwargs : dict, optional
        Arguments to pass to scipy.optimize.minimize.

    Returns
    -------
    parameters : SARIMAXParams object
    other_results : Bunch
        Includes four components: `spec`, containing the `SARIMAXSpecification`
        instance corresponding to the input arguments; `minimize_kwargs`,
        containing any keyword arguments passed to `minimize`; `start_params`,
        containing the untransformed starting parameters passed to `minimize`;
        and `minimize_results`, containing the output from `minimize`.

    Notes
    -----
    The primary reference is [1]_, section 5.2.

    Note: we do not include `enforce_stationarity` as an argument, because this
    function requires stationarity.

    TODO: support concentrating out the scale (should be easy: use sigma2=1
          and then compute sigma2=np.sum(u**2 / v) / len(u); would then need to
          redo llf computation in the Cython function).

    TODO: add support for fixed parameters

    TODO: add support for secondary optimization that does not enforce
          stationarity / invertibility, starting from first step's parameters

    References
    ----------
    .. [1] Brockwell, Peter J., and Richard A. Davis. 2016.
       Introduction to Time Series and Forecasting. Springer.
    """
    ...


"""
This type stub file was generated by pyright.
"""

from statsmodels.compat.pandas import deprecate_kwarg

"""Correlation plot functions."""
@deprecate_kwarg("unbiased", "adjusted")
def plot_acf(x, ax=..., lags=..., *, alpha=..., use_vlines=..., adjusted=..., fft=..., missing=..., title=..., zero=..., vlines_kwargs=..., **kwargs):
    """
    Plot the autocorrelation function

    Plots lags on the horizontal and the correlations on vertical axis.

    Parameters
    ----------
    x : array_like
        Array of time-series values
    ax : AxesSubplot, optional
        If given, this subplot is used to plot in instead of a new figure being
        created.
    lags : {int, array_like}, optional
        An int or array of lag values, used on horizontal axis. Uses
        np.arange(lags) when lags is an int.  If not provided,
        ``lags=np.arange(len(corr))`` is used.
    alpha : scalar, optional
        If a number is given, the confidence intervals for the given level are
        returned. For instance if alpha=.05, 95 % confidence intervals are
        returned where the standard deviation is computed according to
        Bartlett's formula. If None, no confidence intervals are plotted.
    use_vlines : bool, optional
        If True, vertical lines and markers are plotted.
        If False, only markers are plotted.  The default marker is 'o'; it can
        be overridden with a ``marker`` kwarg.
    adjusted : bool
        If True, then denominators for autocovariance are n-k, otherwise n
    fft : bool, optional
        If True, computes the ACF via FFT.
    missing : str, optional
        A string in ['none', 'raise', 'conservative', 'drop'] specifying how
        the NaNs are to be treated.
    title : str, optional
        Title to place on plot.  Default is 'Autocorrelation'
    zero : bool, optional
        Flag indicating whether to include the 0-lag autocorrelation.
        Default is True.
    vlines_kwargs : dict, optional
        Optional dictionary of keyword arguments that are passed to vlines.
    **kwargs : kwargs, optional
        Optional keyword arguments that are directly passed on to the
        Matplotlib ``plot`` and ``axhline`` functions.

    Returns
    -------
    Figure
        If `ax` is None, the created figure.  Otherwise the figure to which
        `ax` is connected.

    See Also
    --------
    matplotlib.pyplot.xcorr
    matplotlib.pyplot.acorr

    Notes
    -----
    Adapted from matplotlib's `xcorr`.

    Data are plotted as ``plot(lags, corr, **kwargs)``

    kwargs is used to pass matplotlib optional arguments to both the line
    tracing the autocorrelations and for the horizontal line at 0. These
    options must be valid for a Line2D object.

    vlines_kwargs is used to pass additional optional arguments to the
    vertical lines connecting each autocorrelation to the axis.  These options
    must be valid for a LineCollection object.

    Examples
    --------
    >>> import pandas as pd
    >>> import matplotlib.pyplot as plt
    >>> import statsmodels.api as sm

    >>> dta = sm.datasets.sunspots.load_pandas().data
    >>> dta.index = pd.Index(sm.tsa.datetools.dates_from_range('1700', '2008'))
    >>> del dta["YEAR"]
    >>> sm.graphics.tsa.plot_acf(dta.values.squeeze(), lags=40)
    >>> plt.show()

    .. plot:: plots/graphics_tsa_plot_acf.py
    """
    ...

def plot_pacf(x, ax=..., lags=..., alpha=..., method=..., use_vlines=..., title=..., zero=..., vlines_kwargs=..., **kwargs):
    """
    Plot the partial autocorrelation function

    Parameters
    ----------
    x : array_like
        Array of time-series values
    ax : AxesSubplot, optional
        If given, this subplot is used to plot in instead of a new figure being
        created.
    lags : {int, array_like}, optional
        An int or array of lag values, used on horizontal axis. Uses
        np.arange(lags) when lags is an int.  If not provided,
        ``lags=np.arange(len(corr))`` is used.
    alpha : float, optional
        If a number is given, the confidence intervals for the given level are
        returned. For instance if alpha=.05, 95 % confidence intervals are
        returned where the standard deviation is computed according to
        1/sqrt(len(x))
    method : {'ywunbiased', 'ywmle', 'ols'}
        Specifies which method for the calculations to use:

        - yw or ywunbiased : yule walker with bias correction in denominator
          for acovf. Default.
        - ywm or ywmle : yule walker without bias correction
        - ols - regression of time series on lags of it and on constant
        - ld or ldunbiased : Levinson-Durbin recursion with bias correction
        - ldb or ldbiased : Levinson-Durbin recursion without bias correction

    use_vlines : bool, optional
        If True, vertical lines and markers are plotted.
        If False, only markers are plotted.  The default marker is 'o'; it can
        be overridden with a ``marker`` kwarg.
    title : str, optional
        Title to place on plot.  Default is 'Partial Autocorrelation'
    zero : bool, optional
        Flag indicating whether to include the 0-lag autocorrelation.
        Default is True.
    vlines_kwargs : dict, optional
        Optional dictionary of keyword arguments that are passed to vlines.
    **kwargs : kwargs, optional
        Optional keyword arguments that are directly passed on to the
        Matplotlib ``plot`` and ``axhline`` functions.

    Returns
    -------
    Figure
        If `ax` is None, the created figure.  Otherwise the figure to which
        `ax` is connected.

    See Also
    --------
    matplotlib.pyplot.xcorr
    matplotlib.pyplot.acorr

    Notes
    -----
    Plots lags on the horizontal and the correlations on vertical axis.
    Adapted from matplotlib's `xcorr`.

    Data are plotted as ``plot(lags, corr, **kwargs)``

    kwargs is used to pass matplotlib optional arguments to both the line
    tracing the autocorrelations and for the horizontal line at 0. These
    options must be valid for a Line2D object.

    vlines_kwargs is used to pass additional optional arguments to the
    vertical lines connecting each autocorrelation to the axis.  These options
    must be valid for a LineCollection object.

    Examples
    --------
    >>> import pandas as pd
    >>> import matplotlib.pyplot as plt
    >>> import statsmodels.api as sm

    >>> dta = sm.datasets.sunspots.load_pandas().data
    >>> dta.index = pd.Index(sm.tsa.datetools.dates_from_range('1700', '2008'))
    >>> del dta["YEAR"]
    >>> sm.graphics.tsa.plot_acf(dta.values.squeeze(), lags=40)
    >>> plt.show()

    .. plot:: plots/graphics_tsa_plot_pacf.py
    """
    ...

def seasonal_plot(grouped_x, xticklabels, ylabel=..., ax=...):
    """
    Consider using one of month_plot or quarter_plot unless you need
    irregular plotting.

    Parameters
    ----------
    grouped_x : iterable of DataFrames
        Should be a GroupBy object (or similar pair of group_names and groups
        as DataFrames) with a DatetimeIndex or PeriodIndex
    xticklabels : list of str
        List of season labels, one for each group.
    ylabel : str
        Lable for y axis
    ax : AxesSubplot, optional
        If given, this subplot is used to plot in instead of a new figure being
        created.
    """
    ...

def month_plot(x, dates=..., ylabel=..., ax=...):
    """
    Seasonal plot of monthly data.

    Parameters
    ----------
    x : array_like
        Seasonal data to plot. If dates is None, x must be a pandas object
        with a PeriodIndex or DatetimeIndex with a monthly frequency.
    dates : array_like, optional
        If `x` is not a pandas object, then dates must be supplied.
    ylabel : str, optional
        The label for the y-axis. Will attempt to use the `name` attribute
        of the Series.
    ax : Axes, optional
        Existing axes instance.

    Returns
    -------
    Figure
       If `ax` is provided, the Figure instance attached to `ax`. Otherwise
       a new Figure instance.

    Examples
    --------
    >>> import statsmodels.api as sm
    >>> import pandas as pd

    >>> dta = sm.datasets.elnino.load_pandas().data
    >>> dta['YEAR'] = dta.YEAR.astype(int).astype(str)
    >>> dta = dta.set_index('YEAR').T.unstack()
    >>> dates = pd.to_datetime(list(map(lambda x: '-'.join(x) + '-1',
    ...                                 dta.index.values)))
    >>> dta.index = pd.DatetimeIndex(dates, freq='MS')
    >>> fig = sm.graphics.tsa.month_plot(dta)

    .. plot:: plots/graphics_tsa_month_plot.py
    """
    ...

def quarter_plot(x, dates=..., ylabel=..., ax=...):
    """
    Seasonal plot of quarterly data

    Parameters
    ----------
    x : array_like
        Seasonal data to plot. If dates is None, x must be a pandas object
        with a PeriodIndex or DatetimeIndex with a monthly frequency.
    dates : array_like, optional
        If `x` is not a pandas object, then dates must be supplied.
    ylabel : str, optional
        The label for the y-axis. Will attempt to use the `name` attribute
        of the Series.
    ax : matplotlib.axes, optional
        Existing axes instance.

    Returns
    -------
    Figure
       If `ax` is provided, the Figure instance attached to `ax`. Otherwise
       a new Figure instance.

    Examples
    --------
    >>> import statsmodels.api as sm
    >>> import pandas as pd

    >>> dta = sm.datasets.elnino.load_pandas().data
    >>> dta['YEAR'] = dta.YEAR.astype(int).astype(str)
    >>> dta = dta.set_index('YEAR').T.unstack()
    >>> dates = pd.to_datetime(list(map(lambda x: '-'.join(x) + '-1',
    ...                                 dta.index.values)))
    >>> dta.index = dates.to_period('Q')
    >>> fig = sm.graphics.tsa.quarter_plot(dta)

    .. plot:: plots/graphics_tsa_quarter_plot.py
    """
    ...

def plot_predict(result, start=..., end=..., dynamic=..., alpha=..., ax=..., **predict_kwargs):
    """

    Parameters
    ----------
    result : Result
        Any model result supporting ``get_prediction``.
    start : int, str, or datetime, optional
        Zero-indexed observation number at which to start forecasting,
        i.e., the first forecast is start. Can also be a date string to
        parse or a datetime type. Default is the the zeroth observation.
    end : int, str, or datetime, optional
        Zero-indexed observation number at which to end forecasting, i.e.,
        the last forecast is end. Can also be a date string to
        parse or a datetime type. However, if the dates index does not
        have a fixed frequency, end must be an integer index if you
        want out of sample prediction. Default is the last observation in
        the sample.
    dynamic : bool, int, str, or datetime, optional
        Integer offset relative to `start` at which to begin dynamic
        prediction. Can also be an absolute date string to parse or a
        datetime type (these are not interpreted as offsets).
        Prior to this observation, true endogenous values will be used for
        prediction; starting with this observation and continuing through
        the end of prediction, forecasted endogenous values will be used
        instead.
    alpha : {float, None}
        The tail probability not covered by the confidence interval. Must
        be in (0, 1). Confidence interval is constructed assuming normally
        distributed shocks. If None, figure will not show the confidence
        interval.
    ax : AxesSubplot
        matplotlib Axes instance to use
    **predict_kwargs
        Any additional keyword arguments to pass to ``result.get_prediction``.

    Returns
    -------
    Figure
        matplotlib Figure containing the prediction plot
    """
    ...


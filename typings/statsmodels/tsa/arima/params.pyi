"""
This type stub file was generated by pyright.
"""

"""
SARIMAX parameters class.

Author: Chad Fulton
License: BSD-3
"""
class SARIMAXParams(object):
    """
    SARIMAX parameters.

    Parameters
    ----------
    spec : SARIMAXSpecification
        Specification of the SARIMAX model.

    Attributes
    ----------
    spec : SARIMAXSpecification
        Specification of the SARIMAX model.
    exog_names : list of str
        Names associated with exogenous parameters.
    ar_names : list of str
        Names associated with (non-seasonal) autoregressive parameters.
    ma_names : list of str
        Names associated with (non-seasonal) moving average parameters.
    seasonal_ar_names : list of str
        Names associated with seasonal autoregressive parameters.
    seasonal_ma_names : list of str
        Names associated with seasonal moving average parameters.
    param_names :list of str
        Names of all model parameters.
    k_exog_params : int
        Number of parameters associated with exogenous variables.
    k_ar_params : int
        Number of parameters associated with (non-seasonal) autoregressive
        lags.
    k_ma_params : int
        Number of parameters associated with (non-seasonal) moving average
        lags.
    k_seasonal_ar_params : int
        Number of parameters associated with seasonal autoregressive lags.
    k_seasonal_ma_params : int
        Number of parameters associated with seasonal moving average lags.
    k_params : int
        Total number of model parameters.
    """
    def __init__(self, spec) -> None:
        ...
    
    @property
    def exog_params(self):
        """(array) Parameters associated with exogenous variables."""
        ...
    
    @exog_params.setter
    def exog_params(self, value):
        ...
    
    @property
    def ar_params(self):
        """(array) Autoregressive (non-seasonal) parameters."""
        ...
    
    @ar_params.setter
    def ar_params(self, value):
        ...
    
    @property
    def ar_poly(self):
        """(Polynomial) Autoregressive (non-seasonal) lag polynomial."""
        ...
    
    @ar_poly.setter
    def ar_poly(self, value):
        ...
    
    @property
    def ma_params(self):
        """(array) Moving average (non-seasonal) parameters."""
        ...
    
    @ma_params.setter
    def ma_params(self, value):
        ...
    
    @property
    def ma_poly(self):
        """(Polynomial) Moving average (non-seasonal) lag polynomial."""
        ...
    
    @ma_poly.setter
    def ma_poly(self, value):
        ...
    
    @property
    def seasonal_ar_params(self):
        """(array) Seasonal autoregressive parameters."""
        ...
    
    @seasonal_ar_params.setter
    def seasonal_ar_params(self, value):
        ...
    
    @property
    def seasonal_ar_poly(self):
        """(Polynomial) Seasonal autoregressive lag polynomial."""
        ...
    
    @seasonal_ar_poly.setter
    def seasonal_ar_poly(self, value):
        ...
    
    @property
    def seasonal_ma_params(self):
        """(array) Seasonal moving average parameters."""
        ...
    
    @seasonal_ma_params.setter
    def seasonal_ma_params(self, value):
        ...
    
    @property
    def seasonal_ma_poly(self):
        """(Polynomial) Seasonal moving average lag polynomial."""
        ...
    
    @seasonal_ma_poly.setter
    def seasonal_ma_poly(self, value):
        ...
    
    @property
    def sigma2(self):
        """(float) Innovation variance."""
        ...
    
    @sigma2.setter
    def sigma2(self, params):
        ...
    
    @property
    def reduced_ar_poly(self):
        """(Polynomial) Reduced form autoregressive lag polynomial."""
        ...
    
    @property
    def reduced_ma_poly(self):
        """(Polynomial) Reduced form moving average lag polynomial."""
        ...
    
    @property
    def params(self):
        """(array) Complete parameter vector."""
        ...
    
    @params.setter
    def params(self, value):
        ...
    
    @property
    def is_complete(self):
        """(bool) Are current parameter values all filled in (i.e. not NaN)."""
        ...
    
    @property
    def is_valid(self):
        """(bool) Are current parameter values valid (e.g. variance > 0)."""
        ...
    
    @property
    def is_stationary(self):
        """(bool) Is the reduced autoregressive lag poylnomial stationary."""
        ...
    
    @property
    def is_invertible(self):
        """(bool) Is the reduced moving average lag poylnomial invertible."""
        ...
    
    def to_dict(self):
        """
        Return the parameters split by type into a dictionary.

        Returns
        -------
        split_params : dict
            Dictionary with keys 'exog_params', 'ar_params', 'ma_params',
            'seasonal_ar_params', 'seasonal_ma_params', and (unless
            `concentrate_scale=True`) 'sigma2'. Values are the parameters
            associated with the key, based on the `params` argument.
        """
        ...
    
    def to_pandas(self):
        """
        Return the parameters as a Pandas series.

        Returns
        -------
        series : pd.Series
            Pandas series with index set to the parameter names.
        """
        ...
    
    def __repr__(self):
        """Represent SARIMAXParams object as a string."""
        ...
    



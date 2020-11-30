"""
This type stub file was generated by pyright.
"""

from statsmodels.tools.decorators import cache_readonly, cache_writable

"""
Base tools for handling various kinds of data structures, attaching metadata to
results, and doing data cleaning
"""
class ModelData(object):
    """
    Class responsible for handling input data and extracting metadata into the
    appropriate form
    """
    _param_names = ...
    _cov_names = ...
    def __init__(self, endog, exog=..., missing=..., hasconst=..., **kwargs) -> None:
        ...
    
    def __getstate__(self):
        ...
    
    def __setstate__(self, d):
        ...
    
    @classmethod
    def handle_missing(cls, endog, exog, missing, **kwargs):
        """
        This returns a dictionary with keys endog, exog and the keys of
        kwargs. It preserves Nones.
        """
        ...
    
    @cache_writable()
    def ynames(self):
        ...
    
    @cache_writable()
    def xnames(self):
        ...
    
    @property
    def param_names(self):
        ...
    
    @param_names.setter
    def param_names(self, values):
        ...
    
    @property
    def cov_names(self):
        """
        Labels for covariance matrices

        In multidimensional models, each dimension of a covariance matrix
        differs from the number of param_names.

        If not set, returns param_names
        """
        ...
    
    @cov_names.setter
    def cov_names(self, value):
        ...
    
    @cache_readonly
    def row_labels(self):
        ...
    
    def wrap_output(self, obj, how=..., names=...):
        ...
    
    def attach_columns(self, result):
        ...
    
    def attach_columns_eq(self, result):
        ...
    
    def attach_cov(self, result):
        ...
    
    def attach_cov_eq(self, result):
        ...
    
    def attach_rows(self, result):
        ...
    
    def attach_dates(self, result):
        ...
    
    def attach_mv_confint(self, result):
        ...
    
    def attach_generic_columns(self, result, *args, **kwargs):
        ...
    
    def attach_generic_columns_2d(self, result, *args, **kwargs):
        ...
    
    def attach_ynames(self, result):
        ...
    


class PatsyData(ModelData):
    ...


class PandasData(ModelData):
    """
    Data handling class which knows how to reattach pandas metadata to model
    results
    """
    def attach_generic_columns(self, result, names):
        ...
    
    def attach_generic_columns_2d(self, result, rownames, colnames=...):
        ...
    
    def attach_columns(self, result):
        ...
    
    def attach_columns_eq(self, result):
        ...
    
    def attach_cov(self, result):
        ...
    
    def attach_cov_eq(self, result):
        ...
    
    def attach_rows(self, result):
        ...
    
    def attach_dates(self, result):
        ...
    
    def attach_mv_confint(self, result):
        ...
    
    def attach_ynames(self, result):
        ...
    


def handle_missing(endog, exog=..., missing=..., **kwargs):
    ...

def handle_data_class_factory(endog, exog):
    """
    Given inputs
    """
    ...

def handle_data(endog, exog, missing=..., hasconst=..., **kwargs):
    ...


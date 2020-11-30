"""
This type stub file was generated by pyright.
"""

class MPLConfigurator(object):
    def __init__(self) -> None:
        ...
    
    def revert(self):
        ...
    
    def set_fontsize(self, size):
        ...
    


def plot_mts(Y, names=..., index=...):
    """
    Plot multiple time series
    """
    ...

def plot_var_forc(prior, forc, err_upper, err_lower, index=..., names=..., plot_stderr=..., legend_options=...):
    ...

def plot_with_error(y, error, x=..., axes=..., value_fmt=..., error_fmt=..., alpha=..., stderr_type=...):
    """
    Make plot with optional error bars

    Parameters
    ----------
    y :
    error : array or None
    """
    ...

def plot_full_acorr(acorr, fontsize=..., linewidth=..., xlabel=..., err_bound=...):
    """

    Parameters
    ----------
    """
    ...

def acorr_plot(acorr, linewidth=..., xlabel=..., ax=...):
    ...

def plot_acorr_with_error():
    ...

def adjust_subplots(**kwds):
    ...

def irf_grid_plot(values, stderr, impcol, rescol, names, title, signif=..., hlines=..., subplot_params=..., plot_params=..., figsize=..., stderr_type=...):
    """
    Reusable function to make flexible grid plots of impulse responses and
    comulative effects

    values : (T + 1) x k x k
    stderr : T x k x k
    hlines : k x k
    """
    ...

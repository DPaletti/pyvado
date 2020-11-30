"""
This type stub file was generated by pyright.
"""

from pymoo.util.termination.collection import TerminationCollection

class SlidingWindowTermination(TerminationCollection):
    def __init__(self, metric_window_size=..., data_window_size=..., min_data_for_metric=..., nth_gen=..., n_max_gen=..., n_max_evals=..., truncate_metrics=..., truncate_data=...) -> None:
        """

        Parameters
        ----------

        metric_window_size : int
            The last generations that should be considering during the calculations

        data_window_size : int
            How much of the history should be kept in memory based on a sliding window.

        nth_gen : int
            Each n-th generation the termination should be checked for

        """
        ...
    
    def get_metric(self):
        ...
    



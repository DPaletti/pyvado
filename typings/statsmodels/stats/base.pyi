"""
This type stub file was generated by pyright.
"""

from statsmodels.tools.testing import Holder

"""Base classes for statistical test results

Created on Mon Apr 22 14:03:21 2013

Author: Josef Perktold
"""
class HolderTuple(Holder):
    """Holder class with indexing

    """
    def __init__(self, tuple_=..., **kwds) -> None:
        ...
    
    def __iter__(self):
        ...
    
    def __getitem__(self, idx):
        ...
    
    def __len__(self):
        ...
    
    def __array__(self, dtype=...):
        ...
    


class AllPairsResults(object):
    '''Results class for pairwise comparisons, based on p-values

    Parameters
    ----------
    pvals_raw : array_like, 1-D
        p-values from a pairwise comparison test
    all_pairs : list of tuples
        list of indices, one pair for each comparison
    multitest_method : str
        method that is used by default for p-value correction. This is used
        as default by the methods like if the multiple-testing method is not
        specified as argument.
    levels : {list[str], None}
        optional names of the levels or groups
    n_levels : None or int
        If None, then the number of levels or groups is inferred from the
        other arguments. It can be explicitly specified, if the inferred
        number is incorrect.

    Notes
    -----
    This class can also be used for other pairwise comparisons, for example
    comparing several treatments to a control (as in Dunnet's test).

    '''
    def __init__(self, pvals_raw, all_pairs, multitest_method=..., levels=..., n_levels=...) -> None:
        ...
    
    def pval_corrected(self, method=...):
        '''p-values corrected for multiple testing problem

        This uses the default p-value correction of the instance stored in
        ``self.multitest_method`` if method is None.

        '''
        ...
    
    def __str__(self) -> str:
        ...
    
    def pval_table(self):
        '''create a (n_levels, n_levels) array with corrected p_values

        this needs to improve, similar to R pairwise output
        '''
        ...
    
    def summary(self):
        '''returns text summarizing the results

        uses the default pvalue correction of the instance stored in
        ``self.multitest_method``
        '''
        ...
    


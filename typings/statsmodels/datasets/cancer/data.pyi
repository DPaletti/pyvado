"""
This type stub file was generated by pyright.
"""

"""Breast Cancer Data"""
__docformat__ = 'restructuredtext'
COPYRIGHT = """???"""
TITLE = """Breast Cancer Data"""
SOURCE = """
This is the breast cancer data used in Owen's empirical likelihood.  It is taken from
Rice, J.A. Mathematical Statistics and Data Analysis.
http://www.cengage.com/statistics/discipline_content/dataLibrary.html
"""
DESCRSHORT = """Breast Cancer and county population"""
DESCRLONG = """The number of breast cancer observances in various counties"""
NOTE = """::

    Number of observations: 301
    Number of variables: 2
    Variable name definitions:

        cancer - The number of breast cancer observances
        population - The population of the county

"""
def load_pandas():
    ...

def load(as_pandas=...):
    """
    Load the data and return a Dataset class instance.

    Parameters
    ----------
    as_pandas : bool
        Flag indicating whether to return pandas DataFrames and Series
        or numpy recarrays and arrays.  If True, returns pandas.

    Returns
    -------
    Dataset
        See DATASET_PROPOSAL.txt for more information.
    """
    ...

"""
This type stub file was generated by pyright.
"""

"""
Created on Fri Dec 19 11:29:18 2014

Author: Josef Perktold
License: BSD-3

"""
class PredictionResults(object):
    def __init__(self, predicted_mean, var_pred_mean, var_resid=..., df=..., dist=..., row_labels=..., linpred=..., link=...) -> None:
        ...
    
    @property
    def se_obs(self):
        ...
    
    @property
    def se_mean(self):
        ...
    
    @property
    def tvalues(self):
        ...
    
    def t_test(self, value=..., alternative=...):
        '''z- or t-test for hypothesis that mean is equal to value

        Parameters
        ----------
        value : array_like
            value under the null hypothesis
        alternative : str
            'two-sided', 'larger', 'smaller'

        Returns
        -------
        stat : ndarray
            test statistic
        pvalue : ndarray
            p-value of the hypothesis test, the distribution is given by
            the attribute of the instance, specified in `__init__`. Default
            if not specified is the normal distribution.

        '''
        ...
    
    def conf_int(self, method=..., alpha=..., **kwds):
        """
        Returns the confidence interval of the value, `effect` of the
        constraint.

        This is currently only available for t and z tests.

        Parameters
        ----------
        alpha : float, optional
            The significance level for the confidence interval.
            ie., The default `alpha` = .05 returns a 95% confidence interval.

        kwds : extra keyword arguments
            currently ignored, only for compatibility, consistent signature

        Returns
        -------
        ci : ndarray, (k_constraints, 2)
            The array has the lower and the upper limit of the confidence
            interval in the columns.
        """
        ...
    
    def summary_frame(self, alpha=...):
        """Summary frame"""
        ...
    


def get_prediction_glm(self, exog=..., transform=..., weights=..., row_labels=..., linpred=..., link=..., pred_kwds=...):
    """
    compute prediction results

    Parameters
    ----------
    exog : array_like, optional
        The values for which you want to predict.
    transform : bool, optional
        If the model was fit via a formula, do you want to pass
        exog through the formula. Default is True. E.g., if you fit
        a model y ~ log(x1) + log(x2), and transform is True, then
        you can pass a data structure that contains x1 and x2 in
        their original form. Otherwise, you'd need to log the data
        first.
    weights : array_like, optional
        Weights interpreted as in WLS, used for the variance of the predicted
        residual.
    *args :
        Some models can take additional arguments. See the
        predict method of the model for the details.
    **kwargs :
        Some models can take additional keyword arguments. See the
        predict method of the model for the details.

    Returns
    -------
    prediction_results : generalized_linear_model.PredictionResults
        The prediction results instance contains prediction and prediction
        variance and can on demand calculate confidence intervals and summary
        tables for the prediction of the mean and of new observations.
    """
    ...

def params_transform_univariate(params, cov_params, link=..., transform=..., row_labels=...):
    """
    results for univariate, nonlinear, monotonicaly transformed parameters

    This provides transformed values, standard errors and confidence interval
    for transformations of parameters, for example in calculating rates with
    `exp(params)` in the case of Poisson or other models with exponential
    mean function.
    """
    ...


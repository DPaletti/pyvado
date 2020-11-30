"""
This type stub file was generated by pyright.
"""

"""Statistical power, solving for nobs, ... - trial version

Created on Sat Jan 12 21:48:06 2013

Author: Josef Perktold

Example
roundtrip - root with respect to all variables

       calculated, desired
nobs   33.367204205 33.367204205
effect 0.5 0.5
alpha  0.05 0.05
power   0.8 0.8


TODO:
refactoring
 - rename beta -> power,    beta (type 2 error is beta = 1-power)  DONE
 - I think the current implementation can handle any kinds of extra keywords
   (except for maybe raising meaningful exceptions
 - streamline code, I think internally classes can be merged
   how to extend to k-sample tests?
   user interface for different tests that map to the same (internal) test class
 - sequence of arguments might be inconsistent,
   arg and/or kwds so python checks what's required and what can be None.
 - templating for docstrings ?


"""
def ttest_power(effect_size, nobs, alpha, df=..., alternative=...):
    '''Calculate power of a ttest
    '''
    ...

def normal_power(effect_size, nobs, alpha, alternative=..., sigma=...):
    """Calculate power of a normal distributed test statistic

    This is an generalization of `normal_power` when variance under Null and
    Alternative differ.

    Parameters
    ----------
    effect size : float
        difference in the estimated means or statistics under the alternative
        normalized by the standard deviation (without division by sqrt(nobs).
    nobs : float or int
        number of observations
    alpha : float in interval (0,1)
        significance level, e.g. 0.05, is the probability of a type I
        error, that is wrong rejections if the Null Hypothesis is true.
    alternative : string, 'two-sided' (default), 'larger', 'smaller'
        extra argument to choose whether the power is calculated for a
        two-sided (default) or one sided test. The one-sided test can be
        either 'larger', 'smaller'.
    """
    ...

def normal_power_het(diff, nobs, alpha, std_null=..., std_alternative=..., alternative=...):
    """Calculate power of a normal distributed test statistic

    This is an generalization of `normal_power` when variance under Null and
    Alternative differ.

    Parameters
    ----------
    diff : float
        difference in the estimated means or statistics under the alternative.
    nobs : float or int
        number of observations
    alpha : float in interval (0,1)
        significance level, e.g. 0.05, is the probability of a type I
        error, that is wrong rejections if the Null Hypothesis is true.
    std_null : float
        standard deviation under the Null hypothesis without division by
        sqrt(nobs)
    std_null : float
        standard deviation under the Alternative hypothesis without division
        by sqrt(nobs)
    alternative : string, 'two-sided' (default), 'larger', 'smaller'
        extra argument to choose whether the power is calculated for a
        two-sided (default) or one sided test. The one-sided test can be
        either 'larger', 'smaller'.

    Returns
    -------
    power : float
    """
    ...

def normal_sample_size_one_tail(diff, power, alpha, std_null=..., std_alternative=...):
    """explicit sample size computation if only one tail is relevant

    The sample size is based on the power in one tail assuming that the
    alternative is in the tail where the test has power that increases
    with sample size.
    Use alpha/2 to compute the one tail approximation to the two-sided
    test, i.e. consider only one tail of two-sided test.

    Parameters
    ----------
    diff : float
        difference in the estimated means or statistics under the alternative.
    power : float in interval (alpha, 1)
        number of observations
    alpha : float in interval (0,1)
        significance level, e.g. 0.05, is the probability of a type I
        error, that is wrong rejections if the Null Hypothesis is true.
    std_null : float
        standard deviation under the Null hypothesis without division by
        sqrt(nobs)
    std_null : float
        standard deviation under the Alternative hypothesis without division
        by sqrt(nobs)

    Returns
    -------
    nobs : float
        sample size to achieve the desired power

    """
    ...

def ftest_anova_power(effect_size, nobs, alpha, k_groups=..., df=...):
    '''power for ftest for one way anova with k equal sized groups

    nobs total sample size, sum over all groups

    should be general nobs observations, k_groups restrictions ???
    '''
    ...

def ftest_power(effect_size, df_num, df_denom, alpha, ncc=...):
    '''Calculate the power of a F-test.

    Parameters
    ----------
    effect_size : float
        standardized effect size, mean divided by the standard deviation.
        effect size has to be positive.
    df_num : int or float
        numerator degrees of freedom.
    df_denom : int or float
        denominator degrees of freedom.
    alpha : float in interval (0,1)
        significance level, e.g. 0.05, is the probability of a type I
        error, that is wrong rejections if the Null Hypothesis is true.
    ncc : int
        degrees of freedom correction for non-centrality parameter.
        see Notes

    Returns
    -------
    power : float
        Power of the test, e.g. 0.8, is one minus the probability of a
        type II error. Power is the probability that the test correctly
        rejects the Null Hypothesis if the Alternative Hypothesis is true.

    Notes
    -----

    sample size is given implicitly by df_num

    set ncc=0 to match t-test, or f-test in LikelihoodModelResults.
    ncc=1 matches the non-centrality parameter in R::pwr::pwr.f2.test

    ftest_power with ncc=0 should also be correct for f_test in regression
    models, with df_num and d_denom as defined there. (not verified yet)
    '''
    ...

class Power(object):
    '''Statistical Power calculations, Base Class

    so far this could all be class methods
    '''
    def __init__(self, **kwds) -> None:
        ...
    
    def power(self, *args, **kwds):
        ...
    
    def solve_power(self, **kwds):
        '''solve for any one of the parameters of a t-test

        for t-test the keywords are:
            effect_size, nobs, alpha, power

        exactly one needs to be ``None``, all others need numeric values

        *attaches*

        cache_fit_res : list
            Cache of the result of the root finding procedure for the latest
            call to ``solve_power``, mainly for debugging purposes.
            The first element is the success indicator, one if successful.
            The remaining elements contain the return information of the up to
            three solvers that have been tried.


        '''
        ...
    
    def plot_power(self, dep_var=..., nobs=..., effect_size=..., alpha=..., ax=..., title=..., plt_kwds=..., **kwds):
        """
        Plot power with number of observations or effect size on x-axis

        Parameters
        ----------
        dep_var : {'nobs', 'effect_size', 'alpha'}
            This specifies which variable is used for the horizontal axis.
            If dep_var='nobs' (default), then one curve is created for each
            value of ``effect_size``. If dep_var='effect_size' or alpha, then
            one curve is created for each value of ``nobs``.
        nobs : {scalar, array_like}
            specifies the values of the number of observations in the plot
        effect_size : {scalar, array_like}
            specifies the values of the effect_size in the plot
        alpha : {float, array_like}
            The significance level (type I error) used in the power
            calculation. Can only be more than a scalar, if ``dep_var='alpha'``
        ax : None or axis instance
            If ax is None, than a matplotlib figure is created. If ax is a
            matplotlib axis instance, then it is reused, and the plot elements
            are created with it.
        title : str
            title for the axis. Use an empty string, ``''``, to avoid a title.
        plt_kwds : {None, dict}
            not used yet
        kwds : dict
            These remaining keyword arguments are used as arguments to the
            power function. Many power function support ``alternative`` as a
            keyword argument, two-sample test support ``ratio``.

        Returns
        -------
        Figure
            If `ax` is None, the created figure.  Otherwise the figure to which
            `ax` is connected.

        Notes
        -----
        This works only for classes where the ``power`` method has
        ``effect_size``, ``nobs`` and ``alpha`` as the first three arguments.
        If the second argument is ``nobs1``, then the number of observations
        in the plot are those for the first sample.
        TODO: fix this for FTestPower and GofChisquarePower

        TODO: maybe add line variable, if we want more than nobs and effectsize
        """
        ...
    


class TTestPower(Power):
    '''Statistical Power calculations for one sample or paired sample t-test

    '''
    def power(self, effect_size, nobs, alpha, df=..., alternative=...):
        '''Calculate the power of a t-test for one sample or paired samples.

        Parameters
        ----------
        effect_size : float
            standardized effect size, mean divided by the standard deviation.
            effect size has to be positive.
        nobs : int or float
            sample size, number of observations.
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        df : int or float
            degrees of freedom. By default this is None, and the df from the
            one sample or paired ttest is used, ``df = nobs1 - 1``
        alternative : str, 'two-sided' (default), 'larger', 'smaller'
            extra argument to choose whether the power is calculated for a
            two-sided (default) or one sided test. The one-sided test can be
            either 'larger', 'smaller'.
            .

        Returns
        -------
        power : float
            Power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

       '''
        ...
    
    def solve_power(self, effect_size=..., nobs=..., alpha=..., power=..., alternative=...):
        '''solve for any one parameter of the power of a one sample t-test

        for the one sample t-test the keywords are:
            effect_size, nobs, alpha, power

        Exactly one needs to be ``None``, all others need numeric values.

        This test can also be used for a paired t-test, where effect size is
        defined in terms of the mean difference, and nobs is the number of
        pairs.

        Parameters
        ----------
        effect_size : float
            standardized effect size, mean divided by the standard deviation.
            effect size has to be positive.
        nobs : int or float
            sample size, number of observations.
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        power : float in interval (0,1)
            power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.
        alternative : str, 'two-sided' (default) or 'one-sided'
            extra argument to choose whether the power is calculated for a
            two-sided (default) or one sided test.
            'one-sided' assumes we are in the relevant tail.

        Returns
        -------
        value : float
            The value of the parameter that was set to None in the call. The
            value solves the power equation given the remaining parameters.

        *attaches*

        cache_fit_res : list
            Cache of the result of the root finding procedure for the latest
            call to ``solve_power``, mainly for debugging purposes.
            The first element is the success indicator, one if successful.
            The remaining elements contain the return information of the up to
            three solvers that have been tried.

        Notes
        -----
        The function uses scipy.optimize for finding the value that satisfies
        the power equation. It first uses ``brentq`` with a prior search for
        bounds. If this fails to find a root, ``fsolve`` is used. If ``fsolve``
        also fails, then, for ``alpha``, ``power`` and ``effect_size``,
        ``brentq`` with fixed bounds is used. However, there can still be cases
        where this fails.

        '''
        ...
    


class TTestIndPower(Power):
    '''Statistical Power calculations for t-test for two independent sample

    currently only uses pooled variance

    '''
    def power(self, effect_size, nobs1, alpha, ratio=..., df=..., alternative=...):
        '''Calculate the power of a t-test for two independent sample

        Parameters
        ----------
        effect_size : float
            standardized effect size, difference between the two means divided
            by the standard deviation. `effect_size` has to be positive.
        nobs1 : int or float
            number of observations of sample 1. The number of observations of
            sample two is ratio times the size of sample 1,
            i.e. ``nobs2 = nobs1 * ratio``
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        ratio : float
            ratio of the number of observations in sample 2 relative to
            sample 1. see description of nobs1
            The default for ratio is 1; to solve for ratio given the other
            arguments, it has to be explicitly set to None.
        df : int or float
            degrees of freedom. By default this is None, and the df from the
            ttest with pooled variance is used, ``df = (nobs1 - 1 + nobs2 - 1)``
        alternative : str, 'two-sided' (default), 'larger', 'smaller'
            extra argument to choose whether the power is calculated for a
            two-sided (default) or one sided test. The one-sided test can be
            either 'larger', 'smaller'.

        Returns
        -------
        power : float
            Power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

        '''
        ...
    
    def solve_power(self, effect_size=..., nobs1=..., alpha=..., power=..., ratio=..., alternative=...):
        '''solve for any one parameter of the power of a two sample t-test

        for t-test the keywords are:
            effect_size, nobs1, alpha, power, ratio

        exactly one needs to be ``None``, all others need numeric values

        Parameters
        ----------
        effect_size : float
            standardized effect size, difference between the two means divided
            by the standard deviation. `effect_size` has to be positive.
        nobs1 : int or float
            number of observations of sample 1. The number of observations of
            sample two is ratio times the size of sample 1,
            i.e. ``nobs2 = nobs1 * ratio``
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        power : float in interval (0,1)
            power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.
        ratio : float
            ratio of the number of observations in sample 2 relative to
            sample 1. see description of nobs1
            The default for ratio is 1; to solve for ratio given the other
            arguments it has to be explicitly set to None.
        alternative : str, 'two-sided' (default), 'larger', 'smaller'
            extra argument to choose whether the power is calculated for a
            two-sided (default) or one sided test. The one-sided test can be
            either 'larger', 'smaller'.

        Returns
        -------
        value : float
            The value of the parameter that was set to None in the call. The
            value solves the power equation given the remaining parameters.


        Notes
        -----
        The function uses scipy.optimize for finding the value that satisfies
        the power equation. It first uses ``brentq`` with a prior search for
        bounds. If this fails to find a root, ``fsolve`` is used. If ``fsolve``
        also fails, then, for ``alpha``, ``power`` and ``effect_size``,
        ``brentq`` with fixed bounds is used. However, there can still be cases
        where this fails.

        '''
        ...
    


class NormalIndPower(Power):
    '''Statistical Power calculations for z-test for two independent samples.

    currently only uses pooled variance

    '''
    def __init__(self, ddof=..., **kwds) -> None:
        ...
    
    def power(self, effect_size, nobs1, alpha, ratio=..., alternative=...):
        '''Calculate the power of a z-test for two independent sample

        Parameters
        ----------
        effect_size : float
            standardized effect size, difference between the two means divided
            by the standard deviation. effect size has to be positive.
        nobs1 : int or float
            number of observations of sample 1. The number of observations of
            sample two is ratio times the size of sample 1,
            i.e. ``nobs2 = nobs1 * ratio``
            ``ratio`` can be set to zero in order to get the power for a
            one sample test.
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        ratio : float
            ratio of the number of observations in sample 2 relative to
            sample 1. see description of nobs1
        alternative : str, 'two-sided' (default), 'larger', 'smaller'
            extra argument to choose whether the power is calculated for a
            two-sided (default) or one sided test. The one-sided test can be
            either 'larger', 'smaller'.

        Returns
        -------
        power : float
            Power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

        '''
        ...
    
    def solve_power(self, effect_size=..., nobs1=..., alpha=..., power=..., ratio=..., alternative=...):
        '''solve for any one parameter of the power of a two sample z-test

        for z-test the keywords are:
            effect_size, nobs1, alpha, power, ratio

        exactly one needs to be ``None``, all others need numeric values

        Parameters
        ----------
        effect_size : float
            standardized effect size, difference between the two means divided
            by the standard deviation.
            If ratio=0, then this is the standardized mean in the one sample
            test.
        nobs1 : int or float
            number of observations of sample 1. The number of observations of
            sample two is ratio times the size of sample 1,
            i.e. ``nobs2 = nobs1 * ratio``
            ``ratio`` can be set to zero in order to get the power for a
            one sample test.
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        power : float in interval (0,1)
            power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.
        ratio : float
            ratio of the number of observations in sample 2 relative to
            sample 1. see description of nobs1
            The default for ratio is 1; to solve for ration given the other
            arguments it has to be explicitly set to None.
        alternative : str, 'two-sided' (default), 'larger', 'smaller'
            extra argument to choose whether the power is calculated for a
            two-sided (default) or one sided test. The one-sided test can be
            either 'larger', 'smaller'.

        Returns
        -------
        value : float
            The value of the parameter that was set to None in the call. The
            value solves the power equation given the remaining parameters.


        Notes
        -----
        The function uses scipy.optimize for finding the value that satisfies
        the power equation. It first uses ``brentq`` with a prior search for
        bounds. If this fails to find a root, ``fsolve`` is used. If ``fsolve``
        also fails, then, for ``alpha``, ``power`` and ``effect_size``,
        ``brentq`` with fixed bounds is used. However, there can still be cases
        where this fails.

        '''
        ...
    


class FTestPower(Power):
    '''Statistical Power calculations for generic F-test

    '''
    def power(self, effect_size, df_num, df_denom, alpha, ncc=...):
        '''Calculate the power of a F-test.

        Parameters
        ----------
        effect_size : float
            standardized effect size, mean divided by the standard deviation.
            effect size has to be positive.
        df_num : int or float
            numerator degrees of freedom.
        df_denom : int or float
            denominator degrees of freedom.
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        ncc : int
            degrees of freedom correction for non-centrality parameter.
            see Notes

        Returns
        -------
        power : float
            Power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

        Notes
        -----

        sample size is given implicitly by df_num

        set ncc=0 to match t-test, or f-test in LikelihoodModelResults.
        ncc=1 matches the non-centrality parameter in R::pwr::pwr.f2.test

        ftest_power with ncc=0 should also be correct for f_test in regression
        models, with df_num and d_denom as defined there. (not verified yet)
        '''
        ...
    
    def solve_power(self, effect_size=..., df_num=..., df_denom=..., nobs=..., alpha=..., power=..., ncc=...):
        '''solve for any one parameter of the power of a F-test

        for the one sample F-test the keywords are:
            effect_size, df_num, df_denom, alpha, power

        Exactly one needs to be ``None``, all others need numeric values.


        Parameters
        ----------
        effect_size : float
            standardized effect size, mean divided by the standard deviation.
            effect size has to be positive.
        nobs : int or float
            sample size, number of observations.
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        power : float in interval (0,1)
            power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.
        alternative : str, 'two-sided' (default) or 'one-sided'
            extra argument to choose whether the power is calculated for a
            two-sided (default) or one sided test.
            'one-sided' assumes we are in the relevant tail.

        Returns
        -------
        value : float
            The value of the parameter that was set to None in the call. The
            value solves the power equation given the remaining parameters.


        Notes
        -----
        The function uses scipy.optimize for finding the value that satisfies
        the power equation. It first uses ``brentq`` with a prior search for
        bounds. If this fails to find a root, ``fsolve`` is used. If ``fsolve``
        also fails, then, for ``alpha``, ``power`` and ``effect_size``,
        ``brentq`` with fixed bounds is used. However, there can still be cases
        where this fails.

        '''
        ...
    


class FTestAnovaPower(Power):
    '''Statistical Power calculations F-test for one factor balanced ANOVA

    '''
    def power(self, effect_size, nobs, alpha, k_groups=...):
        '''Calculate the power of a F-test for one factor ANOVA.

        Parameters
        ----------
        effect_size : float
            standardized effect size, mean divided by the standard deviation.
            effect size has to be positive.
        nobs : int or float
            sample size, number of observations.
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        k_groups : int or float
            number of groups in the ANOVA or k-sample comparison. Default is 2.

        Returns
        -------
        power : float
            Power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

       '''
        ...
    
    def solve_power(self, effect_size=..., nobs=..., alpha=..., power=..., k_groups=...):
        '''solve for any one parameter of the power of a F-test

        for the one sample F-test the keywords are:
            effect_size, nobs, alpha, power

        Exactly one needs to be ``None``, all others need numeric values.


        Parameters
        ----------
        effect_size : float
            standardized effect size, mean divided by the standard deviation.
            effect size has to be positive.
        nobs : int or float
            sample size, number of observations.
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        power : float in interval (0,1)
            power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

        Returns
        -------
        value : float
            The value of the parameter that was set to None in the call. The
            value solves the power equation given the remaining parameters.


        Notes
        -----
        The function uses scipy.optimize for finding the value that satisfies
        the power equation. It first uses ``brentq`` with a prior search for
        bounds. If this fails to find a root, ``fsolve`` is used. If ``fsolve``
        also fails, then, for ``alpha``, ``power`` and ``effect_size``,
        ``brentq`` with fixed bounds is used. However, there can still be cases
        where this fails.

        '''
        ...
    


class GofChisquarePower(Power):
    '''Statistical Power calculations for one sample chisquare test

    '''
    def power(self, effect_size, nobs, alpha, n_bins, ddof=...):
        '''Calculate the power of a chisquare test for one sample

        Only two-sided alternative is implemented

        Parameters
        ----------
        effect_size : float
            standardized effect size, according to Cohen's definition.
            see :func:`statsmodels.stats.gof.chisquare_effectsize`
        nobs : int or float
            sample size, number of observations.
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        n_bins : int
            number of bins or cells in the distribution.

        Returns
        -------
        power : float
            Power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

       '''
        ...
    
    def solve_power(self, effect_size=..., nobs=..., alpha=..., power=..., n_bins=...):
        '''solve for any one parameter of the power of a one sample chisquare-test

        for the one sample chisquare-test the keywords are:
            effect_size, nobs, alpha, power

        Exactly one needs to be ``None``, all others need numeric values.

        n_bins needs to be defined, a default=2 is used.


        Parameters
        ----------
        effect_size : float
            standardized effect size, according to Cohen's definition.
            see :func:`statsmodels.stats.gof.chisquare_effectsize`
        nobs : int or float
            sample size, number of observations.
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        power : float in interval (0,1)
            power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.
        n_bins : int
            number of bins or cells in the distribution

        Returns
        -------
        value : float
            The value of the parameter that was set to None in the call. The
            value solves the power equation given the remaining parameters.


        Notes
        -----
        The function uses scipy.optimize for finding the value that satisfies
        the power equation. It first uses ``brentq`` with a prior search for
        bounds. If this fails to find a root, ``fsolve`` is used. If ``fsolve``
        also fails, then, for ``alpha``, ``power`` and ``effect_size``,
        ``brentq`` with fixed bounds is used. However, there can still be cases
        where this fails.

        '''
        ...
    


class _GofChisquareIndPower(Power):
    '''Statistical Power calculations for chisquare goodness-of-fit test

    TODO: this is not working yet
          for 2sample case need two nobs in function
          no one-sided chisquare test, is there one? use normal distribution?
          -> drop one-sided options?
    '''
    def power(self, effect_size, nobs1, alpha, ratio=..., alternative=...):
        '''Calculate the power of a chisquare for two independent sample

        Parameters
        ----------
        effect_size : float
            standardize effect size, difference between the two means divided
            by the standard deviation. effect size has to be positive.
        nobs1 : int or float
            number of observations of sample 1. The number of observations of
            sample two is ratio times the size of sample 1,
            i.e. ``nobs2 = nobs1 * ratio``
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        ratio : float
            ratio of the number of observations in sample 2 relative to
            sample 1. see description of nobs1
            The default for ratio is 1; to solve for ration given the other
            arguments it has to be explicitely set to None.
        alternative : str, 'two-sided' (default) or 'one-sided'
            extra argument to choose whether the power is calculated for a
            two-sided (default) or one sided test.
            'one-sided' assumes we are in the relevant tail.

        Returns
        -------
        power : float
            Power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.

        '''
        ...
    
    def solve_power(self, effect_size=..., nobs1=..., alpha=..., power=..., ratio=..., alternative=...):
        '''solve for any one parameter of the power of a two sample z-test

        for z-test the keywords are:
            effect_size, nobs1, alpha, power, ratio

        exactly one needs to be ``None``, all others need numeric values

        Parameters
        ----------
        effect_size : float
            standardize effect size, difference between the two means divided
            by the standard deviation.
        nobs1 : int or float
            number of observations of sample 1. The number of observations of
            sample two is ratio times the size of sample 1,
            i.e. ``nobs2 = nobs1 * ratio``
        alpha : float in interval (0,1)
            significance level, e.g. 0.05, is the probability of a type I
            error, that is wrong rejections if the Null Hypothesis is true.
        power : float in interval (0,1)
            power of the test, e.g. 0.8, is one minus the probability of a
            type II error. Power is the probability that the test correctly
            rejects the Null Hypothesis if the Alternative Hypothesis is true.
        ratio : float
            ratio of the number of observations in sample 2 relative to
            sample 1. see description of nobs1
            The default for ratio is 1; to solve for ration given the other
            arguments it has to be explicitely set to None.
        alternative : str, 'two-sided' (default) or 'one-sided'
            extra argument to choose whether the power is calculated for a
            two-sided (default) or one sided test.
            'one-sided' assumes we are in the relevant tail.

        Returns
        -------
        value : float
            The value of the parameter that was set to None in the call. The
            value solves the power equation given the remaining parameters.


        Notes
        -----
        The function uses scipy.optimize for finding the value that satisfies
        the power equation. It first uses ``brentq`` with a prior search for
        bounds. If this fails to find a root, ``fsolve`` is used. If ``fsolve``
        also fails, then, for ``alpha``, ``power`` and ``effect_size``,
        ``brentq`` with fixed bounds is used. However, there can still be cases
        where this fails.

        '''
        ...
    


tt_solve_power = TTestPower().solve_power
tt_ind_solve_power = TTestIndPower().solve_power
zt_ind_solve_power = NormalIndPower().solve_power

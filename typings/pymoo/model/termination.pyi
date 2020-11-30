"""
This type stub file was generated by pyright.
"""

class Termination:
    def __init__(self) -> None:
        """
        Base class for the implementation of a termination criterion for an algorithm.
        """
        ...
    
    def do_continue(self, algorithm):
        """

        Whenever the algorithm objects wants to know whether it should continue or not it simply
        asks the termination criterion for it.

        Parameters
        ----------
        algorithm : class
            The algorithm object that is asking if it has terminated or not.

        Returns
        -------
        do_continue : bool
            Whether the algorithm has terminated or not.

        """
        ...
    
    def has_terminated(self, algorithm):
        """
        Instead of asking if the algorithm should continue it can also ask if it has terminated.
        (just negates the continue method.)
        """
        ...
    



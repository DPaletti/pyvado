"""
This type stub file was generated by pyright.
"""

from pymoo.algorithms.genetic_algorithm import GeneticAlgorithm

class DE(GeneticAlgorithm):
    def __init__(self, pop_size=..., sampling=..., variant=..., CR=..., F=..., dither=..., jitter=..., display=..., **kwargs) -> None:
        """

        Parameters
        ----------

        pop_size : {pop_size}

        sampling : {sampling}

        variant : {{DE/(rand|best)/1/(bin/exp)}}
         The different variants of DE to be used. DE/x/y/z where x how to select individuals to be pertubed,
         y the number of difference vector to be used and z the crossover type. One of the most common variant
         is DE/rand/1/bin.

        F : float
         The weight to be used during the crossover.

        CR : float
         The probability the individual exchanges variable values from the donor vector.

        dither : {{'no', 'scalar', 'vector'}}
         One strategy to introduce adaptive weights (F) during one run. The option allows
         the same dither to be used in one iteration ('scalar') or a different one for
         each individual ('vector).

        jitter : bool
         Another strategy for adaptive weights (F). Here, only a very small value is added or
         subtracted to the weight used for the crossover for each individual.


        """
        ...
    



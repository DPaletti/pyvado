"""
This type stub file was generated by pyright.
"""

from pymoo.configuration import Configuration
from pymoo.problems.many import *
from pymoo.problems.multi import *
from pymoo.problems.single import *

"""
This module is a factory method what allows to import various objects, such as algorithms, crossover, mutation.

The definitions for each object are purposely defined as a list and not as a dictionary to keep an order for the documentation.


"""
def get_from_list(l, name, args, kwargs):
    ...

def get_algorithm_options():
    ...

def get_algorithm(name, *args, d=..., **kwargs):
    ...

def get_sampling_options():
    ...

def get_sampling(name, *args, d=..., **kwargs):
    ...

def get_selection_options():
    ...

def get_selection(name, *args, d=..., **kwargs):
    ...

def get_crossover_options():
    ...

def get_crossover(name, *args, d=..., **kwargs):
    ...

def get_mutation_options():
    ...

def get_mutation(name, *args, d=..., **kwargs):
    ...

def get_termination_options():
    ...

def get_termination(name, *args, d=..., **kwargs):
    ...

def get_problem_options():
    ...

def get_problem(name, *args, d=..., **kwargs):
    ...

def get_reference_direction_options():
    ...

def get_reference_directions(name, *args, d=..., **kwargs):
    ...

def get_visualization_options():
    ...

def get_visualization(name, *args, d=..., **kwargs):
    ...

def get_performance_indicator_options():
    ...

def get_performance_indicator(name, *args, d=..., **kwargs):
    ...

def get_decomposition_options():
    ...

def get_decomposition(name, *args, d=..., **kwargs):
    ...

def get_decision_making_options():
    ...

def get_decision_making(name, *args, d=..., **kwargs):
    ...

def dummy(name, kwargs):
    """
    A convenience method to get a {type} object just by providing a string.

    Parameters
    ----------

    name : {{ {options} }}
        Name of the {type}.

    kwargs : dict
        Dictionary that should be used to call the method mapped to the {type} factory function.

    Returns
    -------
    class : {clazz}
        An {type} object based on the string. `None` if the {type} was not found.

    """
    ...

def options_to_string(l):
    ...

if Configuration.parse_custom_docs:
    ...

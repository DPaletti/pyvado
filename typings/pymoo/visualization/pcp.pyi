"""
This type stub file was generated by pyright.
"""

from pymoo.model.plot import Plot

class PCP(Plot):
    def __init__(self, bounds=..., show_bounds=..., n_ticks=..., normalize_each_axis=..., **kwargs) -> None:
        """

        Parallel Coordinate Plot


        Parameters
        ----------------

        bounds : {bounds}

        axis_style : {axis_style}

        labels : {labels}

        n_ticks : int
            Number of ticks to be shown on each parallel axis.

        show_bounds : bool
            Whether the value of the boundaries are shown in the plot or not.

        normalize_each_axis : bool
            Whether the values should be normalized either by bounds or implictly.

        Other Parameters
        ----------------

        figsize : {figsize}
        title : {title}
        legend : {legend}
        tight_layout : {tight_layout}
        cmap : {cmap}

        """
        ...
    



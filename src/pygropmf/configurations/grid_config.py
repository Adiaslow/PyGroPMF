# pygropmf/configurations/grid_config.py
from dataclasses import dataclass
from typing import Tuple, Literal
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

@dataclass
class GridConfig:
    """Configuration for grid visualization."""
    cmap: str = 'viridis'
    figsize: Tuple[int, int] = (10, 8)
    dpi: int = 300
    plot_type: Literal['contour', 'heatmap'] = 'contour'
    levels: int = 20

    def __post_init__(self):
        """Validate configuration parameters."""
        # Validate colormap using matplotlib's built-in validation
        try:
            if self.cmap not in plt.colormaps():
                raise ValueError(
                    f"'{self.cmap}' is not a valid colormap. "
                    f"Please choose from: {', '.join(sorted(plt.colormaps()))}"
                )
        except Exception as e:
            raise ValueError(str(e))

        # Validate plot type
        valid_plot_types = ['contour', 'heatmap']
        if self.plot_type not in valid_plot_types:
            raise ValueError(
                f"'{self.plot_type}' is not a valid plot type. "
                f"Please choose from: {', '.join(valid_plot_types)}"
            )

        # Validate numeric parameters
        if not isinstance(self.levels, int) or self.levels <= 0:
            raise ValueError("levels must be a positive integer")

        if not isinstance(self.dpi, int) or self.dpi <= 0:
            raise ValueError("dpi must be a positive integer")

        if not isinstance(self.figsize, tuple) or len(self.figsize) != 2:
            raise ValueError("figsize must be a tuple of (width, height)")

        if not all(isinstance(x, (int, float)) and x > 0 for x in self.figsize):
            raise ValueError("figsize dimensions must be positive numbers")

    def __hash__(self):
        """Make GridConfig hashable for use as dict keys."""
        return hash((
            self.cmap,
            self.figsize,
            self.dpi,
            self.plot_type,
            self.levels
        ))

# pygropmf/visualizers/contour_visualizer.py

import matplotlib.pyplot as plt
from pathlib import Path
from ..configurations.grid_config import GridConfig
from ..core.results.pmf_result import PMFResult
from ..core.protocols.visualizer import Visualizer
from matplotlib.figure import Figure

class ContourVisualizer(Visualizer):
    """Creates contour plot visualizations of PMF data."""

    def __init__(self, config: GridConfig):
        """Initialize with configuration."""
        self.config = config
        if self.config.plot_type != 'contour':
            raise ValueError("ContourVisualizer requires plot_type='contour'")

    def _set_common_elements(self, fig: Figure, ax, mappable) -> None:
        """Set common plot elements."""
        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
        ax.set_title('Potential of Mean Force')
        fig.colorbar(mappable, ax=ax, label='Energy (kJ/mol)')

    def create_visualization(self, data: PMFResult) -> Figure:
        """Create a contour plot visualization."""
        fig, ax = plt.subplots(figsize=self.config.figsize, dpi=self.config.dpi)

        # Create contour plot and store the mappable
        contour = ax.contourf(
            data.x_coords,
            data.y_coords,
            data.pmf_values.T,
            levels=self.config.levels,
            cmap=self.config.cmap
        )

        # Pass the contour mappable to set_common_elements
        self._set_common_elements(fig, ax, contour)
        plt.tight_layout()

        return fig

    def save_visualization(self, figure: Figure, file_path: Path) -> None:
        """Save the visualization to a file."""
        figure.savefig(file_path, dpi=self.config.dpi, bbox_inches='tight')
        plt.close(figure)

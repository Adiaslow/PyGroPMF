# pygropmf/visualizers/heatmap_visualizer.py
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from ..configurations.grid_config import GridConfig
from ..core.results.grid_result import GridResult
from ..core.protocols.visualizer import Visualizer
from matplotlib.figure import Figure

class HeatmapVisualizer(Visualizer):
    """Creates heatmap visualizations of PMF data."""

    def __init__(self, config: GridConfig):
        """Initialize with configuration."""
        self.config = config
        if self.config.plot_type != 'heatmap':
            raise ValueError("HeatmapVisualizer requires plot_type='heatmap'")

    def create_visualization(self, data: GridResult) -> Figure:
        """Create a heatmap visualization."""
        fig, ax = plt.subplots(figsize=self.config.figsize, dpi=self.config.dpi)

        heatmap = ax.imshow(
            data.pmf_values.T,
            cmap=self.config.cmap,
            aspect='auto',
            extent=[
                data.x_coords.min(),
                data.x_coords.max(),
                data.y_coords.min(),
                data.y_coords.max()
            ],
            origin='lower'
        )

        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
        ax.set_title('Potential of Mean Force')

        plt.colorbar(heatmap, label='Energy (kJ/mol)', ax=ax)
        plt.tight_layout()

        return fig

    def save_visualization(self, figure: Figure, file_path: Path) -> None:
        """Save the visualization to a file."""
        figure.savefig(file_path, dpi=self.config.dpi, bbox_inches='tight')
        plt.close(figure)

    def _configure_axis(self, ax, data: GridResult):
        """Configure axis settings."""
        xticks = np.linspace(data.x_coords.min(), data.x_coords.max(), 5)
        yticks = np.linspace(data.y_coords.min(), data.y_coords.max(), 5)

        ax.set_xticks(xticks)
        ax.set_yticks(yticks)

        ax.set_xticklabels([f'{x:.1f}' for x in xticks])
        ax.set_yticklabels([f'{y:.1f}' for y in yticks])

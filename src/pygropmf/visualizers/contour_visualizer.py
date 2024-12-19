# src/pygropmf/visualizers/contour_visualizer.py
import logging
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from ..core.protocols.visualizer import Visualizer
from ..core.results.grid_result import GridResult
from ..configurations.grid_config import GridConfig

class ContourVisualizer(Visualizer):
    """Creates contour plot visualizations for PMF data"""

    def __init__(self, config: GridConfig):
        self.config = config

    def create_visualization(self, data: GridResult) -> Figure:
        try:
            fig, ax = plt.subplots(figsize=self.config.figsize)

            X, Y = np.meshgrid(data.x_coords, data.y_coords)
            contour = ax.contourf(X, Y, data.pmf_values.T,
                                levels=self.config.levels,
                                cmap=self.config.cmap)

            cbar = plt.colorbar(contour)
            cbar.set_label('PMF (kJ/mol)', rotation=270, labelpad=15)

            self._set_common_elements(ax, 'PMF Contour Plot')
            return fig

        except Exception as e:
            logging.error(f"Error creating contour plot: {e}")
            raise

    def save_visualization(self, figure: Figure, file_path: Path) -> None:
        try:
            figure.savefig(file_path, dpi=self.config.dpi, bbox_inches='tight')
            plt.close(figure)
        except Exception as e:
            logging.error(f"Error saving visualization to {file_path}: {e}")
            raise IOError(f"Failed to save visualization: {e}") from e

    def _set_common_elements(self, ax: Axes, title: str) -> None:
        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
        ax.set_title(title)

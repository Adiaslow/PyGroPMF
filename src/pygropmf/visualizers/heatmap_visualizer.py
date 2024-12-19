# src/pygropmf/visualizers/heatmap_visualizer.py

from pathlib import Path
from typing import Any
import logging
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns

from ..core.protocols import Visualizer
from ..core.results import GridResult

class HeatmapVisualizer(Visualizer):
    """Creates heatmap visualizations for PMF data using seaborn"""

    def __init__(self, cmap: str = 'viridis', figsize: tuple[int, int] = (10, 8)):
        self.cmap = cmap
        self.figsize = figsize

    def create_visualization(self, data: GridResult) -> Figure:
        """
        Create heatmap visualization

        Args:
            data: GridResult containing coordinates and PMF values

        Returns:
            matplotlib Figure object
        """
        try:
            # Create figure and axis
            fig, ax = plt.subplots(figsize=self.figsize)

            # Create heatmap using seaborn
            sns.heatmap(data.pmf_values.T,
                       cmap=self.cmap,
                       xticklabels=np.round(data.x_coords, 1),
                       yticklabels=np.round(data.y_coords, 1),
                       ax=ax)

            # Set labels and title
            ax.set_xlabel('PC1')
            ax.set_ylabel('PC2')
            ax.set_title('PMF Heatmap')

            return fig

        except Exception as e:
            logging.error(f"Error creating visualization: {e}")
            raise

    def save_visualization(self, figure: Figure, file_path: Path) -> None:
        """
        Save visualization to file

        Args:
            figure: matplotlib Figure to save
            file_path: Output file path
        """
        try:
            figure.savefig(file_path, dpi=300, bbox_inches='tight')
        except Exception as e:
            logging.error(f"Error saving visualization to {file_path}: {e}")
            raise IOError(f"Failed to save visualization: {e}") from e

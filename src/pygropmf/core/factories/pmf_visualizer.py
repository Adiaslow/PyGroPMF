# src/pygropmf/core/factories/pmf_visualizer.py

from pathlib import Path
from typing import Optional
import logging
from matplotlib.figure import Figure

from ..protocols import Visualizer
from ..results import GridResult
from ...configurations import GridConfig
from ...visualizers import ContourVisualizer
from ...visualizers import HeatmapVisualizer

class PMFVisualizer(Visualizer):
    """Factory class for creating and managing PMF visualizations"""
    def __init__(self, config: GridConfig):
        self.config = config
        self._visualizer = self._create_visualizer()

    def _create_visualizer(self) -> Visualizer:
        """Create appropriate visualizer based on configuration"""
        if self.config.plot_type == 'contour':
            return ContourVisualizer(self.config)
        elif self.config.plot_type == 'heatmap':
            return HeatmapVisualizer(self.config)
        else:
            raise ValueError(f"Unsupported plot type: {self.config.plot_type}")

    def create_visualization(self, data: GridResult) -> Figure:
        """Create visualization using the configured visualizer"""
        return self._visualizer.create_visualization(data)

    def save_visualization(self, figure: Figure, file_path: Path) -> None:
        """Save visualization using the configured visualizer"""
        self._visualizer.save_visualization(figure, file_path)

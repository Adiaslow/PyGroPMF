# src/pygropmf/core/protocols/visualizer.py
from matplotlib.figure import Figure
from pathlib import Path
from typing import Protocol, runtime_checkable
from ..results.grid_result import GridResult
from ...configurations.grid_config import GridConfig

@runtime_checkable
class Visualizer(Protocol):
    """Protocol defining the interface for visualization creators."""

    config: GridConfig

    def __init__(self, config: GridConfig) -> None:
        """Initialize visualizer with configuration."""
        ...

    def create_visualization(self, data: GridResult) -> Figure:
        """
        Create visualization and return the figure.

        Args:
            data: The grid result data to visualize

        Returns:
            A matplotlib Figure object containing the visualization

        Raises:
            ValueError: If the data is invalid or incompatible with the visualization
        """
        ...

    def save_visualization(self, figure: Figure, file_path: Path) -> None:
        """
        Save visualization to file.

        Args:
            figure: The matplotlib Figure to save
            file_path: Path where the figure should be saved

        Raises:
            IOError: If the file cannot be written
            ValueError: If the figure is invalid
        """
        ...

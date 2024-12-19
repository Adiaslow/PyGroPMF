# src/pygropmf/core/protocols/visualizer.py

from matplotlib.figure import Figure
from pathlib import Path
from typing import Protocol

from ..results.grid_result import GridResult

class Visualizer(Protocol):
    """Protocol defining the interface for visualization creators"""
    def create_visualization(self, data: GridResult) -> Figure:
        """Create visualization and return the figure"""
        ...

    def save_visualization(self, figure: Figure, file_path: Path) -> None:
        """Save visualization to file"""
        ...

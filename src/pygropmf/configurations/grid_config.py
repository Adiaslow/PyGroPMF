# src/pygropmf/configurations/grid_config.py

from dataclasses import dataclass
from typing import Literal

@dataclass
class GridConfig:
    """Configuration for PMF grid visualization"""
    cmap: str = 'coolwarm'
    figsize: tuple[int, int] = (10, 8)
    dpi: int = 300
    plot_type: Literal['contour', 'heatmap', 'surface'] = 'contour'
    levels: int = 20

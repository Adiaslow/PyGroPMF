# src/pygropmf/core/results/grid_result.py

from dataclasses import dataclass
from numpy import ndarray as NDArray

@dataclass
class GridResult:
    """Container for grid calculation results"""
    x_coords: NDArray
    y_coords: NDArray
    pmf_values: NDArray

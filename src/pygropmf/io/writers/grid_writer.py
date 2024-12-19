# pygropmf/io/writers/grid_writer.py
from pathlib import Path
import numpy as np
from ...core.results import PMFResult

class GridWriter:
    """Writes PMF results to grid format."""

    @staticmethod
    def write(filepath: Path, result: PMFResult) -> None:
        """Write PMF results to grid file."""
        with open(filepath, 'w') as f:
            for i in range(len(result.x_coords)):
                for j in range(len(result.y_coords)):
                    f.write(f"{result.x_coords[i]:10.3f} "
                           f"{result.y_coords[j]:10.3f} "
                           f"{result.pmf_values[i,j]:15.5f}\n")
                f.write("\n")

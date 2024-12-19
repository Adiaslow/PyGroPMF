# src/pygropmf/io/writers/grid_writer.py

from pathlib import Path
from ...core.results.pmf_result import PMFResult

class GridWriter:
    """Writes PMF results to grid format."""

    @staticmethod
    def write(filepath: Path, result: PMFResult) -> None:
        with open(filepath, 'w') as f:
            for i in range(result.pmf_values.shape[0]):
                for j in range(result.pmf_values.shape[1]):
                    f.write(f"{result.x_coords[i, j]:10.3f} {result.y_coords[i, j]:10.3f} {result.pmf_values[i, j]:15.5f}\n")
                f.write("\n")

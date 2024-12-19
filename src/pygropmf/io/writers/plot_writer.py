# pygropmf/io/writers/plot_writer.py
from pathlib import Path
import numpy as np
from ...core.results import PMFResult

class PlotWriter:
    """Writes PMF results to plot format."""

    @staticmethod
    def write(filepath: Path, result: PMFResult) -> None:
        """Write PMF results to plot file."""
        with open(filepath, 'w') as f:
            # Write header
            f.write("$ DATA=CONTOUR\n")

            # Write axis information
            x_min, x_max = result.x_coords.min(), result.x_coords.max()
            y_min, y_max = result.y_coords.min(), result.y_coords.max()
            f.write(f"% xmin={x_min:6.1f} xmax={x_max:6.1f}\n")
            f.write(f"% ymin={y_min:6.1f} ymax={y_max:6.1f}\n")

            # Write dimensions
            f.write(f"% nx={len(result.x_coords):2d} ny={len(result.y_coords):2d}\n")

            # Write tick labels
            for x in np.arange(np.floor(x_min/10)*10, np.ceil(x_max/10)*10, 10):
                f.write(f"% xticklabel= ({int(x)},{int(x)})\n")
            for y in np.arange(np.floor(y_min/10)*10, np.ceil(y_max/10)*10, 10):
                f.write(f"% yticklabel= ({int(y)},{int(y)})\n")

            # Write contour parameters
            f.write("% cmin= 0.0 cmax= 10.0\n")
            f.write("% nsteps= 10\n")
            f.write("% contfill\n")

            # Write data
            for i in range(len(result.y_coords)):
                values = " ".join(f"{v:15.5f}" for v in result.pmf_values[:,i])
                f.write(f"{values}\n")

            f.write("\n$ END\n")

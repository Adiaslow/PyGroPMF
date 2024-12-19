# pygropmf/io/readers/pca_reader.py
from pathlib import Path
import pandas as pd
import numpy as np
from typing import List
from ...core.data import PCAData

class PCAReader:
    """Reads and processes PCA data files."""

    def __init__(self, n_components: int):
        self.n_components = n_components

    def read(self, filepath: Path) -> PCAData:
        """Read PCA data from file."""
        df = pd.read_csv(filepath, sep=r'\s+', skiprows=1, header=None)

        if df.shape[1] != self.n_components + 1:
            raise ValueError(f"Dimension mismatch: Expected {self.n_components + 1} columns, found {df.shape[1]}")

        # First column is energy, remaining columns are components
        energy = df[0].values.astype(np.float64)
        components = df.iloc[:, 1:self.n_components + 1].values

        return PCAData(
            energy=energy,
            components=components
        )

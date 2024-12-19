# pygropmf/core/data/energy_pdf_data.py
from dataclasses import dataclass
import numpy as np
from numpy.typing import NDArray
import pandas as pd
from typing import Iterator, Tuple

@dataclass
class EnergyPDFData:
    """Represents energy probability density function data."""
    energy: NDArray[np.float64]
    probability: NDArray[np.float64]

    def __len__(self) -> int:
        """Return the length of the data."""
        return len(self.energy)

    def __getitem__(self, idx) -> Tuple[float, float]:
        """Enable indexing."""
        return self.energy[idx], self.probability[idx]

    def to_dataframe(self) -> pd.DataFrame:
        """Convert to pandas DataFrame."""
        return pd.DataFrame({
            'energy': self.energy,
            'probability': self.probability
        })

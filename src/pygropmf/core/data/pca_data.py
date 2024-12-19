# pygropmf/core/data/pca_data.py
from dataclasses import dataclass
import numpy as np
from numpy.typing import NDArray
import pandas as pd
from typing import Iterator

@dataclass
class PCAData:
    """Represents principal component analysis data."""
    energy: NDArray[np.float64]
    components: NDArray[np.float64]

    def __len__(self) -> int:
        """Return the length of the data."""
        return len(self.energy)

    def iterrows(self) -> Iterator[tuple[int, dict]]:
        """Implement pandas-like iterrows functionality."""
        for i in range(len(self.energy)):
            yield i, {
                'energy': self.energy[i],
                'components': self.components[i]
            }

    def to_dataframe(self) -> pd.DataFrame:
        """Convert to pandas DataFrame."""
        df = pd.DataFrame(self.components, columns=[f'comp_{i}' for i in range(self.components.shape[1])])
        df['energy'] = self.energy
        return df

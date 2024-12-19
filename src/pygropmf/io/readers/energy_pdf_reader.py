# pygropmf/io/readers/energy_pdf_reader.py
from pathlib import Path
import pandas as pd
import numpy as np
from ...core.data import EnergyPDFData

class EnergyPDFReader:
    """Reads and processes energy PDF files."""

    @staticmethod
    def read(filepath: Path) -> EnergyPDFData:
        df = pd.read_csv(filepath, sep=r'\s+', header=None, names=['energy', 'log_probability'])
        if df.empty:
            raise pd.errors.EmptyDataError("The file is empty")

        max_log_prob = df['log_probability'].max()
        probabilities = np.exp(df['log_probability'] - max_log_prob)
        probabilities[probabilities < 1e-11] = 0.0
        probabilities /= probabilities.sum()  # Normalize to sum to 1

        return EnergyPDFData(
            energy=df['energy'].values.astype(np.float64),
            probability=probabilities
        )

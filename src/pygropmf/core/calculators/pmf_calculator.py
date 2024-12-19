# src/pygropmf/core/calculators/pmf_calculator.py

import numpy as np
from scipy import constants
from typing import Tuple
from ..data.energy_pdf_data import EnergyPDFData
from ..data.pca_data import PCAData
from ..results.pmf_result import PMFResult
from ...configurations.pmf_config import PMFConfig

class PMFCalculator:
    """Modern implementation of the PMF calculation logic."""

    def __init__(self, config: PMFConfig):
        self.config = config
        self.const = constants.R * self.config.temperature / 1000  # kJ/mol

    def calculate_pmf(self, energy_pdf: EnergyPDFData, pca_data: PCAData) -> PMFResult:
        prob_sum = np.zeros((self.config.x_bin_size, self.config.y_bin_size))
        for _, row in pca_data.iterrows():
            energy = row['energy']
            prob = self._get_probability(energy, energy_pdf)

            components = row['components']
            px = components[self.config.x_axis]
            py = components[self.config.y_axis]

            if px < self.config.x_min or py < self.config.y_min:
                continue

            px_idx = int((px - self.config.x_min) / self.config.x_bin)
            py_idx = int((py - self.config.y_min) / self.config.y_bin)

            if px_idx >= self.config.x_bin_size or py_idx >= self.config.y_bin_size:
                continue

            prob_sum[px_idx, py_idx] += prob

        pmf_values = self._calculate_final_pmf(prob_sum)
        x_coords, y_coords = self._generate_grid_coordinates()
        return PMFResult(pmf_values=pmf_values, x_coords=x_coords, y_coords=y_coords)

    def _get_probability(self, energy: float, energy_pdf: EnergyPDFData) -> float:
        for i in range(1, len(energy_pdf)):
            e1, p1 = energy_pdf[i-1]
            e2, p2 = energy_pdf[i]
            if e1 <= energy < e2:
                frac = (energy - e1) / (e2 - e1)
                return p1 + frac * (p2 - p1)
        return 0.0

    def _calculate_final_pmf(self, prob_sum: np.ndarray) -> np.ndarray:
        mask = prob_sum != 0
        pmf = np.full_like(prob_sum, 50.0)
        pmf[mask] = -self.const * np.log(prob_sum[mask])

        min_val = np.min(pmf[mask]) if np.any(mask) else 0.0
        pmf[mask] -= min_val

        return pmf

    def _generate_grid_coordinates(self) -> Tuple[np.ndarray, np.ndarray]:
        x = np.linspace(
            self.config.x_min + self.config.x_bin / 2,
            self.config.x_min + (self.config.x_bin_size - 1) * self.config.x_bin + self.config.x_bin / 2,
            self.config.x_bin_size
        )
        y = np.linspace(
            self.config.y_min + self.config.y_bin / 2,
            self.config.y_min + (self.config.y_bin_size - 1) * self.config.y_bin + self.config.y_bin / 2,
            self.config.y_bin_size
        )
        return np.meshgrid(x, y)

    def get_grid_coordinates(self) -> Tuple[np.ndarray, np.ndarray]:
        return self._generate_grid_coordinates()

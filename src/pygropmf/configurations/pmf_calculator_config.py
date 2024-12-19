# src/pygropmf/configurations/pmf_calculator_config.py

from dataclasses import dataclass

@dataclass
class PMFCalculatorConfig:
    n_components: int
    x_axis: int
    y_axis: int
    x_min: float
    x_bin: float
    x_bin_size: int
    y_min: float
    y_bin: float
    y_bin_size: int
    temperature: float

# src/test/test_calculators.py
import pytest
import numpy as np
import json  # Import json to handle JSON operations
from pathlib import Path
from pygropmf.core.calculators.pmf_calculator import PMFCalculator
from pygropmf.configurations.pmf_config import PMFConfig
from pygropmf.core.data.energy_pdf_data import EnergyPDFData
from pygropmf.core.data.pca_data import PCAData
from pygropmf.core.results.pmf_result import PMFResult

@pytest.fixture
def calculator_config(tmp_path):
    # Create a temporary config file
    config_path = tmp_path / "config.json"
    config_data = {
        "temperature": 300.0,
        "x_bin_size": 20,
        "y_bin_size": 20,
        "x_axis": 0,
        "y_axis": 1,
        "x_min": -5.0,
        "x_bin": 0.5,
        "y_min": -5.0,
        "y_bin": 0.5,
        "ncomp": 2,
        "inppdf": str(tmp_path / "energy_pdf.csv"),
        "inppca": str(tmp_path / "pca.csv"),
        "outgrd": str(tmp_path / "out.grid"),
        "outplt": str(tmp_path / "out.plot")
    }
    config_path.write_text(json.dumps(config_data))
    return PMFConfig(config_path)

@pytest.fixture
def energy_pdf_data():
    energies = np.array([-10.0, -9.0, -8.0, -7.0, -6.0])
    probabilities = np.array([0.1, 0.2, 0.4, 0.2, 0.1])
    return EnergyPDFData(
        energy=energies,
        probability=probabilities
    )

@pytest.fixture
def pca_data():
    energy = np.array([-8.5, -7.5, -6.5])
    components = np.array([
        [0.0, 0.0],
        [2.0, 2.0],
        [4.0, 4.0]
    ])
    return PCAData(
        energy=energy,
        components=components
    )

def test_pmf_calculator_initialization(calculator_config):
    calculator = PMFCalculator(calculator_config)
    assert calculator.config == calculator_config
    assert np.isclose(calculator.const, 8.314462145e-3 * 300.0)

def test_get_probability(calculator_config, energy_pdf_data):
    calculator = PMFCalculator(calculator_config)
    prob = calculator._get_probability(-8.5, energy_pdf_data)
    assert np.isclose(prob, 0.3)  # Should interpolate between -9.0 and -8.0

def test_calculate_pmf(calculator_config, energy_pdf_data, pca_data):
    calculator = PMFCalculator(calculator_config)
    pmf_result = calculator.calculate_pmf(energy_pdf_data, pca_data)

    assert isinstance(pmf_result, PMFResult)
    assert pmf_result.pmf_values.shape == (20, 20)
    assert not np.any(np.isnan(pmf_result.pmf_values))
    assert np.all(pmf_result.pmf_values[pmf_result.pmf_values < 50.0] >= 0.0)  # PMF values should be non-negative
    assert np.any(pmf_result.pmf_values == 50.0)  # Should have some zero-probability regions

def test_get_grid_coordinates(calculator_config):
    calculator = PMFCalculator(calculator_config)
    x_grid, y_grid = calculator.get_grid_coordinates()

    assert x_grid.shape == (20, 20)
    assert y_grid.shape == (20, 20)
    assert np.isclose(x_grid[0, 0], -4.75)  # First point should be min + bin/2
    assert np.isclose(y_grid[0, 0], -4.75)

import pytest
import numpy as np
import pandas as pd
from pathlib import Path
from pygropmf.io.readers import EnergyPDFReader, PCAReader
from pygropmf.io.writers import PlotWriter
from pygropmf.core.results import PMFResult
from pygropmf.core.data import EnergyPDFData, PCAData

@pytest.fixture
def sample_energy_pdf_file(tmp_path):
    filepath = tmp_path / "energy.dat"
    content = """
-10.0  0.0
-9.0   -0.693147
-8.0   -1.386294
-7.0   -0.693147
-6.0   0.0
""".strip()
    filepath.write_text(content)
    return filepath

@pytest.fixture
def sample_pmf_result():
    x_coords = np.linspace(0, 1, 10)
    y_coords = np.linspace(0, 1, 10)
    pmf_values = np.outer(x_coords, y_coords)
    return PMFResult(pmf_values=pmf_values, x_coords=x_coords, y_coords=y_coords)

def test_energy_pdf_reader(sample_energy_pdf_file):
    reader = EnergyPDFReader()
    data = reader.read(sample_energy_pdf_file)

    assert isinstance(data, EnergyPDFData)
    assert len(data.energy) == 5
    assert len(data.probability) == 5

    total_prob = np.sum(data.probability)
    assert np.isclose(total_prob, 1.0, rtol=1e-5)
    assert np.all(data.probability >= 0)

def test_energy_pdf_reader_empty_file(tmp_path):
    filepath = tmp_path / "empty.dat"
    filepath.write_text("\n\n")  # Create file with only newlines
    reader = EnergyPDFReader()
    with pytest.raises((pd.errors.EmptyDataError, ValueError)):
        reader.read(filepath)

def test_pca_reader_dimension_mismatch(tmp_path):
    filepath = tmp_path / "mismatch.dat"
    content = """aaa
-8.5  0.0  0.0  0.0
-7.5  2.0  2.0  0.0
""".strip()
    filepath.write_text(content)
    reader = PCAReader(n_components=2)
    with pytest.raises((IndexError, ValueError)):
        reader.read(filepath)

def test_plot_writer(tmp_path, sample_pmf_result):
    output_path = tmp_path / "plot.plt"
    writer = PlotWriter()

    output_path.parent.mkdir(parents=True, exist_ok=True)

    writer.write(output_path, sample_pmf_result)
    assert output_path.exists()

    content = output_path.read_text()
    assert "$ DATA=CONTOUR" in content
    assert "% xmin=" in content
    assert "% ymin=" in content
    assert any("nx=" in line and "ny=" in line for line in content.split('\n'))
    assert "$ END" in content

    for line in content.split('\n'):
        if "nx=" in line and "ny=" in line:
            assert f"nx={len(sample_pmf_result.x_coords)}" in line
            assert f"ny={len(sample_pmf_result.y_coords)}" in line
            break

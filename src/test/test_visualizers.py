# tests/test_visualizers.py
import pytest
import numpy as np
from pathlib import Path
from pygropmf import GridResult, GridConfig, PMFVisualizer
from pygropmf.visualizers import ContourVisualizer, HeatmapVisualizer

@pytest.fixture
def sample_data():
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    Z = np.random.rand(50, 50)
    return GridResult(x_coords=x, y_coords=y, pmf_values=Z)

@pytest.fixture
def config():
    return GridConfig(plot_type='contour', cmap='viridis')

def test_contour_visualizer(sample_data, config, tmp_path):
    visualizer = ContourVisualizer(config)
    fig = visualizer.create_visualization(sample_data)
    output_path = tmp_path / "test_contour.png"
    visualizer.save_visualization(fig, output_path)
    assert output_path.exists()

def test_heatmap_visualizer(sample_data, config, tmp_path):
    config.plot_type = 'heatmap'
    visualizer = HeatmapVisualizer(config)
    fig = visualizer.create_visualization(sample_data)
    output_path = tmp_path / "test_heatmap.png"
    visualizer.save_visualization(fig, output_path)
    assert output_path.exists()

def test_pmf_visualizer_factory(sample_data, config, tmp_path):
    visualizer = PMFVisualizer(config)
    fig = visualizer.create_visualization(sample_data)
    output_path = tmp_path / "test_pmf.png"
    visualizer.save_visualization(fig, output_path)
    assert output_path.exists()

# src/test/test_visualizers.py
import pytest
import numpy as np
from pathlib import Path
from pygropmf import GridResult, GridConfig, PMFVisualizer
from pygropmf.visualizers import ContourVisualizer, HeatmapVisualizer

@pytest.fixture
def sample_data():
    """Create sample grid data for testing."""
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    Z = np.random.rand(50, 50)
    return GridResult(x_coords=x, y_coords=y, pmf_values=Z)

@pytest.fixture
def contour_config():
    """Create configuration for contour plots."""
    return GridConfig(
        plot_type='contour',
        cmap='viridis',
        figsize=(10, 8),
        dpi=300,
        levels=20
    )

@pytest.fixture
def heatmap_config():
    """Create configuration for heatmap plots."""
    return GridConfig(
        plot_type='heatmap',
        cmap='viridis',
        figsize=(10, 8),
        dpi=300,
        levels=20
    )

def test_contour_visualizer(sample_data, contour_config, tmp_path):
    """Test contour visualization creation and saving."""
    visualizer = ContourVisualizer(contour_config)
    fig = visualizer.create_visualization(sample_data)
    output_path = tmp_path / "test_contour.png"
    visualizer.save_visualization(fig, output_path)
    assert output_path.exists()

def test_heatmap_visualizer(sample_data, heatmap_config, tmp_path):
    """Test heatmap visualization creation and saving."""
    visualizer = HeatmapVisualizer(heatmap_config)
    fig = visualizer.create_visualization(sample_data)
    output_path = tmp_path / "test_heatmap.png"
    visualizer.save_visualization(fig, output_path)
    assert output_path.exists()

def test_pmf_visualizer_factory(sample_data, contour_config, tmp_path):
    """Test PMF visualizer factory with different configurations."""
    visualizer = PMFVisualizer(contour_config)
    fig = visualizer.create_visualization(sample_data)
    output_path = tmp_path / "test_pmf.png"
    visualizer.save_visualization(fig, output_path)
    assert output_path.exists()

def test_invalid_colormap():
    """Test that invalid colormap raises ValueError."""
    with pytest.raises(ValueError) as exc_info:
        GridConfig(cmap='invalid_colormap')
    assert "is not a valid colormap" in str(exc_info.value)

def test_invalid_plot_type():
    """Test that invalid plot type raises ValueError."""
    with pytest.raises(ValueError) as exc_info:
        GridConfig(plot_type='invalid_type')
    assert "is not a valid plot type" in str(exc_info.value)

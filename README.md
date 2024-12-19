# PyGroPMF

[![PyPI version](https://badge.fury.io/py/pygropmf.svg)](https://badge.fury.io/py/pygropmf)
[![Build Status](https://travis-ci.com/Adiaslow/PyGroPMF.svg?branch=main)](https://travis-ci.com/Adiaslow/PyGroPMF)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python package for visualizing Potential of Mean Force (PMF) data from GROMACS simulations.

## Installation

```bash
pip install pygropmf
```

## Quick Start

Here's a quick example to get you started with visualizing PMF data using PyGroPMF.

```python
import json
from pygropmf.configurations.pmf_config import PMFConfig
from pygropmf.configurations.grid_config import GridConfig
from pygropmf.io.readers.energy_pdf_reader import EnergyPDFReader
from pygropmf.io.readers.pca_reader import PCAReader
from pygropmf.core.calculators.pmf_calculator import PMFCalculator
from pygropmf.visualizers.contour_visualizer import ContourVisualizer
from pygropmf.visualizers.heatmap_visualizer import HeatmapVisualizer

# Load the configuration from a file
with open('path/to/config.json', 'r') as f:
    config_data = json.load(f)

pmf_config = PMFConfig(config_data['pmf_config'])
grid_config = GridConfig(config_data['grid_config'])

# Initialize readers, calculator, and visualizers
energy_pdf_path = pmf_config.inppdf
pca_path = pmf_config.inppca
out_contour_plot_path = grid_config.output_contour_plot
out_heatmap_plot_path = grid_config.output_heatmap_plot

energy_pdf_data = EnergyPDFReader.read(energy_pdf_path)
pca_reader = PCAReader(n_components=pmf_config.ncomp)
pca_data = pca_reader.read(pca_path)

pmf_calculator = PMFCalculator(pmf_config)
pmf_result = pmf_calculator.calculate_pmf(energy_pdf_data, pca_data)

# Use visualizers for visualization
contour_visualizer = ContourVisualizer(grid_config)
contour_fig = contour_visualizer.create_visualization(pmf_result)
contour_visualizer.save_visualization(contour_fig, out_contour_plot_path)

heatmap_visualizer = HeatmapVisualizer(grid_config)
heatmap_fig = heatmap_visualizer.create_visualization(pmf_result)
heatmap_visualizer.save_visualization(heatmap_fig, out_heatmap_plot_path)
```

## Configuration

Below is an example of a configuration file (`config.json`) used to set up PMF calculations and visualizations.

```json
{
    "pmf_config": {
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
        "inppdf": "path/to/energy_pdf.csv",
        "inppca": "path/to/pca.csv",
        "outgrd": "path/to/output.grid",
        "outplt": "path/to/output.plot"
    },
    "grid_config": {
        "plot_type": "contour",  // or "heatmap"
        "figsize": [10, 8],
        "dpi": 100,
        "levels": 20,
        "cmap": "viridis",
        "output_contour_plot": "path/to/contour_plot_output.png",
        "output_heatmap_plot": "path/to/heatmap_plot_output.png"
    }
}
```

## Development

To set up the development environment:

```bash
# Clone the repository
git clone https://github.com/yourusername/pygropmf.git
cd pygropmf

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## Features

- Multiple visualization types (contour, heatmap)
- Customizable plot settings
- Easy-to-use interface
- Compatible with GROMACS output

## License

MIT License

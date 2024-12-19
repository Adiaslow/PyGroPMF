# README.md
# PyGroPMF

A Python package for visualizing Potential of Mean Force (PMF) data from GROMACS simulations.

## Installation

```bash
pip install pygropmf
```

## Quick Start

```python
from pygropmf import GridResult, GridConfig, PMFVisualizer
import numpy as np

# Prepare your PMF data
data = GridResult(
    x_coords=your_x_data,
    y_coords=your_y_data,
    pmf_values=your_pmf_values
)

# Configure visualization
config = GridConfig(plot_type='contour', cmap='viridis')

# Create and save visualization
visualizer = PMFVisualizer(config)
fig = visualizer.create_visualization(data)
visualizer.save_visualization(fig, 'pmf_plot.png')
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

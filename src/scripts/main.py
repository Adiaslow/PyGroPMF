# src/scripts/main.py

import json
from pathlib import Path
from pygropmf.configurations.pmf_config import PMFConfig
from pygropmf.io.readers.energy_pdf_reader import EnergyPDFReader
from pygropmf.io.readers.pca_reader import PCAReader
from pygropmf.core.calculators.pmf_calculator import PMFCalculator
from pygropmf.io.writers.grid_writer import GridWriter
from pygropmf.io.writers.plot_writer import PlotWriter
from pygropmf.visualizers.contour_visualizer import ContourVisualizer
from pygropmf.visualizers.heatmap_visualizer import HeatmapVisualizer
from pygropmf.configurations.grid_config import GridConfig

def main():
    # Load the configuration from a file
    config_path = 'path/to/config.json'
    config = PMFConfig(config_path)

    # Initialize readers, calculator, and visualizers
    energy_pdf_path = Path(config.inppdf)
    pca_path = Path(config.inppca)
    out_grid_path = Path(config.outgrd)
    out_plot_path = Path(config.outplt)
    out_contour_plot_path = Path("path/to/contour_plot_output.png")
    out_heatmap_plot_path = Path("path/to/heatmap_plot_output.png")

    energy_pdf_data = EnergyPDFReader.read(energy_pdf_path)
    pca_reader = PCAReader(n_components=config.ncomp)
    pca_data = pca_reader.read(pca_path)

    pmf_calculator = PMFCalculator(config)
    pmf_result = pmf_calculator.calculate_pmf(energy_pdf_data, pca_data)

    # Use existing writers
    grid_writer = GridWriter()
    grid_writer.write(out_grid_path, pmf_result)

    plot_writer = PlotWriter()
    plot_writer.write(out_plot_path, pmf_result)

    # Load grid configuration
    grid_config_path = 'path/to/grid_config.json'
    grid_config = GridConfig(grid_config_path)

    # Use visualizers for visualization
    contour_visualizer = ContourVisualizer(grid_config)
    contour_fig = contour_visualizer.create_visualization(pmf_result)
    contour_visualizer.save_visualization(contour_fig, out_contour_plot_path)

    heatmap_visualizer = HeatmapVisualizer(grid_config)
    heatmap_fig = heatmap_visualizer.create_visualization(pmf_result)
    heatmap_visualizer.save_visualization(heatmap_fig, out_heatmap_plot_path)

if __name__ == "__main__":
    main()

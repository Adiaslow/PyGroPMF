# Python Codebase Summary

Generated on: 2024-12-18 22:44:25

## Summary Statistics
- Total Python files: 31
- Total functions: 72

---


## Directory: test


### __init__.py
**File Statistics:**
- Total lines: 2
- Non-empty lines: 1
- Number of functions: 0

---

### test_calculators.py
**File Statistics:**
- Total lines: 74
- Non-empty lines: 64
- Number of functions: 7

**Functions:**
```python
def calculator_config
def energy_pdf_data
def pca_data
def test_pmf_calculator_initialization
def test_get_probability
def test_calculate_pmf
def test_get_grid_coordinates
```
---

### test_io.py
**File Statistics:**
- Total lines: 81
- Non-empty lines: 68
- Number of functions: 6

**Functions:**
```python
def sample_energy_pdf_file
def sample_pmf_result
def test_energy_pdf_reader
def test_energy_pdf_reader_empty_file
def test_pca_reader_dimension_mismatch
def test_plot_writer
```
---

### test_visualizers.py
**File Statistics:**
- Total lines: 73
- Non-empty lines: 64
- Number of functions: 8

**Functions:**
```python
def sample_data
def contour_config
def heatmap_config
def test_contour_visualizer
def test_heatmap_visualizer
def test_pmf_visualizer_factory
def test_invalid_colormap
def test_invalid_plot_type
```
---


## Directory: pygropmf


### __init__.py
**File Statistics:**
- Total lines: 7
- Non-empty lines: 5
- Number of functions: 0

---


## Directory: pygropmf/configurations


### __init__.py
**File Statistics:**
- Total lines: 6
- Non-empty lines: 4
- Number of functions: 0

---

### grid_config.py
**File Statistics:**
- Total lines: 58
- Non-empty lines: 49
- Number of functions: 2

**Functions:**
```python
def __post_init__
def __hash__
```
---

### pmf_config.py
**File Statistics:**
- Total lines: 72
- Non-empty lines: 53
- Number of functions: 17

**Functions:**
```python
def __init__
def _load_config
def get
def temperature
def x_bin_size
def y_bin_size
def x_axis
def y_axis
def x_min
def x_bin
def y_min
def y_bin
def ncomp
def inppdf
def inppca
def outgrd
def outplt
```
---


## Directory: pygropmf/core


### __init__.py
**File Statistics:**
- Total lines: 2
- Non-empty lines: 0
- Number of functions: 0

---


## Directory: pygropmf/core/results


### __init__.py
**File Statistics:**
- Total lines: 6
- Non-empty lines: 4
- Number of functions: 0

---

### grid_result.py
**File Statistics:**
- Total lines: 12
- Non-empty lines: 9
- Number of functions: 0

---

### pmf_result.py
**File Statistics:**
- Total lines: 12
- Non-empty lines: 10
- Number of functions: 0

---


## Directory: pygropmf/core/factories


### pmf_visualizer.py
**File Statistics:**
- Total lines: 36
- Non-empty lines: 29
- Number of functions: 4

**Functions:**
```python
def __init__
def _create_visualizer
def create_visualization
def save_visualization
```
---


## Directory: pygropmf/core/calculators


### __init__.py
**File Statistics:**
- Total lines: 5
- Non-empty lines: 3
- Number of functions: 0

---

### pmf_calculator.py
**File Statistics:**
- Total lines: 74
- Non-empty lines: 58
- Number of functions: 5

**Functions:**
```python
def __init__
def calculate_pmf
def _get_probability
def _calculate_final_pmf
def _generate_grid_coordinates
```
---


## Directory: pygropmf/core/data


### __init__.py
**File Statistics:**
- Total lines: 10
- Non-empty lines: 7
- Number of functions: 0

---

### energy_pdf_data.py
**File Statistics:**
- Total lines: 28
- Non-empty lines: 23
- Number of functions: 3

**Functions:**
```python
def __len__
def __getitem__
def to_dataframe
```
---

### pca_data.py
**File Statistics:**
- Total lines: 31
- Non-empty lines: 26
- Number of functions: 3

**Functions:**
```python
def __len__
def iterrows
def to_dataframe
```
---


## Directory: pygropmf/core/protocols


### __init__.py
**File Statistics:**
- Total lines: 5
- Non-empty lines: 3
- Number of functions: 0

---

### visualizer.py
**File Statistics:**
- Total lines: 46
- Non-empty lines: 35
- Number of functions: 3

**Functions:**
```python
def __init__
def create_visualization
def save_visualization
```
---


## Directory: pygropmf/visualizers


### __init__.py
**File Statistics:**
- Total lines: 6
- Non-empty lines: 4
- Number of functions: 0

---

### contour_visualizer.py
**File Statistics:**
- Total lines: 49
- Non-empty lines: 40
- Number of functions: 4

**Functions:**
```python
def __init__
def _set_common_elements
def create_visualization
def save_visualization
```
---

### heatmap_visualizer.py
**File Statistics:**
- Total lines: 60
- Non-empty lines: 48
- Number of functions: 4

**Functions:**
```python
def __init__
def create_visualization
def save_visualization
def _configure_axis
```
---


## Directory: pygropmf/io


### __init__.py
**File Statistics:**
- Total lines: 1
- Non-empty lines: 0
- Number of functions: 0

---


## Directory: pygropmf/io/writers


### __init__.py
**File Statistics:**
- Total lines: 10
- Non-empty lines: 7
- Number of functions: 0

---

### grid_writer.py
**File Statistics:**
- Total lines: 16
- Non-empty lines: 12
- Number of functions: 1

**Functions:**
```python
def write
```
---

### plot_writer.py
**File Statistics:**
- Total lines: 30
- Non-empty lines: 26
- Number of functions: 1

**Functions:**
```python
def write
```
---


## Directory: pygropmf/io/readers


### __init__.py
**File Statistics:**
- Total lines: 6
- Non-empty lines: 4
- Number of functions: 0

---

### energy_pdf_reader.py
**File Statistics:**
- Total lines: 25
- Non-empty lines: 20
- Number of functions: 1

**Functions:**
```python
def read
```
---

### pca_reader.py
**File Statistics:**
- Total lines: 26
- Non-empty lines: 20
- Number of functions: 2

**Functions:**
```python
def __init__
def read
```
---


## Directory: pygropmf/scripts


### main.py
**File Statistics:**
- Total lines: 38
- Non-empty lines: 29
- Number of functions: 1

**Functions:**
```python
def main
```
---

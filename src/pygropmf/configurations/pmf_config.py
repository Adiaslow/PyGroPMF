# src/pygropmf/configurations/pmf_config.py

import json

class PMFConfig:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        with open(self.config_path, 'r') as f:
            return json.load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)

    @property
    def temperature(self):
        return self.get('temperature')

    @property
    def x_bin_size(self):
        return self.get('x_bin_size')

    @property
    def y_bin_size(self):
        return self.get('y_bin_size')

    @property
    def x_axis(self):
        return self.get('x_axis')

    @property
    def y_axis(self):
        return self.get('y_axis')

    @property
    def x_min(self):
        return self.get('x_min')

    @property
    def x_bin(self):
        return self.get('x_bin')

    @property
    def y_min(self):
        return self.get('y_min')

    @property
    def y_bin(self):
        return self.get('y_bin')

    @property
    def ncomp(self):
        return self.get('ncomp')

    @property
    def inppdf(self):
        return self.get('inppdf')

    @property
    def inppca(self):
        return self.get('inppca')

    @property
    def outgrd(self):
        return self.get('outgrd')

    @property
    def outplt(self):
        return self.get('outplt')

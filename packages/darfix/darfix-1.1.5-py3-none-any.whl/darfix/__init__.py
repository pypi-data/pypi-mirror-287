"""The darfix package contains the following main sub-packages:

- silx.core: Core classes and functions
- silx.gui: Qt widgets for data visualization and data file browsing
- silx.image: Some processing functions for 2D images
- silx.io: Functions for input/output operations
- silx.utils: Miscellaneous convenient functions
"""

__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "21/06/2024"
__version__ = "1.1.5"

from ._config import Config as _Config

config = _Config()
"""Global configuration shared with the whole library"""

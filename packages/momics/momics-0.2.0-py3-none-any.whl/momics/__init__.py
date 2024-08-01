"""
momics
~~~~~~

Cloud-native, TileDB-based multi-omics data format. 

:author: Jacques Serizay
:license: CC BY-NC 4.0

"""

from ._version import __format_version__, __version__
from .Momics import Momics

__all__ = [
    "__version__",
    "__format_version__",
]

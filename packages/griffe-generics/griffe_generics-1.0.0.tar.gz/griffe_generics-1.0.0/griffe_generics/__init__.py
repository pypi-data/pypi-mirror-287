# from griffe_generics.extension import GenericsExtension
from importlib import reload

import griffe_generics.extension

reload(griffe_generics.extension)
GenericsExtension = griffe_generics.extension.GenericsExtension
__version__ = "1.0.0"

__all__ = ["GenericsExtension"]

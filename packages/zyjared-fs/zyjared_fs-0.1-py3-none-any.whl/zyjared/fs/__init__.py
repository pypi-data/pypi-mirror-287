__path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .fs import rm_path, matches_path, clean_directory  # noqa: F401

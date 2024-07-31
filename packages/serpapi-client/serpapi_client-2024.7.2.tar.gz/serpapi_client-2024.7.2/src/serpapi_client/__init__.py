from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("serpapi_client")
except PackageNotFoundError:
    # package is not installed
    pass
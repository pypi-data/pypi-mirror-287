try:
    from .version import __version__, __build__
except Exception:
    __version__ = "0.0.0"
    __build__ = "dev"

from .encoder import generify, GenerifyEncoder, GenerifyException, GenerifyGetAttrException
from .json_encoder import GenerifyJSONEncoder

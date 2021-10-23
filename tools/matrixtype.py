
__all__ = [
    'get_matrix_types',
    'inspect_matrix',
    'Matrix',
]

import collections
import ctypes
import re

import glm
from typemap import DATA_TYPE_PREFIX_TO_C_TYPE, DATA_TYPE_PREFIX_TO_PYTHON_TYPE

_PATTERN = re.compile(f'^([dfiu])?mat(\d)x(\d)$')
_PATTERN_DATA_TYPE_INDEX = 1
_PATTERN_ROWS = 2
_PATTERN_COLUMNS = 3

_MATRIX_TYPES = tuple(sorted(
    t.__name__ for t in
    {getattr(glm, name) for name in dir(glm) if _PATTERN.match(name)}
))


_MATRIX_ALIASES = {}
for name in dir(glm):
    alias_obj = getattr(glm, name)
    if not hasattr(alias_obj, "__name__"):
        continue
    if alias_obj.__name__ == name:
        continue
    actual_name = alias_obj.__name__
    if actual_name not in _MATRIX_TYPES:
        continue
    try:
        aliases = _MATRIX_ALIASES[actual_name]
    except KeyError:
        aliases = _MATRIX_ALIASES[actual_name] = []
    aliases.append(name)


def get_matrix_types(filter=None):
    return (
        name for name in _MATRIX_TYPES
        if not filter or filter(inspect_matrix(name))
    )


def inspect_matrix(name):
    match = _PATTERN.match(name)
    data_type = match[_PATTERN_DATA_TYPE_INDEX]
    if data_type is None:
        data_type = 'f'
    data_size = ctypes.sizeof(DATA_TYPE_PREFIX_TO_C_TYPE[data_type]) * 8
    return Matrix(
        name,
        data_type,
        data_size,
        int(match[_PATTERN_ROWS]),
        int(match[_PATTERN_COLUMNS]),
        DATA_TYPE_PREFIX_TO_PYTHON_TYPE[data_type].__name__,
        _MATRIX_ALIASES.get(name, [])
    )


Matrix = collections.namedtuple(
    "Matrix",
    ['name', 'data_type', 'data_size', 'rows', 'columns', 'python_type', 'aliases']
)

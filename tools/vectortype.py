
__all__ = [
    'get_vector_types',
    'inspect_vector',
    'Vector',
]

import collections
import ctypes
import re

import glm
from typemap import DATA_TYPE_PREFIX_TO_C_TYPE, DATA_TYPE_PREFIX_TO_PYTHON_TYPE

_PATTERN = re.compile(f'^([bdfiu])?(\d*)(m)?vec(\d)$')
_PATTERN_DATA_TYPE_INDEX = 1
_PATTERN_DATA_SIZE_INDEX = 2
_PATTERN_M = 3
_PATTERN_SIZE = 4

_VECTOR_TYPES = tuple(sorted(
    t.__name__ for t in
    {getattr(glm, name) for name in dir(glm) if _PATTERN.match(name)}
))


_VECTOR_ALIASES = {}
for name in dir(glm):
    alias_obj = getattr(glm, name)
    if not hasattr(alias_obj, "__name__"):
        continue
    if alias_obj.__name__ == name:
        continue
    actual_name = alias_obj.__name__
    if actual_name not in _VECTOR_TYPES:
        continue
    try:
        aliases = _VECTOR_ALIASES[actual_name]
    except KeyError:
        aliases = _VECTOR_ALIASES[actual_name] = []
    aliases.append(name)


def get_vector_types(filter=None):
    return (
        name for name in _VECTOR_TYPES
        if not filter or filter(inspect_vector(name))
    )


def inspect_vector(name):
    match = _PATTERN.match(name)
    data_type = match[_PATTERN_DATA_TYPE_INDEX]
    if data_type is None:
        data_type = 'f'
    c_type = DATA_TYPE_PREFIX_TO_C_TYPE[data_type]
    try:
        data_size = int(match[_PATTERN_DATA_SIZE_INDEX])
    except ValueError:
        data_size = ctypes.sizeof(c_type) * 8
    return Vector(
        name,
        data_type,
        data_size,
        match[_PATTERN_M] == 'm',
        int(match[_PATTERN_SIZE]),
        DATA_TYPE_PREFIX_TO_PYTHON_TYPE[data_type].__name__,
        _VECTOR_ALIASES.get(name, []),
    )


Vector = collections.namedtuple(
    "Vector",
    ['name', 'data_type', 'data_size', 'm', 'size', 'python_type', 'aliases']
)

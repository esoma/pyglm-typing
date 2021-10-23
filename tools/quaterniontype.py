
__all__ = [
    'get_quaternion_types',
    'inspect_quaternion',
    'Quaternion',
]

import collections
import ctypes
import re

import glm
from typemap import DATA_TYPE_PREFIX_TO_C_TYPE, DATA_TYPE_PREFIX_TO_PYTHON_TYPE

_PATTERN = re.compile(f'^(d)?quat$')
_PATTERN_DATA_TYPE_INDEX = 1

_QUATERNION_TYPES = tuple(sorted(
    t.__name__ for t in
    {getattr(glm, name) for name in dir(glm) if _PATTERN.match(name)}
))


_QUATERNION_ALIASES = {}
for name in dir(glm):
    alias_obj = getattr(glm, name)
    if not hasattr(alias_obj, "__name__"):
        continue
    if alias_obj.__name__ == name:
        continue
    actual_name = alias_obj.__name__
    if actual_name not in _QUATERNION_TYPES:
        continue
    try:
        aliases = _QUATERNION_ALIASES[actual_name]
    except KeyError:
        aliases = _QUATERNION_ALIASES[actual_name] = []
    aliases.append(name)


def get_quaternion_types(filter=None):
    return (
        name for name in _QUATERNION_TYPES
        if not filter or filter(inspect_quaternion(name))
    )


def inspect_quaternion(name):
    match = _PATTERN.match(name)
    data_type = match[_PATTERN_DATA_TYPE_INDEX]
    if data_type is None:
        data_type = 'f'
    data_size = ctypes.sizeof(DATA_TYPE_PREFIX_TO_C_TYPE[data_type]) * 8
    return Quaternion(
        name,
        data_type,
        data_size,
        DATA_TYPE_PREFIX_TO_PYTHON_TYPE[data_type].__name__,
        _QUATERNION_ALIASES.get(name, [])
    )


Quaternion = collections.namedtuple(
    "Quaternion",
    ['name', 'data_type', 'data_size', 'python_type', 'aliases']
)

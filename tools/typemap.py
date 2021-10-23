
__all__ = [
    'DATA_TYPE_PREFIX_TO_C_TYPE',
    'DATA_TYPE_PREFIX_TO_PYTHON_TYPE',
    'DATA_TYPE_SIZE_PREFIX_TO_C_TYPE',
]

import ctypes

DATA_TYPE_PREFIX_TO_C_TYPE = {
    'b': ctypes.c_bool,
    'd': ctypes.c_double,
    'f': ctypes.c_float,
    'i': ctypes.c_int,
    'u': ctypes.c_uint,
}

DATA_TYPE_PREFIX_TO_PYTHON_TYPE = {
    'b': bool,
    'd': float,
    'f': float,
    'i': int,
    'u': int,
}

DATA_TYPE_SIZE_PREFIX_TO_C_TYPE = {
    ('b', 8): ctypes.c_bool,
    ('d', 64): ctypes.c_double,
    ('f', 32): ctypes.c_float,
    ('i', 8): ctypes.c_int8,
    ('i', 16): ctypes.c_int16,
    ('i', 32): ctypes.c_int32,
    ('i', 64): ctypes.c_int64,
    ('u', 8): ctypes.c_uint8,
    ('u', 16): ctypes.c_uint16,
    ('u', 32): ctypes.c_uint32,
    ('u', 64): ctypes.c_uint64,
}


__all__ = [
    'union',
    'matrix_name', 'matrix_union',
    'quaternion_name', 'quaternion_union',
    'vector_name', 'vector_union'
]

import ctypes

from typemap import DATA_TYPE_PREFIX_TO_C_TYPE


def union(names):
    if not hasattr(names, "__len__"):
        names = list(names)
    if len(names) == 1:
        return names[0]
    return f'Union[{", ".join(names)}]'

def matrix_name(data_type, rows, columns):
    if data_type == 'f':
        data_type = ''
    return f'''{data_type}mat{rows}x{columns}'''

def matrix_union(
    data_type=None,
    data_size=None,
    rows=None,
    columns=None,
    include_tuple=True,
    *,
    prefix='glm_typing.'
):
    name = 'Matrix' if include_tuple else 'Mat'
    if data_type is None:
        if data_size is not None:
            return None
        data_type = 'Any'
    elif data_type not in 'dfiu':
        return None
    else:
        if data_size is not None:
            c_type = DATA_TYPE_PREFIX_TO_C_TYPE[data_type]
            if ctypes.sizeof(c_type) * 8 != data_size:
                return None
        data_type = data_type.upper()
    if data_size is None:
        data_size = 'Any'
    if rows is None:
        rows = 'Any'
    if columns is None:
        columns = 'Any'
    return f'''{prefix}{data_type}{data_size}{name}{rows}x{columns}'''

def quaternion_name(data_type):
    if data_type == 'f':
        data_type = ''
    return f'''{data_type}quat'''

def quaternion_union(
    data_type=None,
    data_size=None,
    include_tuple=True,
    *,
    prefix='glm_typing.'
):
    name = 'Quaternion' if include_tuple else 'Quat'
    if data_type is None:
        if data_size is not None:
            return None
        data_type = 'Any'
    elif data_type not in 'fd':
        return None
    else:
        if data_size is not None:
            c_type = DATA_TYPE_PREFIX_TO_C_TYPE[data_type]
            if ctypes.sizeof(c_type) * 8 != data_size:
                return None
        data_type = data_type.upper()
    if data_size is None:
        data_size = 'Any'
    return f'''{prefix}{data_type}{data_size}{name}'''

def vector_name(data_type, size, m=False):
    if data_type == 'f':
        data_type = ''
    m = 'm' if m else ''
    return f'''{data_type}{m}vec{size}'''

def vector_union(
    data_type=None,
    data_size=None,
    size=None,
    include_tuple=True,
    *,
    prefix='glm_typing.'
):
    name = 'Vector' if include_tuple else 'Vec'
    if data_type is None:
        data_type = 'Any'
    elif data_type not in 'bdfiu':
        return None
    else:
        data_type = data_type.upper()
    if data_size is None:
        data_size = 'Any'
    if size is None:
        size = 'Any'
    return f'''{prefix}{data_type}{data_size}{name}{size}'''

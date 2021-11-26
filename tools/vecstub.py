
__all__ = [
    'generate_vec_stub',
    'generate_vec_typevars',
    'generate_vec_unions',
    'vector_tuple',
]

import textwrap
from itertools import product

from stub import matrix_union, union, vector_union
from vectortype import get_vector_types, inspect_vector

_COMPONENT_NAMES = ('x', 'y', 'z', 'w')


def generate_vec_unions():
    for data_type, data_size, size, include_tuple in product(
        ['b', 'd', 'f', 'i', 'u', None],
        [8, 16, 32, 64, None],
        [1, 2, 3, 4, None],
        [True, False],
    ):
        def _(vector):
            if data_type is not None and vector.data_type != data_type:
                return False
            if data_size is not None and vector.data_size != data_size:
                return False
            if size is not None and vector.size != size:
                return False
            return True
        union_name = vector_union(
            data_type=data_type,
            data_size=data_size,
            size=size,
            include_tuple=include_tuple,
            prefix='',
        )
        if union_name is None:
            continue
        vectors = [f'glm.{v}' for v in get_vector_types(_)]
        if not vectors:
            continue
        if include_tuple:
            if size is None:
                tuples = [vector_tuple(i, prefix=None) for i in range(1, 5)]
            else:
                tuples = [vector_tuple(size, prefix=None)]
        else:
            tuples = []
        yield union_name, f'''{union_name} = {union([*vectors, *tuples])}'''
    yield 'FDAnyVectorAny', f'''FDAnyVectorAny = {union(['FAnyVectorAny', 'DAnyVectorAny'])}'''
    yield 'FDAnyVector1', f'''FDAnyVector1 = {union(['FAnyVector1', 'DAnyVector1'])}'''
    yield 'FDAnyVector2', f'''FDAnyVector2 = {union(['FAnyVector2', 'DAnyVector2'])}'''
    yield 'FDAnyVector3', f'''FDAnyVector3 = {union(['FAnyVector3', 'DAnyVector3'])}'''
    yield 'FDAnyVector4', f'''FDAnyVector4 = {union(['FAnyVector4', 'DAnyVector4'])}'''
    yield 'IUAnyVector1', f'''IUAnyVector1 = {union(['IAnyVector1', 'UAnyVector1'])}'''
    yield 'IUAnyVector2', f'''IUAnyVector2 = {union(['IAnyVector2', 'UAnyVector2'])}'''
    yield 'IUAnyVector3', f'''IUAnyVector3 = {union(['IAnyVector3', 'UAnyVector3'])}'''
    yield 'IUAnyVector4', f'''IUAnyVector4 = {union(['IAnyVector4', 'UAnyVector4'])}'''


def generate_vec_typevars():
    typevars = [
        ('_VT', get_vector_types()),
        ('_NF32VT', get_vector_types(lambda v: not (v.data_type == 'f' and v.data_size == 32))),
        ('_FDVT', get_vector_types(lambda v: v.data_type in 'df')),
        ('_NF32DFVT', get_vector_types(lambda v: v.data_type in 'df' and not (v.data_type == 'f' and v.data_size == 32))),
        ('_NF32DFV1T', get_vector_types(lambda v: v.data_type in 'df' and v.size == 1 and not (v.data_type == 'f' and v.data_size == 32))),
        ('_NF32DFV2T', get_vector_types(lambda v: v.data_type in 'df' and v.size == 2 and not (v.data_type == 'f' and v.data_size == 32))),
        ('_NF32DFV3T', get_vector_types(lambda v: v.data_type in 'df' and v.size == 3 and not (v.data_type == 'f' and v.data_size == 32))),
        ('_NF32DFV4T', get_vector_types(lambda v: v.data_type in 'df' and v.size == 4 and not (v.data_type == 'f' and v.data_size == 32))),
        ('_NF32V1T', get_vector_types(lambda v: v.size == 1 and not (v.data_type == 'f' and v.data_size == 32))),
        ('_NF32V2T', get_vector_types(lambda v: v.size == 2 and not (v.data_type == 'f' and v.data_size == 32))),
        ('_NF32V3T', get_vector_types(lambda v: v.size == 3 and not (v.data_type == 'f' and v.data_size == 32))),
        ('_NF32V4T', get_vector_types(lambda v: v.size == 4 and not (v.data_type == 'f' and v.data_size == 32))),
        ('_IVT', get_vector_types(lambda v: v.data_type in 'i')),
        ('_UVT', get_vector_types(lambda v: v.data_type in 'u')),
        ('_NI32IVT', get_vector_types(lambda v: v.data_type in 'i' and not (v.data_type == 'i' and v.data_size == 32))),
        ('_NI32IUVT', get_vector_types(lambda v: v.data_type in 'iu' and not (v.data_type == 'i' and v.data_size == 32))),
        ('_NI32IUV1T', get_vector_types(lambda v: v.data_type in 'iu' and v.size == 1 and not (v.data_type == 'i' and v.data_size == 32))),
        ('_NI32IUV2T', get_vector_types(lambda v: v.data_type in 'iu' and v.size == 2 and not (v.data_type == 'i' and v.data_size == 32))),
        ('_NI32IUV3T', get_vector_types(lambda v: v.data_type in 'iu' and v.size == 3 and not (v.data_type == 'i' and v.data_size == 32))),
        ('_NI32IUV4T', get_vector_types(lambda v: v.data_type in 'iu' and v.size == 4 and not (v.data_type == 'i' and v.data_size == 32))),
    ]
    return '\n'.join(
        f'''{name} = TypeVar('{name}', {', '.join(types) if len(types) > 1 else f'bound={types[0]}'})'''
        for name, types in
        ((n, list(ts)) for n, ts in typevars)
    ) + '\n'


def generate_vec_stub(name):
    vector = inspect_vector(name)
    this_vector_union = vector_union(
        data_type=vector.data_type,
        data_size=vector.data_size,
        size=vector.size
    )
    this_mat2x2 = matrix_union(
        data_type=vector.data_type,
        data_size=vector.data_size,
        rows=2, columns=2
    )
    this_mat3x2 = matrix_union(
        data_type=vector.data_type,
        data_size=vector.data_size,
        rows=3, columns=2
    )
    this_mat4x2 = matrix_union(
        data_type=vector.data_type,
        data_size=vector.data_size,
        rows=4, columns=2
    )

    return [name, *vector.aliases], textwrap.dedent(f"""{"".join(f'''
    {alias} = {name}''' for alias in vector.aliases)}

    class {name}:{''.join(f'''
        {c}: {vector.python_type}''' for c in _COMPONENT_NAMES[:vector.size])}

        @overload
        def __init__(self) -> None: ...{f'''
        @overload
        def __init__(self, x: glm_typing.Number) -> None: ...''' if vector.size != 1 else ''}
        @overload
        def __init__(self, {', '.join(f'{c}: glm_typing.Number' for c in _COMPONENT_NAMES[:vector.size])}) -> None: ...
        @overload
        def __init__(self, x: {union([vector_union(size=vector.size), *(vector_union(data_type=vector.data_type, size=i) for i in range(vector.size + 1, 5))])}) -> None: ...

        def __len__(self) -> Literal[{vector.size}]: ...
        def __getitem__(self, index: int) -> {vector.python_type}: ...
        def __setitem__(self, index: int, value: glm_typing.Number) -> None: ...
        def __contains__(self, value: Any) -> bool: ...
        def __iter__(self) -> Generator[{vector.python_type}, None, None]: ...

        def __neg__(self) -> {name}: ...
        def __pos__(self) -> {name}: ...
        def __abs__(self) -> {name}: ...

        def __lt__(self, other: Any) -> bool: ...
        def __le__(self, other: Any) -> bool: ...
        def __eq__(self, other: Any) -> bool: ...
        def __ne__(self, other: Any) -> bool: ...
        def __ge__(self, other: Any) -> bool: ...
        def __gt__(self, other: Any) -> bool: ...

        def to_list(self) -> List[{vector.python_type}]: ...
        def to_tuple(self) -> Tuple[{', '.join(vector.python_type for i in range(vector.size))}]: ...
        def to_bytes(self) -> bytes: ...

        @staticmethod
        def from_bytes(bytes: bytes, /) -> {name}: ...

        def __add__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...
        def __radd__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...
        def __iadd__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...

        def __sub__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...
        def __rsub__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...
        def __isub__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...

        @overload
        def __mul__(self, other: glm_typing.Number) -> {name}: ...
        @overload
        def __mul__(self, other: {this_vector_union}) -> {name}: ...{f'''
        @overload
        def __mul__(self, other: {this_mat2x2}) -> vec2: ...''' if this_mat2x2 else ''}{f'''
        @overload
        def __mul__(self, other: {this_mat3x2}) -> vec3: ...''' if this_mat3x2 else ''}{f'''
        @overload
        def __mul__(self, other: {this_mat4x2}) -> vec4: ...''' if this_mat4x2 else ''}
        @overload
        def __rmul__(self, other: glm_typing.Number) -> {name}: ...
        @overload
        def __rmul__(self, other: {this_vector_union}) -> {name}: ...{f'''
        @overload
        def __rmul__(self, other: {this_mat2x2}) -> vec2: ...''' if this_mat2x2 else ''}{f'''
        @overload
        def __rmul__(self, other: {this_mat3x2}) -> vec3: ...''' if this_mat3x2 else ''}{f'''
        @overload
        def __rmul__(self, other: {this_mat4x2}) -> vec4: ...''' if this_mat4x2 else ''}
        @overload
        def __imul__(self, other: glm_typing.Number) -> {name}: ...
        @overload
        def __imul__(self, other: {this_vector_union}) -> {name}: ...{f'''
        @overload
        def __imul__(self, other: {this_mat2x2}) -> vec2: ...''' if this_mat2x2 else ''}{f'''
        @overload
        def __imul__(self, other: {this_mat3x2}) -> vec3: ...''' if this_mat3x2 else ''}{f'''
        @overload
        def __imul__(self, other: {this_mat4x2}) -> vec4: ...''' if this_mat4x2 else ''}

        def __mod__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...
        def __rmod__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...
        def __imod__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...

        def __pow__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...
        def __rpow__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...
        def __ipow__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...

        def __truediv__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...
        def __rtruediv__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...
        def __itruediv__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...

        def __floordiv__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...
        def __rfloordiv__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...
        def __ifloordiv__(self, other: {union([this_vector_union, 'glm_typing.Number'])}) -> {name}: ...

        @overload
        def __matmul__(self, other: glm_typing.Number) -> {name}: ...
        @overload
        def __matmul__(self, other: {this_vector_union}) -> {name}: ...{f'''
        @overload
        def __matmul__(self, other: {this_mat2x2}) -> vec2: ...''' if this_mat2x2 else ''}{f'''
        @overload
        def __matmul__(self, other: {this_mat3x2}) -> vec3: ...''' if this_mat3x2 else ''}{f'''
        @overload
        def __matmul__(self, other: {this_mat4x2}) -> vec4: ...''' if this_mat4x2 else ''}
        @overload
        def __rmatmul__(self, other: glm_typing.Number) -> {name}: ...
        @overload
        def __rmatmul__(self, other: {this_vector_union}) -> {name}: ...{f'''
        @overload
        def __rmatmul__(self, other: {this_mat2x2}) -> vec2: ...''' if this_mat2x2 else ''}{f'''
        @overload
        def __rmatmul__(self, other: {this_mat3x2}) -> vec3: ...''' if this_mat3x2 else ''}{f'''
        @overload
        def __rmatmul__(self, other: {this_mat4x2}) -> vec4: ...''' if this_mat4x2 else ''}
        @overload
        def __imatmul__(self, other: glm_typing.Number) -> {name}: ...
        @overload
        def __imatmul__(self, other: {this_vector_union}) -> {name}: ...{f'''
        @overload
        def __imatmul__(self, other: {this_mat2x2}) -> vec2: ...''' if this_mat2x2 else ''}{f'''
        @overload
        def __imatmul__(self, other: {this_mat3x2}) -> vec3: ...''' if this_mat3x2 else ''}{f'''
        @overload
        def __imatmul__(self, other: {this_mat4x2}) -> vec4: ...''' if this_mat4x2 else ''}

        def __divmod__(self, other: {name}) -> Tuple[{name}, {name}]: ...
    """)


def vector_tuple(size, prefix='glm_typing.'):
    if prefix is None:
        prefix = ''
    return f"""Tuple[{', '.join(f'{prefix}Number' for i in range(size))}]"""


__all__ = [
    'generate_quat_stub',
    'generate_quat_typevars',
    'generate_quat_unions'
]

import textwrap
from itertools import product

from quaterniontype import get_quaternion_types, inspect_quaternion
from stub import (matrix_union, quaternion_union, union, vector_name,
                  vector_union)


def generate_quat_unions():
    for data_type, data_size, include_tuple in product(
        ['d', 'f', None],
        [8, 16, 32, 64, None],
        [True, False],
    ):
        def _(quaternion):
            if data_type is not None and quaternion.data_type != data_type:
                return False
            if data_size is not None and quaternion.data_size != data_size:
                return False
            return True
        union_name = quaternion_union(
            data_type=data_type,
            data_size=data_size,
            include_tuple=include_tuple,
            prefix=''
        )
        if union_name is None:
            continue
        quaternions = [f'glm.{v}' for v in get_quaternion_types(_)]
        if not quaternions:
            continue
        if include_tuple:
            tuples = [_quaternion_tuple()]
        else:
            tuples = []
        yield union_name, f'''{union_name} = {union([*quaternions, *tuples])}'''
    yield 'FDAnyQuaternion', f'''FDAnyQuaternion = {union(['FAnyQuaternion', 'DAnyQuaternion'])}'''


def generate_quat_typevars():
    typevars = [
        ('_QT', get_quaternion_types()),
        ('_NF32QT', get_quaternion_types(lambda q: not (q.data_type == 'f' and q.data_size == 32))),
    ]
    return '\n'.join(
        f'''{name} = TypeVar('{name}', {', '.join(types) if len(types) > 1 else f'bound={types[0]}'})'''
        for name, types in
        ((n, list(ts)) for n, ts in typevars)
    ) + '\n'

def generate_quat_stub(name):
    quaternion = inspect_quaternion(name)
    this_quaternion_union = quaternion_union(
        data_type=quaternion.data_type,
        data_size=quaternion.data_size,
    )
    mat3x3_union = matrix_union(data_type=quaternion.data_type, data_size=quaternion.data_size, rows=3, columns=3)
    mat4x4_union = matrix_union(data_type=quaternion.data_type, data_size=quaternion.data_size, rows=4, columns=4)
    vec3_union = vector_union(data_type=quaternion.data_type, data_size=quaternion.data_size, size=3)
    vec4_union = vector_union(data_type=quaternion.data_type, data_size=quaternion.data_size, size=4)
    vec3 = vector_name(quaternion.data_type, 3)
    vec4 = vector_name(quaternion.data_type, 4)

    return [name, *quaternion.aliases], textwrap.dedent(f"""{"".join(f'''
    {alias} = {name}''' for alias in quaternion.aliases)}

    class {name}:
        w: {quaternion.python_type}
        x: {quaternion.python_type}
        y: {quaternion.python_type}
        z: {quaternion.python_type}

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, w: glm_typing.Number, x: glm_typing.Number, y: glm_typing.Number, z: glm_typing.Number) -> None: ...
        @overload
        def __init__(self, w: {union([quaternion_union(), mat3x3_union, mat4x4_union, vec3_union])}) -> None: ...

        def length(self) -> Literal[4]: ...
        def __len__(self) -> Literal[4]: ...
        def __getitem__(self, index: int) -> {quaternion.python_type}: ...
        def __setitem__(self, index: int, value: glm_typing.Number) -> None: ...
        def __contains__(self, value: Any) -> bool: ...
        def __iter__(self) -> Generator[{quaternion.python_type}, None, None]: ...

        def to_list(self) -> List[{quaternion.python_type}]: ...
        def to_tuple(self) -> Tuple[{', '.join(quaternion.python_type for i in range(4))}]: ...
        def to_bytes(self) -> bytes: ...

        @staticmethod
        def from_bytes(bytes: bytes, /) -> {name}: ...

        def __eq__(self, other: Any) -> bool: ...
        def __ne__(self, other: Any) -> bool: ...

        @overload
        def __mul__(self, other: {union([name, 'glm_typing.Number'])}) -> {name}: ...
        @overload
        def __mul__(self, other: {vec3_union}) -> {vec3}: ...
        @overload
        def __mul__(self, other: {vec4_union}) -> {vec4}: ...
        @overload
        def __rmul__(self, other: {union([name, 'glm_typing.Number'])}) -> {name}: ...
        @overload
        def __rmul__(self, other: {vec3_union}) -> {vec3}: ...
        @overload
        def __rmul__(self, other: {vec4_union}) -> {vec4}: ...
        @overload
        def __imul__(self, other: {union([name, 'glm_typing.Number'])}) -> {name}: ...
        @overload
        def __imul__(self, other: {vec3_union}) -> {vec3}: ...
        @overload
        def __imul__(self, other: {vec4_union}) -> {vec4}: ...

        @overload
        def __matmul__(self, other: {union([name, 'glm_typing.Number'])}) -> {name}: ...
        @overload
        def __matmul__(self, other: {vec3_union}) -> {vec3}: ...
        @overload
        def __matmul__(self, other: {vec4_union}) -> {vec4}: ...
        @overload
        def __rmatmul__(self, other: {union([name, 'glm_typing.Number'])}) -> {name}: ...
        @overload
        def __rmatmul__(self, other: {vec3_union}) -> {vec3}: ...
        @overload
        def __rmatmul__(self, other: {vec4_union}) -> {vec4}: ...
        @overload
        def __imatmul__(self, other: {union([name, 'glm_typing.Number'])}) -> {name}: ...
        @overload
        def __imatmul__(self, other: {vec3_union}) -> {vec3}: ...
        @overload
        def __imatmul__(self, other: {vec4_union}) -> {vec4}: ...
    """)


def _quaternion_tuple():
    return f"""Tuple[{', '.join('Number' for i in range(4))}]"""

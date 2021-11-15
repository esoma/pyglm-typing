
__all__ = [
    'generate_mat_stub',
    'generate_mat_typevars',
    'generate_mat_unions'
]

import textwrap
from itertools import product

from matrixtype import get_matrix_types, inspect_matrix
from stub import matrix_name, matrix_union, union, vector_name, vector_union


def generate_mat_unions():
    for data_type, data_size, rows, columns, include_tuple in product(
        ['d', 'f', 'i', 'u', None],
        [8, 16, 32, 64, None],
        [2, 3, 4, None],
        [2, 3, 4, None],
        [True, False],
    ):
        def _(matrix):
            if data_type is not None and matrix.data_type != data_type:
                return False
            if data_size is not None and matrix.data_size != data_size:
                return False
            if rows is not None and matrix.rows != rows:
                return False
            if columns is not None and matrix.columns != columns:
                return False
            return True
        union_name = matrix_union(
            data_type=data_type,
            data_size=data_size,
            rows=rows,
            columns=columns,
            include_tuple=include_tuple,
            prefix='',
        )
        if union_name is None:
            continue
        matrices = [f'glm.{v}' for v in get_matrix_types(_)]
        if not matrices:
            continue
        if include_tuple:
            if rows is None and columns is None:
                tuples = [
                    _matrix_tuple(r, c)
                    for r in range(2, 5)
                    for c in range(2, 5)
                ]
            elif rows is None:
                tuples = [_matrix_tuple(r, columns) for r in range(2, 5)]
            elif columns is None:
                tuples = [_matrix_tuple(rows, c) for c in range(2, 5)]
            else:
                tuples = [_matrix_tuple(rows, columns)]
        else:
            tuples = []
        yield union_name, f'''{union_name} = {union([*matrices, *tuples])}'''
    yield 'AnyAnyMatrixSquare', f'''AnyAnyMatrixSquare = {union(['AnyAnyMatrix2x2', 'AnyAnyMatrix3x3', 'AnyAnyMatrix4x4'])}'''


def generate_mat_typevars():
    typevars = [
        ('_MT', get_matrix_types()),
        ('_NF32FDMSQRT', get_matrix_types(lambda m: m.rows == m.columns and m.data_type in 'fd' and not (m.data_type == 'f' and m.data_size == 32))),
        ('_NF32M2XNT', get_matrix_types(lambda m: m.rows == 2 and not (m.data_type == 'f' and m.data_size == 32))),
        ('_NF32M3XNT', get_matrix_types(lambda m: m.rows == 3 and not (m.data_type == 'f' and m.data_size == 32))),
        ('_NF32M4XNT', get_matrix_types(lambda m: m.rows == 4 and not (m.data_type == 'f' and m.data_size == 32))),
        ('_NF32M2X2T', get_matrix_types(lambda m: m.rows == 2 and m.columns == 2 and not (m.data_type == 'f' and m.data_size == 32))),
        ('_NF32M2X3T', get_matrix_types(lambda m: m.rows == 2 and m.columns == 3 and not (m.data_type == 'f' and m.data_size == 32))),
        ('_NF32M2X4T', get_matrix_types(lambda m: m.rows == 2 and m.columns == 4 and not (m.data_type == 'f' and m.data_size == 32))),
        ('_NF32M3X2T', get_matrix_types(lambda m: m.rows == 3 and m.columns == 2 and not (m.data_type == 'f' and m.data_size == 32))),
        ('_NF32M3X3T', get_matrix_types(lambda m: m.rows == 3 and m.columns == 3 and not (m.data_type == 'f' and m.data_size == 32))),
        ('_NF32M3X4T', get_matrix_types(lambda m: m.rows == 3 and m.columns == 4 and not (m.data_type == 'f' and m.data_size == 32))),
        ('_NF32M4X2T', get_matrix_types(lambda m: m.rows == 4 and m.columns == 2 and not (m.data_type == 'f' and m.data_size == 32))),
        ('_NF32M4X3T', get_matrix_types(lambda m: m.rows == 4 and m.columns == 3 and not (m.data_type == 'f' and m.data_size == 32))),
        ('_NF32M4X4T', get_matrix_types(lambda m: m.rows == 4 and m.columns == 4 and not (m.data_type == 'f' and m.data_size == 32))),
    ]
    return '\n'.join(f'''{name} = TypeVar('{name}', {', '.join(types)})''' for name, types in typevars) + '\n'


def generate_mat_stub(name):
    matrix = inspect_matrix(name)
    matrxc_union = matrix_union(
        data_type=matrix.data_type,
        rows=matrix.rows,
        columns=matrix.columns,
    )
    vec = vector_name(matrix.data_type, matrix.columns)
    mvec = vector_name(matrix.data_type, matrix.columns, m=True)

    matrx2_union = matrix_union(
        data_type=matrix.data_type,
        rows=matrix.rows, columns=2
    )
    matrx2 = matrix_name(matrix.data_type, matrix.rows, 2)
    matrx3_union = matrix_union(
        data_type=matrix.data_type,
        rows=matrix.rows, columns=3
    )
    matrx3 = matrix_name(matrix.data_type, matrix.rows, 3)
    matrx4_union = matrix_union(
        data_type=matrix.data_type,
        rows=matrix.rows, columns=4
    )
    matrx4 = matrix_name(matrix.data_type, matrix.rows, 4)
    vecr_union = vector_union(
        data_type=matrix.data_type,
        data_size=matrix.data_size,
        size=matrix.rows
    )
    vecc = vector_name(matrix.data_type, matrix.columns)
    if matrix.rows == matrix.columns:
        vecr_minus_one_union = vector_union(
            data_type=matrix.data_type,
            data_size=matrix.data_size,
            size=matrix.rows - 1
        )
        vecc_minus_one = vector_name(matrix.data_type, matrix.columns - 1)
    else:
        vecr_minus_one_union = None
        vecc_minus_one = None

    return [name, *matrix.aliases], textwrap.dedent(f"""{"".join(f'''
    {alias} = {name}''' for alias in matrix.aliases)}

    class {name}:

        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, x: glm_typing.Number, /) -> None: ...
        @overload
        def __init__(self, {', '.join(f'_{c}: glm_typing.Number' for c in range(matrix.rows * matrix.columns))}, /) -> None: ...
        @overload
        def __init__(self, x: {union([matrix_union(rows=matrix.rows, columns=matrix.columns), *(matrix_union(data_type=matrix.data_type, rows=r, columns=c) for r in range(matrix.rows, 5) for c in range(matrix.columns, 5))])}, /) -> None: ...

        def length(self) -> Literal[{matrix.rows}]: ...
        def __len__(self) -> Literal[{matrix.rows}]: ...
        def __contains__(self, value: Any) -> bool: ...
        def __iter__(self) -> Generator[{mvec}, None, None]: ...

        @overload
        def __getitem__(self, index: Tuple[int, int]) -> {matrix.python_type}: ...
        @overload
        def __getitem__(self, index: int) -> {mvec}: ...

        @overload
        def __setitem__(self, index: Tuple[int, int], value: glm_typing.Number) -> None: ...
        @overload
        def __setitem__(self, index: int, value: Union[{vec}, {mvec}]) -> None: ...

        def __neg__(self) -> {name}: ...
        def __pos__(self) -> {name}: ...

        def __eq__(self, other: Any) -> bool: ...
        def __ne__(self, other: Any) -> bool: ...

        def to_list(self) -> List[List[{matrix.python_type}]]: ...
        def to_tuple(self) -> Tuple[{', '.join(f'Tuple[{", ".join(matrix.python_type for i in range(matrix.columns))}]' for i in range(matrix.rows))}]: ...
        def to_bytes(self) -> bytes: ...

        @staticmethod
        def from_bytes(bytes: bytes, /) -> {name}: ...

        def __add__(self, other: {matrxc_union}) -> {name}: ...
        def __radd__(self, other: {matrxc_union}) -> {name}: ...
        def __iadd__(self, other: {matrxc_union}) -> {name}: ...

        def __sub__(self, other: {matrxc_union}) -> {name}: ...
        def __rsub__(self, other: {matrxc_union}) -> {name}: ...
        def __isub__(self, other: {matrxc_union}) -> {name}: ...

        @overload
        def __mul__(self, other: {matrx2_union}) -> {matrx2}: ...
        @overload
        def __mul__(self, other: {matrx3_union}) -> {matrx3}: ...
        @overload
        def __mul__(self, other: {matrx4_union}) -> {matrx4}: ...
        @overload
        def __mul__(self, other: {vecr_union}) -> {vecc}: ...{f'''
        @overload
        def __mul__(self, other: {vecr_minus_one_union}) -> {vecc_minus_one}: ...''' if vecr_minus_one_union and vecc_minus_one else ''}
        @overload
        def __rmul__(self, other: {matrx2_union}) -> {matrx2}: ...
        @overload
        def __rmul__(self, other: {matrx3_union}) -> {matrx3}: ...
        @overload
        def __rmul__(self, other: {matrx4_union}) -> {matrx4}: ...
        @overload
        def __rmul__(self, other: {vecr_union}) -> {vecc}: ...{f'''
        @overload
        def __rmul__(self, other: {vecr_minus_one_union}) -> {vecc_minus_one}: ...''' if vecr_minus_one_union and vecc_minus_one else ''}
        @overload
        def __imul__(self, other: {matrx2_union}) -> {matrx2}: ...
        @overload
        def __imul__(self, other: {matrx3_union}) -> {matrx3}: ...
        @overload
        def __imul__(self, other: {matrx4_union}) -> {matrx4}: ...
        @overload
        def __imul__(self, other: {vecr_union}) -> {vecc}: ...{f'''
        @overload
        def __imul__(self, other: {vecr_minus_one_union}) -> {vecc_minus_one}: ...''' if vecr_minus_one_union and vecc_minus_one else ''}{f'''

        @overload
        def __truediv__(self, other: {matrxc_union}) -> {name}: ...
        @overload
        def __truediv__(self, other: {vecr_union}) -> {vecc}: ...
        @overload
        def __rtruediv__(self, other: {matrxc_union}) -> {name}: ...
        @overload
        def __rtruediv__(self, other: {vecr_union}) -> {vecc}: ...
        @overload
        def __itruediv__(self, other: {matrxc_union}) -> {name}: ...
        @overload
        def __itruediv__(self, other: {vecr_union}) -> {vecc}: ...''' if matrix.rows == matrix.columns else ''}

        @overload
        def __matmul__(self, other: {matrx2_union}) -> {matrx2}: ...
        @overload
        def __matmul__(self, other: {matrx3_union}) -> {matrx3}: ...
        @overload
        def __matmul__(self, other: {matrx4_union}) -> {matrx4}: ...
        @overload
        def __matmul__(self, other: {vecr_union}) -> {vecc}: ...{f'''
        @overload
        def __matmul__(self, other: {vecr_minus_one_union}) -> {vecc_minus_one}: ...''' if vecr_minus_one_union and vecc_minus_one else ''}
        @overload
        def __rmatmul__(self, other: {matrx2_union}) -> {matrx2}: ...
        @overload
        def __rmatmul__(self, other: {matrx3_union}) -> {matrx3}: ...
        @overload
        def __rmatmul__(self, other: {matrx4_union}) -> {matrx4}: ...
        @overload
        def __rmatmul__(self, other: {vecr_union}) -> {vecc}: ...{f'''
        @overload
        def __rmatmul__(self, other: {vecr_minus_one_union}) -> {vecc_minus_one}: ...''' if vecr_minus_one_union and vecc_minus_one else ''}
        @overload
        def __imatmul__(self, other: {matrx2_union}) -> {matrx2}: ...
        @overload
        def __imatmul__(self, other: {matrx3_union}) -> {matrx3}: ...
        @overload
        def __imatmul__(self, other: {matrx4_union}) -> {matrx4}: ...
        @overload
        def __imatmul__(self, other: {vecr_union}) -> {vecc}: ...{f'''
        @overload
        def __imatmul__(self, other: {vecr_minus_one_union}) -> {vecc_minus_one}: ...''' if vecr_minus_one_union and vecc_minus_one else ''}
    """)


def _matrix_tuple(rows, columns):
    column = f"""Tuple[{', '.join('Number' for i in range(columns))}]"""
    return f"""Tuple[{', '.join(column for i in range(rows))}]"""

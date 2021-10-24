
__all__ = ['generate_func_matrix_stub']

import textwrap

from matrixtype import get_matrix_types, inspect_matrix


def generate_func_matrix_stub():
    names = [
        'determinant', 'inverse', 'matrixCompMult', 'outerProduct',
        'transpose',
    ]
    return names, textwrap.dedent(f"""
    def determinant(m: glm_typing.AnyAnyMatrixSquare, /) -> float: ...
    {"".join(f'''
    @overload
    def inverse(m: glm_typing.F32Matrix{i}x{i}, /) -> mat{i}x{i}: ...''' for i in range(2, 5))}
    @overload
    def inverse(m: _NF32FDMSQRT, /) -> _NF32FDMSQRT: ...
    @overload
    def inverse(q: _QT, /) -> _QT: ...
    {"".join(f'''
    @overload
    def matrixCompMult(x: glm_typing.F32Matrix{i}x{i}, y: glm_typing.F32Matrix{i}x{i}, /) -> mat{i}x{i}: ...''' for i in range(2, 5))}
    @overload
    def matrixCompMult(x: _NF32FDMSQRT, y: _NF32FDMSQRT, /) -> _NF32FDMSQRT: ...
    {"".join(f'''
    @overload
    def outerProduct(c: glm_typing.F32Vector{c}, r: glm_typing.F32Vector{r}, /) -> mat{r}x{c}: ...
    @overload
    def outerProduct(c: dvec{c}, r: dvec{r}, /) -> mat{r}x{c}: ...''' for c in range(2, 5) for r in range(2, 5))}
    {"".join(f'''
    @overload
    def transpose(x: glm_typing.F32Matrix{matrix.rows}x{matrix.columns}, /) -> {matrix.data_type}mat{matrix.columns}x{matrix.rows}: ...''' for matrix in (inspect_matrix(n) for n in get_matrix_types(lambda m: m.data_type == 'f' and m.data_size == 32)))}{"".join(f'''
    @overload
    def transpose(x: {matrix.name}, /) -> {matrix.data_type}mat{matrix.columns}x{matrix.rows}: ...''' for matrix in (inspect_matrix(n) for n in get_matrix_types(lambda m: not (m.data_type == 'f' and m.data_size == 32))))}
    """)

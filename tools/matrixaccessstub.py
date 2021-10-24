
__all__ = ['generate_matrix_access_stub']

import textwrap

from matrixtype import get_matrix_types, inspect_matrix


def generate_matrix_access_stub():
    names = [
        'column', 'row',
    ]
    return names, textwrap.dedent(f"""
    {"".join(f'''
    @overload
    def column(m: glm_typing.F32Matrix{matrix.rows}x{matrix.columns}, index: int, /) -> vec{matrix.columns}: ...
    @overload
    def column(m: glm_typing.F32Matrix{matrix.rows}x{matrix.columns}, index: int, x: glm_typing.F32Vector{matrix.columns}, /) -> {matrix.name}: ...''' for matrix in (inspect_matrix(n) for n in get_matrix_types(lambda m: m.data_type == 'f' and m.data_size == 32)))}{"".join(f'''
    @overload
    def column(m: {matrix.name}, index: int, /) -> {matrix.data_type}vec{matrix.columns}: ...
    @overload
    def column(m: {matrix.name}, index: int, x: Union[{matrix.data_type}vec{matrix.columns}, {matrix.data_type}mvec{matrix.columns}], /) -> {matrix.name}: ...''' for matrix in (inspect_matrix(n) for n in get_matrix_types(lambda m: not (m.data_type == 'f' and m.data_size == 32))))}
    {"".join(f'''
    @overload
    def row(m: glm_typing.F32Matrix{matrix.rows}x{matrix.columns}, index: int, /) -> vec{matrix.rows}: ...
    @overload
    def row(m: glm_typing.F32Matrix{matrix.rows}x{matrix.columns}, index: int, x: glm_typing.F32Vector{matrix.rows}, /) -> {matrix.name}: ...''' for matrix in (inspect_matrix(n) for n in get_matrix_types(lambda m: m.data_type == 'f' and m.data_size == 32)))}{"".join(f'''
    @overload
    def row(m: {matrix.name}, index: int, /) -> {matrix.data_type}vec{matrix.rows}: ...
    @overload
    def row(m: {matrix.name}, index: int, x: Union[{matrix.data_type}vec{matrix.rows}, {matrix.data_type}mvec{matrix.rows}], /) -> {matrix.name}: ...''' for matrix in (inspect_matrix(n) for n in get_matrix_types(lambda m: not (m.data_type == 'f' and m.data_size == 32))))}
    """)

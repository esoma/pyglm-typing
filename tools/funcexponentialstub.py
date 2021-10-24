
__all__ = ['generate_func_exponential_stub']

import textwrap

from vecstub import vector_tuple


def generate_func_exponential_stub():
    names = ['exp', 'exp2', 'inversesqrt', 'log', 'log2', 'pow', 'sqrt']
    return names, textwrap.dedent(f"""
    @overload
    def exp(x: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def exp(x: {vector_tuple(i)}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def exp(x: _FDVT, /) -> _FDVT: ...
    @overload
    def exp(x: _QT, /) -> _QT: ...

    @overload
    def exp2(x: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def exp2(x: {vector_tuple(i)}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def exp2(x: _FDVT, /) -> _FDVT: ...

    @overload
    def inversesqrt(x: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def inversesqrt(x: {vector_tuple(i)}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def inversesqrt(x: _FDVT, /) -> _FDVT: ...

    @overload
    def log(x: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def log(x: {vector_tuple(i)}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def log(x: _FDVT, /) -> _FDVT: ...
    @overload
    def log(x: _QT, /) -> _QT: ...

    @overload
    def log2(x: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def log2(x: {vector_tuple(i)}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def log2(x: _FDVT, /) -> _FDVT: ...

    @overload
    def pow(base: glm_typing.Number, exponent: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def pow(base: glm_typing.F32Vector{i}, exponent: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def pow(base: _NF32DFVT, exponent: _NF32DFVT, /) -> _NF32DFVT: ...
    @overload
    def pow(base: _QT, exponent: _QT, /) -> _QT: ...

    @overload
    def sqrt(x: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def sqrt(x: {vector_tuple(i)}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def sqrt(x: _FDVT, /) -> _FDVT: ...
    @overload
    def sqrt(x: _QT, /) -> _QT: ...
    """)

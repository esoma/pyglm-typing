
__all__ = ['generate_func_trigonometric_stub']

import textwrap


def generate_func_trigonometric_stub():
    names = [
        'acos', 'acosh',
        'asin', 'asinh',
        'atan', 'atanh',
        'cos', 'cosh',
        'degrees', 'radians',
        'sin', 'sinh',
        'tan', 'tanh',
    ]
    return names, textwrap.dedent(f"""
    @overload
    def acos(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def acos(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def acos(x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def acosh(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def acosh(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def acosh(x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def asin(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def asin(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def asin(x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def asinh(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def asinh(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def asinh(x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def atan(y_over_x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def atan(y_over_x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def atan(y_over_x: _NF32DFVT, /) -> _NF32DFVT: ...
    @overload
    def atan(y: glm_typing.Number, x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def atan(y: glm_typing.F32Vector{i}, x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def atan(y: _NF32DFVT, x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def atanh(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def atanh(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def atanh(x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def cos(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def cos(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def cos(x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def cosh(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def cosh(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def cosh(x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def degrees(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def degrees(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def degrees(x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def radians(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def radians(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def radians(x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def sin(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def sin(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def sin(x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def sinh(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def sinh(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def sinh(x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def tan(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def tan(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def tan(x: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def tanh(x: glm_typing.Number, /) -> float: ...{"".join(f'''
    @overload
    def tanh(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def tanh(x: _NF32DFVT, /) -> _NF32DFVT: ...
    """)

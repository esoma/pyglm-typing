
__all__ = ['generate_ulp_stub']

import textwrap


def generate_ulp_stub():
    names = ['float_distance', 'next_float', 'prev_float']
    return names, textwrap.dedent(f"""
    @overload
    def float_distance(x: glm_typing.Number, y: glm_typing.Number) -> float: ...{''.join(f'''
    @overload
    def float_distance(x: glm_typing.F32Vector{i}, y: glm_typing.F32Vector{i}, /) -> ivec{i}: ...
    @overload
    def float_distance(x: dvec{i}, y: dvec{i}, /) -> i64vec{i}: ...''' for i in range(1, 5))}

    @overload
    def next_float(x: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def next_float(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def next_float(x: _NF32DFVT, /) -> _NF32DFVT: ...
    @overload
    def next_float(x: glm_typing.Number, ULPs: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def next_float(x: glm_typing.F32Vector{i}, ULPs: glm_typing.Number, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def next_float(x: _NF32DFVT, ULPs: glm_typing.Number, /) -> _NF32DFVT: ...{''.join(f'''
    @overload
    def next_float(x: glm_typing.F32Vector{i}, ULPs: glm_typing.I32Vector{i}, /) -> vec{i}: ...
    @overload
    def next_float(x: _NF32DFV{i}T, ULPs: glm_typing.I32Vector{i}, /) -> _NF32DFV{i}T: ...''' for i in range(1, 5))}

    @overload
    def prev_float(x: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def prev_float(x: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def prev_float(x: _NF32DFVT, /) -> _NF32DFVT: ...
    @overload
    def prev_float(x: glm_typing.Number, ULPs: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def prev_float(x: glm_typing.F32Vector{i}, ULPs: glm_typing.Number, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def prev_float(x: _NF32DFVT, ULPs: glm_typing.Number, /) -> _NF32DFVT: ...{''.join(f'''
    @overload
    def prev_float(x: glm_typing.F32Vector{i}, ULPs: glm_typing.I32Vector{i}, /) -> vec{i}: ...
    @overload
    def prev_float(x: _NF32DFV{i}T, ULPs: glm_typing.I32Vector{i}, /) -> _NF32DFV{i}T: ...''' for i in range(1, 5))}
    """)

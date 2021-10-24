
__all__ = ['generate_round_stub']

import textwrap


def generate_round_stub():
    names = [
        'ceilMultiple',
        'ceilPowerOfTwo',
        'floorMultiple',
        'floorPowerOfTwo',
        'roundMultiple',
        'roundPowerOfTwo',
    ]
    return names, textwrap.dedent(f"""
    @overload
    def ceilMultiple(v: glm_typing.Number, Multiple: glm_typing.Number, /) -> int: ...{''.join(f'''
    @overload
    def ceilMultiple(v: glm_typing.I32Vector{i}, Multiple: glm_typing.I32Vector{i}, /) -> ivec{i}: ...''' for i in range(1, 5))}
    @overload
    def ceilMultiple(v: _NI32IVT, Multiple: _NI32IVT, /) -> _NI32IVT: ...

    @overload
    def ceilPowerOfTwo(v: glm_typing.Number, Multiple: glm_typing.Number, /) -> int: ...{''.join(f'''
    @overload
    def ceilPowerOfTwo(v: glm_typing.I32Vector{i}, Multiple: glm_typing.I32Vector{i}, /) -> ivec{i}: ...''' for i in range(1, 5))}
    @overload
    def ceilPowerOfTwo(v: _NI32IVT, Multiple: _NI32IVT, /) -> _NI32IVT: ...

    @overload
    def floorMultiple(v: glm_typing.Number, Multiple: glm_typing.Number, /) -> int: ...{''.join(f'''
    @overload
    def floorMultiple(v: glm_typing.I32Vector{i}, Multiple: glm_typing.I32Vector{i}, /) -> ivec{i}: ...''' for i in range(1, 5))}
    @overload
    def floorMultiple(v: _NI32IVT, Multiple: _NI32IVT, /) -> _NI32IVT: ...

    @overload
    def floorPowerOfTwo(v: glm_typing.Number, Multiple: glm_typing.Number, /) -> int: ...{''.join(f'''
    @overload
    def floorPowerOfTwo(v: glm_typing.I32Vector{i}, Multiple: glm_typing.I32Vector{i}, /) -> ivec{i}: ...''' for i in range(1, 5))}
    @overload
    def floorPowerOfTwo(v: _NI32IVT, Multiple: _NI32IVT, /) -> _NI32IVT: ...

    @overload
    def roundMultiple(v: glm_typing.Number, Multiple: glm_typing.Number, /) -> int: ...{''.join(f'''
    @overload
    def roundMultiple(v: glm_typing.I32Vector{i}, Multiple: glm_typing.I32Vector{i}, /) -> ivec{i}: ...''' for i in range(1, 5))}
    @overload
    def roundMultiple(v: _NI32IVT, Multiple: _NI32IVT, /) -> _NI32IVT: ...

    @overload
    def roundPowerOfTwo(v: glm_typing.Number, Multiple: glm_typing.Number, /) -> int: ...{''.join(f'''
    @overload
    def roundPowerOfTwo(v: glm_typing.I32Vector{i}, Multiple: glm_typing.I32Vector{i}, /) -> ivec{i}: ...''' for i in range(1, 5))}
    @overload
    def roundPowerOfTwo(v: _NI32IVT, Multiple: _NI32IVT, /) -> _NI32IVT: ...
    """)

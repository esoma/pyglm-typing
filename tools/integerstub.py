
__all__ = ['generate_integer_stub']

import textwrap


def generate_integer_stub():
    names = [
        'iround', 'uround',
    ]
    return names, textwrap.dedent(f"""
    @overload
    def iround(x: glm_typing.Number, /) -> int: ...{"".join(f'''
    @overload
    def iround(x: glm_typing.F32Vector{i}, /) -> ivec{i}: ...
    @overload
    def iround(x: _NF32DFV{i}T, /) -> ivec{i}: ...''' for i in range(1, 5))}

    @overload
    def uround(x: glm_typing.Number, /) -> int: ...{"".join(f'''
    @overload
    def uround(x: glm_typing.F32Vector{i}, /) -> uvec{i}: ...
    @overload
    def uround(x: _NF32DFV{i}T, /) -> uvec{i}: ...''' for i in range(1, 5))}
    """)

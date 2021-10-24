
__all__ = ['generate_noise_stub']

import textwrap


def generate_noise_stub():
    names = [
        'perlin', 'simplex',
    ]
    return names, textwrap.dedent(f"""
    @overload
    def perlin(p: glm_typing.FDAnyVectorAny, /) -> float: ...{"".join(f'''
    @overload
    def perlin(p: glm_typing.F32Vector{i}, rep: glm_typing.F32Vector{i}, /) -> float: ...''' for i in range(1, 5))}
    @overload
    def perlin(p: _NF32DFVT, rep: _NF32DFVT, /) -> float: ...

    def simplex(p: glm_typing.FDAnyVectorAny, /) -> float: ...
    """)

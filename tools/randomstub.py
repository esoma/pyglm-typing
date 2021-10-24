
__all__ = ['generate_random_stub']

import textwrap


def generate_random_stub():
    names = [
        'ballRand', 'circularRand', 'diskRand',
        'gaussRand', 'linearRand',
        'setSeed',
        'sphericalRand',
    ]
    return names, textwrap.dedent(f"""
    def ballRand(Radius: glm_typing.Number, /) -> vec3: ...

    def circularRand(Radius: glm_typing.Number, /) -> vec2: ...

    def diskRand(Radius: glm_typing.Number, /) -> vec2: ...

    @overload
    def gaussRand(Mean: glm_typing.Number, Deviation: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def gaussRand(Mean: glm_typing.F32Vector{i}, Deviation: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def gaussRand(Mean: _NF32VT, Deviation: _NF32VT, /) -> _NF32VT: ...

    @overload
    def linearRand(Min: glm_typing.Number, Max: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def linearRand(Min: glm_typing.F32Vector{i}, Max: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def linearRand(Min: _NF32VT, Max: _NF32VT, /) -> _NF32VT: ...

    def setSeed(seed: SupportsInt, /) -> None: ...

    def sphericalRand(Radius: glm_typing.Number, /) -> vec3: ...
    """)

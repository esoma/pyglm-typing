
__all__ = ['generate_polar_coordinates_stub']

import textwrap


def generate_polar_coordinates_stub():
    names = ['euclidean', 'polar']
    return names, textwrap.dedent(f"""
    @overload
    def euclidean(polar: glm_typing.F32Vector2, /) -> vec3: ...
    @overload
    def euclidean(polar: dvec2, /) -> dvec3: ...

    @overload
    def polar(euclidean: glm_typing.F32Vector3, /) -> vec3: ...
    @overload
    def polar(euclidean: _NF32DFV3T, /) -> _NF32DFV3T: ...
    """)

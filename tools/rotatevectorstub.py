
__all__ = ['generate_rotate_vector_stub']

import textwrap


def generate_rotate_vector_stub():
    names = ['orientation']
    return names, textwrap.dedent(f"""
    @overload
    def orientation(Normal: glm_typing.F32Vector3, Up: glm_typing.F32Vector3, /) -> mat4x4: ...
    @overload
    def orientation(Normal: dvec3, Up: dvec3, /) -> dmat4x4: ...

    @overload
    def rotateX(v: glm_typing.F32Vector3, angle: glm_typing.Number) -> vec3: ...
    @overload
    def rotateX(v: _NF32DFV3T, angle: glm_typing.Number) -> _NF32DFV3T: ...
    @overload
    def rotateX(v: glm_typing.F32Vector4, angle: glm_typing.Number) -> vec4: ...
    @overload
    def rotateX(v: _NF32DFV4T, angle: glm_typing.Number) -> _NF32DFV4T: ...

    @overload
    def rotateY(v: glm_typing.F32Vector3, angle: glm_typing.Number) -> vec3: ...
    @overload
    def rotateY(v: _NF32DFV3T, angle: glm_typing.Number) -> _NF32DFV3T: ...
    @overload
    def rotateY(v: glm_typing.F32Vector4, angle: glm_typing.Number) -> vec4: ...
    @overload
    def rotateY(v: _NF32DFV4T, angle: glm_typing.Number) -> _NF32DFV4T: ...

    @overload
    def rotateZ(v: glm_typing.F32Vector3, angle: glm_typing.Number) -> vec3: ...
    @overload
    def rotateZ(v: _NF32DFV3T, angle: glm_typing.Number) -> _NF32DFV3T: ...
    @overload
    def rotateZ(v: glm_typing.F32Vector4, angle: glm_typing.Number) -> vec4: ...
    @overload
    def rotateZ(v: _NF32DFV4T, angle: glm_typing.Number) -> _NF32DFV4T: ...
    """)

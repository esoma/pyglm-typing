
__all__ = ['generate_matrix_projection_stub']

import textwrap


def generate_matrix_projection_stub():
    names = [
        'pickMatrix',
        'projectNO', 'project', 'projectZO',
        'unProjectNO', 'unProject', 'unProjectZO',
    ]
    return names, textwrap.dedent(f"""
    @overload
    def pickMatrix(center: glm_typing.F32Vector2, delta: glm_typing.F32Vector2, viewport: glm_typing.F32Vector4, /) -> mat4x4: ...
    @overload
    def pickMatrix(center: dvec2, delta: dvec2, viewport: dvec4, /) -> dmat4x4: ...

    @overload
    def projectNO(obj: glm_typing.F32Vector3, model: glm_typing.F32Matrix4x4, proj: glm_typing.F32Matrix4x4, viewport: glm_typing.F32Vector4, /) -> vec3: ...
    @overload
    def projectNO(obj: dvec3, model: dmat4x4, proj: dmat4x4, viewport: dvec4, /) -> dvec3: ...

    @overload
    def project(obj: glm_typing.F32Vector3, model: glm_typing.F32Matrix4x4, proj: glm_typing.F32Matrix4x4, viewport: glm_typing.F32Vector4, /) -> vec3: ...
    @overload
    def project(obj: dvec3, model: dmat4x4, proj: dmat4x4, viewport: dvec4, /) -> dvec3: ...

    @overload
    def projectZO(obj: glm_typing.F32Vector3, model: glm_typing.F32Matrix4x4, proj: glm_typing.F32Matrix4x4, viewport: glm_typing.F32Vector4, /) -> vec3: ...
    @overload
    def projectZO(obj: dvec3, model: dmat4x4, proj: dmat4x4, viewport: dvec4, /) -> dvec3: ...

    @overload
    def unProjectNO(obj: glm_typing.F32Vector3, model: glm_typing.F32Matrix4x4, proj: glm_typing.F32Matrix4x4, viewport: glm_typing.F32Vector4, /) -> vec3: ...
    @overload
    def unProjectNO(obj: dvec3, model: dmat4x4, proj: dmat4x4, viewport: dvec4, /) -> dvec3: ...

    @overload
    def unProject(obj: glm_typing.F32Vector3, model: glm_typing.F32Matrix4x4, proj: glm_typing.F32Matrix4x4, viewport: glm_typing.F32Vector4, /) -> vec3: ...
    @overload
    def unProject(obj: dvec3, model: dmat4x4, proj: dmat4x4, viewport: dvec4, /) -> dvec3: ...

    @overload
    def unProjectZO(obj: glm_typing.F32Vector3, model: glm_typing.F32Matrix4x4, proj: glm_typing.F32Matrix4x4, viewport: glm_typing.F32Vector4, /) -> vec3: ...
    @overload
    def unProjectZO(obj: dvec3, model: dmat4x4, proj: dmat4x4, viewport: dvec4, /) -> dvec3: ...
    """)

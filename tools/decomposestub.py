
__all__ = ['generate_decompose_stub']

import textwrap


def generate_decompose_stub():
    names = ['decompose']
    return names, textwrap.dedent(f"""
    @overload
    def decompose(modelMatrix: glm_typing.F32Matrix3x3, scale: glm_typing.F32Vector3, orientation: glm_typing.F32Quaternion, translation: glm_typing.F32Vector3, skew: glm_typing.F32Vector3, perspective: glm_typing.F32Vector4, /) -> bool: ...
    @overload
    def decompose(modelMatrix: dmat4x4, scale: dvec3, orientation: dquat, translation: dvec3, skew: dvec3, perspective: dvec4, /) -> bool: ...
    """)

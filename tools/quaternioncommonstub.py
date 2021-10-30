
__all__ = ['generate_quaternion_common_stub']

import textwrap


def generate_quaternion_common_stub():
    names = ['conjugate', 'lerp', 'slerp']
    return names, textwrap.dedent(f"""
    @overload
    def conjugate(q: glm_typing.F32Quaternion, /) -> quat: ...
    @overload
    def conjugate(q: _NF32QT, /) -> _NF32QT: ...

    @overload
    def lerp(x: glm_typing.F32Quaternion, y: glm_typing.F32Quaternion, a: glm_typing.Number, /) -> quat: ...
    @overload
    def lerp(x: _NF32QT, y: _NF32QT, a: glm_typing.Number, /) -> _NF32QT: ...

    @overload
    def slerp(x: glm_typing.F32Quaternion, y: glm_typing.F32Quaternion, a: glm_typing.Number, /) -> quat: ...
    @overload
    def slerp(x: _NF32QT, y: _NF32QT, a: glm_typing.Number, /) -> _NF32QT: ...
    @overload
    def slerp(x: glm_typing.F32Vector3, y: glm_typing.F32Vector3, a: glm_typing.Number, /) -> vec3: ...
    @overload
    def slerp(x: _NF32DFV3T, y: _NF32DFV3T, a: glm_typing.Number, /) -> _NF32DFV3T: ...
    """)


__all__ = ['generate_quaternion_trigonometric_stub']

import textwrap


def generate_quaternion_trigonometric_stub():
    names = ['angle', 'angleAxis', 'axis']
    return names, textwrap.dedent(f"""
    def angle(x: _QT, /) -> float: ...

    @overload
    def angleAxis(angle: glm_typing.Number, axis: glm_typing.F32Vector3, /) -> quat: ...
    @overload
    def angleAxis(angle: glm_typing.Number, axis: dvec3, /) -> dquat: ...

    @overload
    def axis(x: glm_typing.F32Quat, /) -> vec3: ...
    @overload
    def axis(x: dquat, /) -> dvec3: ...
    """)

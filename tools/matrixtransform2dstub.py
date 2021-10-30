
__all__ = ['generate_matrix_transform_2d_stub']

import textwrap


def generate_matrix_transform_2d_stub():
    names = ['shearX', 'shearY']
    return names, textwrap.dedent(f"""
    @overload
    def shearX(m: glm_typing.F32Matrix3x3, y: glm_typing.Number, /) -> mat3x3: ...
    @overload
    def shearX(m: _NF32M3X3T, y: glm_typing.Number, /) -> _NF32M3X3T: ...

    @overload
    def shearY(m: glm_typing.F32Matrix3x3, y: glm_typing.Number, /) -> mat3x3: ...
    @overload
    def shearY(m: _NF32M3X3T, y: glm_typing.Number, /) -> _NF32M3X3T: ...
    """)

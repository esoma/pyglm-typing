
__all__ = ['generate_func_packing_stub']

import textwrap


def generate_func_packing_stub():
    names = [
        'packDouble2x32',
        'packHalf2x16',
        'packSnorm2x16',
        'packSnorm4x8',
        'packUnorm2x16',
        'packUnorm4x8',
        'unpackDouble2x32',
        'unpackHalf2x16',
        'unpackSnorm2x16',
        'unpackSnorm4x8',
        'unpackUnorm2x16',
        'unpackUnorm4x8',
    ]
    return names, textwrap.dedent(f"""
    def packDouble2x32(v: glm_typing.U32Vector2, /) -> float: ...

    def packHalf2x16(v: glm_typing.F32Vector2, /) -> int: ...

    def packSnorm2x16(v: glm_typing.F32Vector2, /) -> int: ...

    def packSnorm4x8(v: glm_typing.F32Vector4, /) -> int: ...

    def packUnorm2x16(v: glm_typing.F32Vector2, /) -> int: ...

    def packUnorm4x8(v: glm_typing.F32Vector4, /) -> int: ...

    def unpackDouble2x32(v: float, /) -> uvec2: ...

    def unpackHalf2x16(v: int, /) -> vec2: ...

    def unpackSnorm2x16(p: int, /) -> vec2: ...

    def unpackSnorm4x8(p: int, /) -> vec4: ...

    def unpackUnorm2x16(p: int, /) -> vec2: ...

    def unpackUnorm4x8(p: int, /) -> vec4: ...
    """)

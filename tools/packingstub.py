
__all__ = ['generate_packing_stub']

import textwrap


def generate_packing_stub():
    names = [
        'packF2x11_1x10',
        'packF3x9_E1x5',
        'packHalf',
        'packHalf1x16',
        'packHalf4x16',
        'packI3x10_1x2',
        'packInt2x16',
        'packInt2x32',
        'packInt2x8',
        'packInt4x16',
        'packInt4x8',
        'packRGBM',
        'packSnorm',
        'packSnorm1x16',
        'packSnorm1x8',
        'packSnorm2x8',
        'packSnorm3x10_1x2',
        'packSnorm4x16',
        'packU3x10_1x2',
        'packUint2x16',
        'packUint2x32',
        'packUint2x8',
        'packUint4x16',
        'packUint4x8',
        'packUnorm',
        'packUnorm1x16',
        'packUnorm1x5_1x6_1x5',
        'packUnorm2x4',
        'packUnorm2x8',
        'packUnorm3x10_1x2',
        'packUnorm4x16',
        'packUnorm4x4',
        'unpackF2x11_1x10',
        'unpackF3x9_E1x5',
        'unpackHalf',
        'unpackHalf1x16',
        'unpackI3x10_1x2',
        'unpackInt2x16',
        'unpackInt2x32',
        'unpackInt2x8',
        'unpackInt4x16',
        'unpackInt4x8',
        'unpackRGBM',
        'unpackSnorm',
        'unpackSnorm1x16',
        'unpackSnorm1x8',
        'unpackSnorm2x8',
        'unpackSnorm3x10_1x2',
        'unpackSnorm4x16',
        'unpackU3x10_1x2',
        'unpackUint2x16',
        'unpackUint2x32',
        'unpackUint2x8',
        'unpackUint4x16',
        'unpackUint4x8',
        'unpackUnorm',
        'unpackUnorm1x16',
        'unpackUnorm1x5_1x6_1x5',
        'unpackUnorm1x8',
        'unpackUnorm2x3_1x2',
        'unpackUnorm2x4',
        'unpackUnorm2x8',
        'unpackUnorm3x10_1x2',
        'unpackUnorm3x5_1x1',
        'unpackUnorm4x16',
        'unpackUnorm4x4',
    ]
    return names, textwrap.dedent(f"""
    def packF2x11_1x10(v: glm_typing.F32Vector3, /) -> int: ...

    def packF3x9_E1x5(v: glm_typing.F32Vector3, /) -> int: ...
    {"".join(f'''
    @overload
    def packHalf(v: glm_typing.F32Vector{i}, /) -> u16vec{i}: ...''' for i in range(1, 5))}

    def packHalf1x16(v: float, /) -> int: ...

    def packHalf4x16(v: glm_typing.F32Vector4, /) -> int: ...

    def packI3x10_1x2(v: glm_typing.I32Vector4, /) -> int: ...

    def packInt2x16(v: glm_typing.I16Vector2, /) -> int: ...

    def packInt2x32(v: glm_typing.I32Vector2, /) -> int: ...

    def packInt2x8(v: glm_typing.I8Vector2, /) -> int: ...

    def packInt4x16(v: glm_typing.I16Vector4, /) -> int: ...

    def packInt4x8(v: glm_typing.I8Vector4, /) -> int: ...

    def packRGBM(v: glm_typing.F32Vector3, /) -> vec4: ...
    {"".join(f'''
    @overload
    def packSnorm(t: ctypes.{ctype}, v: glm_typing.F32Vector{i}, /) -> {dtype}vec{i}: ...
    @overload
    def packSnorm(t: ctypes.{ctype}, v: _NF32DFV{i}T, /) -> {dtype}vec{i}: ...''' for i in range(1, 5) for ctype, dtype in [('c_int8', 'i8'), ('c_uint8', 'u8'), ('c_int16', 'i16'), ('c_uint16', 'u16'), ('c_int32', 'i32'), ('c_uint32', 'u32'), ('c_int64', 'i64'), ('c_uint64', 'u64')])}

    def packSnorm1x16(v: float, /) -> int: ...

    def packSnorm1x8(v: float, /) -> int: ...

    def packSnorm2x8(v: glm_typing.F32Vector2, /) -> int: ...

    def packSnorm3x10_1x2(v: glm_typing.F32Vector4, /) -> int: ...

    def packSnorm4x16(v: glm_typing.F32Vector4, /) -> int: ...

    def packU3x10_1x2(v: glm_typing.U32Vector4, /) -> int: ...

    def packUint2x16(v: glm_typing.U16Vector2, /) -> int: ...

    def packUint2x32(v: glm_typing.U32Vector2, /) -> int: ...

    def packUint2x8(v: glm_typing.U8Vector2, /) -> int: ...

    def packUint4x16(v: glm_typing.U16Vector4, /) -> int: ...

    def packUint4x8(v: glm_typing.U16Vector4, /) -> int: ...
    {"".join(f'''
    @overload
    def packUnorm(t: ctypes.{ctype}, v: glm_typing.F32Vector{i}, /) -> {dtype}vec{i}: ...
    @overload
    def packUnorm(t: ctypes.{ctype}, v: _NF32DFV{i}T, /) -> {dtype}vec{i}: ...''' for i in range(1, 5) for ctype, dtype in [('c_uint8', 'u8'), ('c_uint16', 'u16'), ('c_uint32', 'u32'), ('c_uint64', 'u64')])}

    def packUnorm1x16(v: float, /) -> int: ...

    def packUnorm1x5_1x6_1x5(v: glm_typing.F32Vector3, /) -> int: ...

    def packUnorm2x4(v: glm_typing.F32Vector2, /) -> int: ...

    def packUnorm2x8(v: glm_typing.F32Vector2, /) -> int: ...

    def packUnorm3x10_1x2(v: glm_typing.F32Vector4, /) -> int: ...

    def packUnorm4x16(v: glm_typing.F32Vector4, /) -> int: ...

    def packUnorm4x4(v: glm_typing.F32Vector4, /) -> int: ...

    def unpackF2x11_1x10(p: int, /) -> vec3: ...

    def unpackF3x9_E1x5(p: int, /) -> vec3: ...
    {"".join(f'''
    @overload
    def unpackHalf(v: glm_typing.U16Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}

    def unpackHalf1x16(p: int, /) -> float: ...

    def unpackI3x10_1x2(p: int, /) -> ivec4: ...

    def unpackInt2x16(p: int, /) -> i16vec2: ...

    def unpackInt2x32(p: int, /) -> i32vec2: ...

    def unpackInt2x8(p: int, /) -> i8vec2: ...

    def unpackInt4x16(p: int, /) -> i16vec4: ...

    def unpackInt4x8(p: int, /) -> i8vec4: ...

    def unpackRGBM(p: glm_typing.F32Vector4, /) -> vec3: ...
    {"".join(f'''
    @overload
    def unpackSnorm(t: ctypes.{ctype}, v: glm_typing.I32Vector{i}, /) -> {dtype}vec{i}: ...
    @overload
    def unpackSnorm(t: ctypes.{ctype}, v: _NI32IUV{i}T, /) -> {dtype}vec{i}: ...''' for i in range(1, 5) for ctype, dtype in [('c_float', ''), ('c_double', 'd')])}

    def unpackSnorm1x16(p: int, /) -> float: ...

    def unpackSnorm1x8(p: int, /) -> float: ...

    def unpackSnorm2x8(p: int, /) -> vec2: ...

    def unpackSnorm3x10_1x2(p: int, /) -> vec4: ...

    def unpackSnorm4x16(p: int, /) -> vec4: ...

    def unpackU3x10_1x2(p: int, /) -> uvec4: ...

    def unpackUint2x16(p: int, /) -> u16vec2: ...

    def unpackUint2x32(p: int, /) -> u32vec2: ...

    def unpackUint2x8(p: int, /) -> u8vec2: ...

    def unpackUint4x16(p: int, /) -> u16vec4: ...

    def unpackUint4x8(p: int, /) -> u8vec4: ...
    {"".join(f'''
    @overload
    def unpackUnorm(t: ctypes.{ctype}, v: glm_typing.I32Vector{i}, /) -> {dtype}vec{i}: ...
    @overload
    def unpackUnorm(t: ctypes.{ctype}, v: _NI32IUV{i}T, /) -> {dtype}vec{i}: ...''' for i in range(1, 5) for ctype, dtype in [('c_float', ''), ('c_double', 'd')])}

    def unpackUnorm1x16(p: int, /) -> float: ...

    def unpackUnorm1x5_1x6_1x5(p: int, /) -> vec3: ...

    def unpackUnorm1x8(p: int, /) -> float: ...

    def unpackUnorm2x3_1x2(p: int, /) -> vec3: ...

    def unpackUnorm2x4(p: int, /) -> vec2: ...

    def unpackUnorm2x8(p: int, /) -> vec2: ...

    def unpackUnorm3x10_1x2(p: int, /) -> vec4: ...

    def unpackUnorm3x5_1x1(p: int, /) -> vec4: ...

    def unpackUnorm4x16(p: int, /) -> vec4: ...

    def unpackUnorm4x4(p: int, /) -> vec4: ...
    """)

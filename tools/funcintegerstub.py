
__all__ = ['generate_func_integer_stub']

import textwrap


def generate_func_integer_stub():
    names = [
        'bitCount', 'bitfieldExtract', 'bitfieldInsert', 'bitfieldReverse',
        'findLSB', 'findMSB', 'imulExtended', 'uaddCarry', 'umulExtended',
        'usubBorrow',
    ]
    return names, textwrap.dedent(f"""
    @overload
    def bitCount(v: int, /) -> int: ...{"".join(f'''
    @overload
    def bitCount(v: glm_typing.IUAnyVector{i}, /) -> ivec{i}: ...''' for i in range(1, 5))}

    @overload
    def bitfieldExtract(value: int, offset: int, bits: int, /) -> int: ...{"".join(f'''
    @overload
    def bitfieldExtract(v: glm_typing.I32Vector{i}, offset: int, bits: int, /) -> ivec{i}: ...''' for i in range(1, 5))}
    @overload
    def bitfieldExtract(value: _NI32IUVT, offset: int, bits: int, /) -> _NI32IUVT: ...

    @overload
    def bitfieldInsert(base: int, insert: int, offset: int, bits: int, /) -> int: ...{"".join(f'''
    @overload
    def bitfieldInsert(base: glm_typing.I32Vector{i}, insert: glm_typing.I32Vector{i}, offset: int, bits: int, /) -> ivec{i}: ...''' for i in range(1, 5))}
    @overload
    def bitfieldInsert(base: _NI32IUVT, insert: _NI32IUVT, offset: int, bits: int, /) -> _NI32IUVT: ...

    @overload
    def bitfieldReverse(value: int, /) -> int: ...{"".join(f'''
    @overload
    def bitfieldReverse(value: glm_typing.I32Vector{i}, /) -> ivec{i}: ...''' for i in range(1, 5))}
    @overload
    def bitfieldReverse(value: _NI32IUVT, /) -> _NI32IUVT: ...

    @overload
    def findLSB(value: int, /) -> int: ...{"".join(f'''
    @overload
    def findLSB(value: glm_typing.I32Vector{i}, /) -> ivec{i}: ...''' for i in range(1, 5))}
    @overload
    def findLSB(value: _NI32IUVT, /) -> _NI32IUVT: ...

    @overload
    def findMSB(value: int, /) -> int: ...{"".join(f'''
    @overload
    def findMSB(value: glm_typing.I32Vector{i}, /) -> ivec{i}: ...''' for i in range(1, 5))}
    @overload
    def findMSB(value: _NI32IUVT, /) -> _NI32IUVT: ...

    def imulExtended(x: _IVT, y: _IVT, msb: _IVT, lsb: _IVT, /) -> None: ...

    def uaddCarry(x: _UVT, y: _UVT, carry: _UVT, /) -> _UVT: ...

    def umulExtended(x: _UVT, y: _UVT, msb: _UVT, lsb: _UVT, /) -> None: ...

    def usubBorrow(x: _UVT, y: _UVT, borrow: _UVT, /) -> _UVT: ...
    """)

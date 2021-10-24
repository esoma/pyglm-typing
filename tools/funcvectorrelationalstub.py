
__all__ = ['generate_func_vector_relational_stub']

import textwrap


def generate_func_vector_relational_stub():
    names = [
        'all', 'any',
        'equal',
        'greaterThan', 'greaterThanEqual',
        'lessThan', 'lessThanEqual',
        'notEqual',
        'not_',
    ]
    return names, textwrap.dedent(f"""

    def all(v: glm_typing.BAnyVectorAny, /) -> bool: ...

    def any(v: glm_typing.BAnyVectorAny, /) -> bool: ...

    @overload
    def equal(x: glm_typing.Number, y: glm_typing.Number, ULPs: int, /) -> int: ...{"".join(f'''
    @overload
    def equal(x: glm_typing.F32Vector{i}, y: glm_typing.F32Vector{i}, /) -> bvec{i}: ...
    @overload
    def equal(x: _NF32V{i}T, y: _NF32V{i}T, /) -> bvec{i}: ...
    @overload
    def equal(x: glm_typing.F32Vector{i}, y: glm_typing.F32Vector{i}, ULPs_epsilon: Union[glm_typing.Number, ivec{i}, glm_typing.F32Vector{i}], /) -> bvec{i}: ...
    @overload
    def equal(x: _NF32V{i}T, y: _NF32V{i}T, ULPs_epsilon: Union[glm_typing.Number, ivec{i}, glm_typing.F32Vector{i}], /) -> bvec{i}: ...''' for i in range(1, 5))}{"".join(f'''
    @overload
    def equal(x: glm_typing.F32Matrix{i}xAny, y: glm_typing.F32Matrix{i}xAny, /) -> bvec{i}: ...
    @overload
    def equal(x: _NF32M{i}XNT, y: _NF32M{i}XNT, /) -> bvec{i}: ...
    @overload
    def equal(x: glm_typing.F32Matrix{i}xAny, y: glm_typing.F32Matrix{i}xAny, ULPs_epsilon: Union[glm_typing.Number, ivec{i}, glm_typing.F32Vector{i}], /) -> bvec{i}: ...
    @overload
    def equal(x: _NF32M{i}XNT, y: _NF32M{i}XNT, ULPs_epsilon: Union[glm_typing.Number, ivec{i}, glm_typing.F32Vector{i}], /) -> bvec{i}: ...''' for i in range(2, 5))}
    @overload
    def equal(x: _QT, y: _QT, /) -> int: ...

    @overload
    def greaterThan(x: _QT, y: _QT, /) -> bvec4: ...{"".join(f'''
    @overload
    def greaterThan(x: glm_typing.F32Vector{i}, y: glm_typing.F32Vector{i}, /) -> bvec{i}: ...
    @overload
    def greaterThan(x: _NF32V{i}T, y: _NF32V{i}T, /) -> bvec{i}: ...''' for i in range(1, 5))}

    @overload
    def greaterThanEqual(x: _QT, y: _QT, /) -> bvec4: ...{"".join(f'''
    @overload
    def greaterThanEqual(x: glm_typing.F32Vector{i}, y: glm_typing.F32Vector{i}, /) -> bvec{i}: ...
    @overload
    def greaterThanEqual(x: _NF32V{i}T, y: _NF32V{i}T, /) -> bvec{i}: ...''' for i in range(1, 5))}

    @overload
    def lessThan(x: _QT, y: _QT, /) -> bvec4: ...{"".join(f'''
    @overload
    def lessThan(x: glm_typing.F32Vector{i}, y: glm_typing.F32Vector{i}, /) -> bvec{i}: ...
    @overload
    def lessThan(x: _NF32V{i}T, y: _NF32V{i}T, /) -> bvec{i}: ...''' for i in range(1, 5))}

    @overload
    def lessThanEqual(x: _QT, y: _QT, /) -> bvec4: ...{"".join(f'''
    @overload
    def lessThanEqual(x: glm_typing.F32Vector{i}, y: glm_typing.F32Vector{i}, /) -> bvec{i}: ...
    @overload
    def lessThanEqual(x: _NF32V{i}T, y: _NF32V{i}T, /) -> bvec{i}: ...''' for i in range(1, 5))}

    @overload
    def notEqual(x: _QT, y: _QT, /) -> bvec4: ...{"".join(f'''
    @overload
    def notEqual(x: glm_typing.F32Vector{i}, y: glm_typing.F32Vector{i}, /) -> bvec{i}: ...
    @overload
    def notEqual(x: _NF32V{i}T, y: _NF32V{i}T, /) -> bvec{i}: ...''' for i in range(1, 5))}

    def not_(v: glm_typing.BAnyVectorAny, /) -> bool: ...
    """)

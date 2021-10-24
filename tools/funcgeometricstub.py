
__all__ = ['generate_func_geometric_stub']

import textwrap

from vecstub import vector_tuple


def generate_func_geometric_stub():
    names = [
        'cross', 'distance', 'dot', 'faceforward', 'normalize', 'reflect',
        'refract',
    ]
    return names, textwrap.dedent(f"""
    @overload
    def cross(x: glm_typing.F32Vector3, y: glm_typing.F32Vector3, /) -> vec3: ...
    @overload
    def cross(x: _NF32DFV3T, y: _NF32DFV3T, /) -> _NF32DFV3T: ...
    @overload
    def cross(x: _QT, y: _QT, /) -> _QT: ...

    @overload
    def distance(p0: glm_typing.Number, p1: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def distance(p0: glm_typing.F32Vector{i}, p1: glm_typing.F32Vector{i}, /) -> float: ...''' for i in range(1, 5))}
    @overload
    def distance(p0: _NF32DFVT, p1: _NF32DFVT, /) -> float: ...

    @overload
    def dot(x: glm_typing.Number, y: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def dot(x: glm_typing.F32Vector{i}, y: glm_typing.F32Vector{i}, /) -> float: ...''' for i in range(1, 5))}
    @overload
    def dot(x: _NF32DFVT, y: _NF32DFVT, /) -> float: ...
    @overload
    def dot(x: _QT, y: _QT, /) -> float: ...

    @overload
    def faceforward(N: glm_typing.Number, I: glm_typing.Number, Nref: float, /) -> float: ...{''.join(f'''
    @overload
    def faceforward(x: glm_typing.F32Vector{i}, I: glm_typing.F32Vector{i}, Nref: glm_typing.F32Vector{i}, /) -> float: ...''' for i in range(1, 5))}
    @overload
    def faceforward(N: _NF32DFVT, I: _NF32DFVT, Nref: _NF32DFVT, /) -> _NF32DFVT: ...

    def length(x: Union[glm_typing.Number, glm_typing.FDAnyVectorAny, glm_typing.FDAnyQuaternion], /) -> float: ...
    {''.join(f'''
    @overload
    def normalize(x: {vector_tuple(i)}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def normalize(x: _FDVT, /) -> _FDVT: ...
    @overload
    def normalize(x: _QT, /) -> _QT: ...

    @overload
    def reflect(I: glm_typing.Number, N: glm_typing.Number, /) -> float: ...{''.join(f'''
    @overload
    def reflect(I: glm_typing.F32Vector{i}, N: glm_typing.F32Vector{i}, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def reflect(I: _NF32DFVT, N: _NF32DFVT, /) -> _NF32DFVT: ...

    @overload
    def refract(I: glm_typing.Number, N: glm_typing.Number, eta: float, /) -> float: ...{''.join(f'''
    @overload
    def refract(I: glm_typing.F32Vector{i}, N: glm_typing.F32Vector{i}, eta: float, /) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def refract(I: _NF32DFVT, N: _NF32DFVT, eta: float, /) -> _NF32DFVT: ...
    """)

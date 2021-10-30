
__all__ = ['generate_norm_stub']

import textwrap


def generate_norm_stub():
    names = [
        'distance2',
        'l1Norm', 'l2Norm', 'lMaxNorm',
        'length2',
        'lxNorm',
    ]
    return names, textwrap.dedent(f"""
    {"".join(f'''
    @overload
    def distance2(p0: glm_typing.F32Vector{i}, p1: glm_typing.F32Vector{i}, /) -> float: ...''' for i in range(1, 5))}
    @overload
    def distance2(p0: _NF32DFVT, p1: _NF32DFVT, /) -> float: ...

    @overload
    def l1Norm(v: glm_typing.FDAnyVector3, /) -> float: ...
    @overload
    def l1Norm(x: glm_typing.F32Vector3, y: glm_typing.F32Vector3, /) -> float: ...
    @overload
    def l1Norm(x: _NF32DFV3T, y: _NF32DFV3T, /) -> float: ...

    @overload
    def l2Norm(v: glm_typing.FDAnyVector3, /) -> float: ...
    @overload
    def l2Norm(x: glm_typing.F32Vector3, y: glm_typing.F32Vector3, /) -> float: ...
    @overload
    def l2Norm(x: _NF32DFV3T, y: _NF32DFV3T, /) -> float: ...

    @overload
    def lMaxNorm(v: glm_typing.FDAnyVector3, /) -> float: ...
    @overload
    def lMaxNorm(x: glm_typing.F32Vector3, y: glm_typing.F32Vector3, /) -> float: ...
    @overload
    def lMaxNorm(x: _NF32DFV3T, y: _NF32DFV3T, /) -> float: ...
    {"".join(f'''
    @overload
    def length2(p0: glm_typing.F32Vector{i}, p1: glm_typing.F32Vector{i}, /) -> float: ...''' for i in range(1, 5))}
    @overload
    def length2(p0: _NF32DFVT, p1: _NF32DFVT, /) -> float: ...

    @overload
    def lxNorm(v: glm_typing.FDAnyVector3, /) -> float: ...
    @overload
    def lxNorm(x: glm_typing.F32Vector3, y: glm_typing.F32Vector3, /) -> float: ...
    @overload
    def lxNorm(x: _NF32DFV3T, y: _NF32DFV3T, /) -> float: ...
    """)

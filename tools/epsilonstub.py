
__all__ = ['generate_epsilon_stub']

import textwrap


def generate_epsilon_stub():
    names = [
        'epsilonEqual', 'epsilonNotEqual',
    ]
    return names, textwrap.dedent(f"""
    @overload
    def epsilonEqual(x: glm_typing.Number, y: glm_typing.Number, epsilon: glm_typing.Number, /) -> bool: ...{"".join(f'''
    @overload
    def epsilonEqual(x: glm_typing.F32Vector{i}, y: glm_typing.F32Vector{i}, epsilon: glm_typing.Number, /) -> bvec{i}: ...
    @overload
    def epsilonEqual(x: _NF32DFV{i}T, y: _NF32DFV{i}T, epsilon: glm_typing.Number, /) -> bvec{i}: ...''' for i in range(1, 5))}

    @overload
    def epsilonNotEqual(x: glm_typing.Number, y: glm_typing.Number, epsilon: glm_typing.Number, /) -> bool: ...{"".join(f'''
    @overload
    def epsilonNotEqual(x: glm_typing.F32Vector{i}, y: glm_typing.F32Vector{i}, epsilon: glm_typing.Number, /) -> bvec{i}: ...
    @overload
    def epsilonNotEqual(x: _NF32DFV{i}T, y: _NF32DFV{i}T, epsilon: glm_typing.Number, /) -> bvec{i}: ...''' for i in range(1, 5))}
    """)

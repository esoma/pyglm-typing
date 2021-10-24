
__all__ = ['generate_reciprocal_stub']

import textwrap


def generate_reciprocal_stub():
    names = [
        'acot', 'acoth',
        'acsc', 'acsch',
        'asec', 'asech',
        'cot', 'coth',
        'csc', 'csch',
        'sec', 'sech',
    ]
    return names, textwrap.dedent(f"""
    def acot(x: glm_typing.Number, /) -> float: ...

    def acoth(x: glm_typing.Number, /) -> float: ...

    def acsc(x: glm_typing.Number, /) -> float: ...

    def acsch(x: glm_typing.Number, /) -> float: ...

    def asec(x: glm_typing.Number, /) -> float: ...

    def asech(x: glm_typing.Number, /) -> float: ...

    def cot(x: glm_typing.Number, /) -> float: ...

    def coth(x: glm_typing.Number, /) -> float: ...

    def csc(x: glm_typing.Number, /) -> float: ...

    def csch(x: glm_typing.Number, /) -> float: ...

    def sec(x: glm_typing.Number, /) -> float: ...

    def sech(x: glm_typing.Number, /) -> float: ...
    """)

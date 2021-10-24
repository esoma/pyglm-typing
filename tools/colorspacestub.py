
__all__ = ['generate_color_space_stub']

import textwrap


def generate_color_space_stub():
    names = [
        'convertLinearToSRGB', 'convertSRGBToLinear',
    ]
    return names, textwrap.dedent(f"""
    {"".join(f'''
    @overload
    def convertLinearToSRGB(ColorLinear: glm_typing.F32Vector{i}) -> vec{i}: ...
    @overload
    def convertLinearToSRGB(ColorLinear: glm_typing.F32Vector{i}, Gamma: glm_typing.Number) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def convertLinearToSRGB(ColorLinear: _NF32DFVT) -> _NF32DFVT: ...
    @overload
    def convertLinearToSRGB(ColorLinear: _NF32DFVT, Gamma: glm_typing.Number) -> _NF32DFVT: ...
    {"".join(f'''
    @overload
    def convertSRGBToLinear(ColorLinear: glm_typing.F32Vector{i}) -> vec{i}: ...
    @overload
    def convertSRGBToLinear(ColorLinear: glm_typing.F32Vector{i}, Gamma: glm_typing.Number) -> vec{i}: ...''' for i in range(1, 5))}
    @overload
    def convertSRGBToLinear(ColorLinear: _NF32DFVT) -> _NF32DFVT: ...
    @overload
    def convertSRGBToLinear(ColorLinear: _NF32DFVT, Gamma: glm_typing.Number) -> _NF32DFVT: ...
    """)

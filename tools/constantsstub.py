
__all__ = ['generate_constants_stub']

import textwrap


def generate_constants_stub():
    names = [
        'e', 'epsilon', 'euler', 'four_over_pi', 'golden_ratio', 'half_pi',
        'ln_ln_two', 'ln_ten', 'ln_two', 'one', 'one_over_pi',
        'one_over_root_two', 'pi', 'quater_pi', 'root_five', 'root_half_pi',
        'root_ln_four', 'root_pi', 'root_three', 'root_two', 'root_two_pi',
        'third', 'three_over_two_pi', 'two_over_pi', 'two_over_root_pi',
        'two_pi', 'two_thirds', 'zero',
    ]
    return names, textwrap.dedent(f"""
    def e() -> float: ...

    def epsilon() -> float: ...

    def euler() -> float: ...

    def four_over_pi() -> float: ...

    def golden_ratio() -> float: ...

    def half_pi() -> float: ...

    def ln_ln_two() -> float: ...

    def ln_ten() -> float: ...

    def ln_two() -> float: ...

    def one() -> float: ...

    def one_over_pi() -> float: ...

    def one_over_root_two() -> float: ...

    def one_over_two_pi() -> float: ...

    def pi() -> float: ...

    def quarter_pi() -> float: ...

    def root_five() -> float: ...

    def root_half_pi() -> float: ...

    def root_ln_four() -> float: ...

    def root_pi() -> float: ...

    def root_three() -> float: ...

    def root_two() -> float: ...

    def root_two_pi() -> float: ...

    def third() -> float: ...

    def three_over_two_pi() -> float: ...

    def two_over_pi() -> float: ...

    def two_over_root_pi() -> float: ...

    def two_pi() -> float: ...

    def two_thirds() -> float: ...

    def zero() -> float: ...
    """)
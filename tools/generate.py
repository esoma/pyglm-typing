
from arraystub import generate_array_stub
from colorspacestub import generate_color_space_stub
from constantsstub import generate_constants_stub
from ctypesstub import generate_ctypes_stub
from epsilonstub import generate_epsilon_stub
from funccommonstub import generate_func_common_stub
from funcexponentialstub import generate_func_exponential_stub
from funcgeometricstub import generate_func_geometric_stub
from funcintegerstub import generate_func_integer_stub
from funcmatrixstub import generate_func_matrix_stub
from funcpackingstub import generate_func_packing_stub
from functrigonometricstub import generate_func_trigonometric_stub
from funcvectorrelationalstub import generate_func_vector_relational_stub
from integerstub import generate_integer_stub
from matrixaccessstub import generate_matrix_access_stub
from matrixinversestub import generate_matrix_inverse_stub
from matrixtype import get_matrix_types
from matstub import (generate_mat_stub, generate_mat_typevars,
                     generate_mat_unions)
from noisestub import generate_noise_stub
from otherstub import generate_other_stub
from packingstub import generate_packing_stub
from quaternionstub import generate_quaternion_stub
from quaterniontype import get_quaternion_types
from quatstub import (generate_quat_stub, generate_quat_typevars,
                      generate_quat_unions)
from stub import union
from vecstub import (generate_vec_stub, generate_vec_typevars,
                     generate_vec_unions)
from vectortype import get_vector_types

header = """
# generated by tools/generate.py
# https://github.com/esoma/pyglm_typing/

"""

with open('src/glm-stubs/__init__.pyi', 'w') as f:
    names = []

    def add_stub(stub_func, *stub_args):
        global names
        stub_names, stub = stub_func(*stub_args)
        names += stub_names
        f.write(stub)
        f.write('\n')

    f.write(header)
    f.write('import ctypes\n')
    f.write('from typing import Any, Callable, Generator, Generic, Iterable, List, Literal, Optional, overload, SupportsInt, Tuple, Type, TypeVar, Union\n')
    f.write('import glm_typing\n')
    f.write('\n')

    f.write('_T = TypeVar(\'_T\')\n')
    f.write(generate_vec_typevars())
    f.write(generate_mat_typevars())
    f.write(generate_quat_typevars())
    f.write('\n')

    add_stub(generate_ctypes_stub)
    for name in get_vector_types():
        add_stub(generate_vec_stub, name)
    for name in get_matrix_types():
        add_stub(generate_mat_stub, name)
    for name in get_quaternion_types():
        add_stub(generate_quat_stub, name)
    add_stub(generate_array_stub)
    add_stub(generate_func_common_stub)
    add_stub(generate_func_exponential_stub)
    add_stub(generate_func_geometric_stub)
    add_stub(generate_func_integer_stub)
    add_stub(generate_func_matrix_stub)
    add_stub(generate_func_packing_stub)
    add_stub(generate_func_trigonometric_stub)
    add_stub(generate_func_vector_relational_stub)
    add_stub(generate_other_stub)
    add_stub(generate_color_space_stub)
    add_stub(generate_constants_stub)
    add_stub(generate_epsilon_stub)
    add_stub(generate_integer_stub)
    add_stub(generate_matrix_access_stub)
    add_stub(generate_matrix_inverse_stub)
    add_stub(generate_noise_stub)
    add_stub(generate_packing_stub)
    add_stub(generate_quaternion_stub)

    f.write(f'__all__ = {sorted(set(names))!r}\n')


with open('src/glm_typing/__init__.py', 'w') as f:
    names = []

    f.write(header)
    f.write('from typing import SupportsFloat, SupportsInt, Tuple, Union\n')
    f.write('import glm\n')
    f.write('Number = Union[SupportsFloat, SupportsInt]\n')

    for union_name, union_stub in (
        *generate_vec_unions(),
        *generate_mat_unions(),
        *generate_quat_unions(),
        ('FDAnyQuaternionVector4', f'''FDAnyQuaternionVector4 = {union(['FDAnyVector4', 'FDAnyQuaternion'])}''')
    ):
        names.append(union_name)
        f.write(union_stub)
        f.write('\n')

    f.write(f'__all__ = {names!r}\n')

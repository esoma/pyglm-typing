

from arraystub import generate_array_stub
from ctypesstub import generate_ctypes_stub
from funccommonstub import generate_func_common_stub
from funcexponentialstub import generate_func_exponential_stub
from funcgeometricstub import generate_func_geometric_stub
from funcintegerstub import generate_func_integer_stub
from funcmatrixstub import generate_func_matrix_stub
from funcpackingstub import generate_func_packing_stub
from functrigonometricstub import generate_func_trigonometric_stub
from funcvectorrelationalstub import generate_func_vector_relational_stub
from matrixstub import (generate_matrix_stub, generate_matrix_typevars,
                        generate_matrix_unions)
from matrixtype import get_matrix_types
from quaternionstub import (generate_quaternion_stub,
                            generate_quaternion_typevars,
                            generate_quaternion_unions)
from quaterniontype import get_quaternion_types
from stub import union
from vectorstub import (generate_vector_stub, generate_vector_typevars,
                        generate_vector_unions)
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
    f.write(generate_vector_typevars())
    f.write(generate_matrix_typevars())
    f.write(generate_quaternion_typevars())
    f.write('\n')

    add_stub(generate_ctypes_stub)
    for name in get_vector_types():
        add_stub(generate_vector_stub, name)
    for name in get_matrix_types():
        add_stub(generate_matrix_stub, name)
    for name in get_quaternion_types():
        add_stub(generate_quaternion_stub, name)
    add_stub(generate_array_stub)
    add_stub(generate_func_common_stub)
    add_stub(generate_func_exponential_stub)
    add_stub(generate_func_geometric_stub)
    add_stub(generate_func_integer_stub)
    add_stub(generate_func_matrix_stub)
    add_stub(generate_func_packing_stub)
    add_stub(generate_func_trigonometric_stub)
    add_stub(generate_func_vector_relational_stub)

    f.write(f'__all__ = {sorted(set(names))!r}\n')


with open('src/glm_typing/__init__.py', 'w') as f:
    names = []

    f.write(header)
    f.write('from typing import SupportsFloat, SupportsInt, Tuple, Union\n')
    f.write('import glm\n')
    f.write('Number = Union[SupportsFloat, SupportsInt]\n')

    for union_name, union_stub in (
        *generate_vector_unions(),
        *generate_matrix_unions(),
        *generate_quaternion_unions(),
        ('FDAnyQuaternionVector4', f'''FDAnyQuaternionVector4 = {union(['FDAnyVector4', 'FDAnyQuaternion'])}''')
    ):
        names.append(union_name)
        f.write(union_stub)
        f.write('\n')

    f.write(f'__all__ = {names!r}\n')

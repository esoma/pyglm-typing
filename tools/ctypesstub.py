
__all__ = ['generate_ctypes_stub']

import ctypes

import glm

_CTYPES_ALIASES = {}
for name in dir(glm):
    alias_obj = getattr(glm, name)
    if not hasattr(alias_obj, "__name__"):
        continue
    if alias_obj.__name__ == name:
        continue
    if alias_obj.__name__ not in dir(ctypes):
        continue
    actual_name = f'ctypes.{alias_obj.__name__}'
    try:
        aliases = _CTYPES_ALIASES[actual_name]
    except KeyError:
        aliases = _CTYPES_ALIASES[actual_name] = []
    aliases.append(name)


def generate_ctypes_stub():
    all_aliases = []
    stubs = []
    for ctype, aliases in _CTYPES_ALIASES.items():
        all_aliases += aliases
        for alias in aliases:
            stubs.append(f'{alias} = {ctype}')
    return all_aliases, '\n'.join(stubs)

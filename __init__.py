from platform import python_version_tuple
from os import name

PYVER = python_version_tuple()

if PYVER[:2] != ('3', '10'):
    raise DeprecationWarning(f"It seems that your python version is lower than the minimum required (3.10.X) to run the game (Your version: {''.join(PYVER)}).")
if name != "nt":
    raise Warning(f"[Aviso]: Puede que algunas cosas no se ejecuten bien debido a la falta de compatibilidad completa con sistemas UNIX. Your system: {name}")

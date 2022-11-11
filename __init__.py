from sys import version_info
from os import name

if version_info < (3, 11):
    raise DeprecationWarning(f"It seems that your python version is lower than the minimum required (3.10.X) to run the game")
if name != "nt":
    raise Warning(f"[WARNING]: Some things may not run well due to lack of full compatibility with UNIX systems. Your system: {name}")

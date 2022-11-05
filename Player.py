"""
Player base class, this class inherits object base class.

For more detailed info about the class open a terminal al type 'python -i Player.py or <file-path>'
- This will open python interpreter in interactive mode, then, to know more details type >>> help(Player)

NOTE: This class can be subclassed,
and may u want to do this to make other player object neither with special methods nor overriding any Player method.
"""
from langs import Langs
from utils import *

from datetime import datetime
from typing import MutableMapping, Generator

from colorama import Fore as _Fore
from pybeaut import Col as _Col


__all__ = ["Player"]


class Player(object):
    """Main player class with cache implementation."""
    # __slots__ = ("token", "name", "color", "cache")

    def __init__(
        self,
        token: str,
        name: str = "Player",
        color: str | _Col = _Col.white,
        country: str = None,        #? un poco porro, valorar.
        custom_doc: str = None
        
    ):

        if not multiple_instcheck((name, token), str):
            #! Hacer que el multiple_inscheck devuelva, en caso de strict=True, el valor que no cumple.
            raise TypeError(f"{multiple_instcheck((name, token), str, True)} param must be a string, not {repr(multiple_instcheck((name, token), str, True))}")

        self._name:    str   = name     #! Si no es establece un nombre, el default es player, que despues en el constructor se cambia por 'Player{}'
        self._token:   str   = token
        self._color:   str   = color
        self.cache:  dict | MutableMapping = self._init_cache()
        
        if custom_doc is not None:
            assert isinstance(custom_doc, str)
            __custom_doc__ = custom_doc

    @property
    def name(self) -> str:
        "Return the name of the player in a read-only view ``(property)``"
        return self.name
    @property
    def color(self) -> _Col | str:
        "Return the color of the player in a read-only view ``(property)``"
        return self._color
    @property
    def token(self) -> str:
        "Return the token of the player in a read-only view ``(property)``"
        return self.token
    @property
    def cache_keys(self) -> list:
        "Return a list with the cache keys``(property)``"
        return list(self.cache.keys())
    @property
    def cache_size(self) -> int | float:
        "Return the size of the cache in bytes.``(property)``"
        return self.cache.__hash__()
    @property 
    def view_movements(self) -> list:
        "Return a read-only view of cached list movements ``(property)``"
        return self.cache["movements"]

    @staticmethod
    def subclasses() -> list:
        "Lazy method to show all subclasses of this class"
        return Player.__subclasses__()

    def _clear_cache(self) -> None:
        "Reload the player cache, makes a new cache."
        self.cache = self._init_cache()

    def _init_cache(self) -> dict[str,]:
        "Initialize the player cache with an static mutabledict"
        return {
            "name": self._name,
            "token": self._token.strip().upper(),
            "color": self._color,
            "movements": [],    #? Aqui solo se guarda la posicion del movimiento.
            "timings": [],
            "best_timing": None,
            "worst_timing": None
        }

    def __format__(self, __format_spec: str) -> str:
        """Special overrided method (to object superclass) to format a instance of a player when we print the instance.
        This method is a ``__str__`` method but it's decorated with a format (__str__+.uppercase())
        
       - Example:
    
        >>> p = Player("Alvaro", "X")
        >>> # we want to print the name in uppercase
        >>> print(f"{p:upper}")
        >>> # we want to print the token in green
        >>> print(f"{p:tkngreen})
        """
        
        fmts = dict.fromkeys([c for c in _Col.static_colors].extend(["upper", "lower", "capitalize", "name"]), ...)

        if not __format_spec in fmts:
            raise TypeError("That format is not valid")

        # super().__format__(__format_spec)
        ...


    def addmov(self, pos: tuple[int, int], time: float | int) -> None:
        "Add in a fast method one movement and it's time in the cache"
        self.cache["movements"].append(pos)
        self.cache["timings"].append(time)
    
    def take_turn(self, lang) -> list[float | tuple[str, str]]:
        #! LEE EL DOC DE ESTA FUNCION
        """
        Method to generate a turn to the player.
        
        - This method does not check if the values are correct, only for the time of the move and the coordinates returned in str
        for the constructor method to check.

        NOTE: ``You may want to overwrite this method in your subclass to adapt it to the needs of the subclass but it MUST ALWAYS RETURN THE SAME VALUE.``
        """
        t = datetime.now()
        posx = input(f"{self.color}[{self.name}]{_Fore.RESET}: {_Fore.LIGHTWHITE_EX}{Langs.get_phrase(lang, 'game', 3).format('X')} -> {_Fore.RESET}") 
        #Coloca la coordenada {} (X o Y)
        posy = input(f"{self.color}[{self.name}]{_Fore.RESET}: {_Fore.LIGHTWHITE_EX}{Langs.get_phrase(lang, 'game', 3).format('Y')} -> {_Fore.RESET}") 
        t = round((datetime.now()-t).total_seconds(), 2)

        return [t, (posx, posy)]

    def cache_gen(self, key: lambda x: x = None):
        "Useless lazy method that yields the cache and returns and iterator."
        if key is not None: 
            yield from self.cache[key]
        yield from self.cache.items()


if __name__ == "__main__":
    t = Player("Alvarotest")
    # print(t.__weakref__())
    print(t.__dir__())
    print(t.__sizeof__())
    print(t.__doc__)
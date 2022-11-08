"""Main bot module"""

#BoardToe imports
from Player import Player
import core

#__init__ imports
from constants import * 
from typing import MutableMapping
from pybeaut import Col as _Col

#Misc imports
from random import randint 
from datetime import datetime
from colorama import Fore as _Fore



class Bot(Player):
    """
    Class instantiated on game start as a player,
    each turn the turn() function should be called to get the move that this bot wants to make.
    """
    __fmts: dict = _Col.static_cols_mapping

    def __init__(
        self, 
        token: str,
        name: str = "CPU",
        color: str | _Col = _Col.white,
        difficulty: str = "Easy",
        custom_doc: str = None
    ):
        if not isinstance(name, str):
            raise TypeError(f"@name param must be a string, not {name!r} of type {type(name).__name__}")
        elif not isinstance(token, str):
            raise TypeError(f"@token param must be a string, not {token!r} of type {type(token).__name__}")
        elif not token in TOKENS:
            raise TypeError(f"@token param is a invalid token. Valid tokens: '⭕' or '❌'")
        elif not color in self.__fmts:
            raise TypeError(f"@color param must be a valid color. Valid colors: {self.__fmts.keys()}")
        elif not difficulty in ["Easy", "Normal", "Hard", "Imposible"]:
            raise TypeError(f"@difficulty param must be a valid difficulty. Valid difficulties: 'Easy', 'Normal', 'Hard', 'Imposible'")
        
        self._token: str = token
        self._name: str = name     #* default 'CPU'
        self._color: str = self.__fmts[color]
        self._difficulty: str = difficulty
        self.cache: dict | MutableMapping = self._init_cache()
        self.__custom_doc__ = custom_doc if custom_doc and isinstance(custom_doc, str) else None

    def is_bot(self) -> bool:
        return True

    def _init_cache(self) -> dict[str]:
        """
        Initialize the player cache with an static dictionary.
        - NOTE: You may want to override this method to get a different cache implementation
        """
        return {
            "name": self._name,
            "token": self._token.strip(),
            "color": self._color,
            "movements": [],    #? Aqui solo se guarda la posicion del movimiento.
            "timings": [],
            "best_timing": None,
            "worst_timing": None,
            "predicted_moves": [] #? Solo el bot
        }   

    def turn(self, matrix: list[list[int]], lang: str) -> list[float | tuple[int]]:
        t = datetime.now()
        moves: list[list[int]] | None = self.__filter_moves(core.win_check(matrix, self.betoken), core.win_check(matrix, self.btoken), len(matrix))
        t = (datetime.now()-t).microseconds
        if moves:
            moves = self.__max(moves)
        else:
            print("EMPATE")

        x = moves[randint(0 , len(moves)-1)]
        print(f"{self.color}[{self.name}]{_Fore.RESET}: {_Fore.LIGHTWHITE_EX}Placed a token on {_Fore.LIGHTCYAN_EX}{(x[0]+1, x[1]+1)}{_Fore.LIGHTWHITE_EX} -> {_Fore.LIGHTYELLOW_EX}{t}μs{_Fore.RESET}")
        return [t, (x[0]+1, x[1]+1)]

    def __filter_moves(self, pmoves: list[tuple[int, list[list[int]]]], bmoves: list[tuple[int, list[list[int]]]], d: int) -> list[list[int]] | None:
        r: list = []
        for moves in [pmoves, bmoves]:
            moves = [v for v in moves if v]
            if moves:
                rr: list = [moves[0][0], moves[0][1]]
                for v in moves[1:]:
                    if v:
                        rr[1] = [_ for _ in v[1]] if rr[0] > v[0] else [_ for _ in rr[1]] + [_ for _ in v[1]] if rr[0] == v[0] else rr[1]
                        rr[0] = v[0] if rr[0] > v[0] else rr[0]
                r.append(rr)
        return None if not r else r[0][1] if len(r) == 1 else r[1][1] if r[1][0] < r[0][0] or r[0][0] >= self.__get_difficulty(d) and randint(0, 100) % randint(1, 2) else r[0][1]

    def __get_difficulty(self, d: int) -> int:
        if self._difficulty == "Easy":
            return 1
        elif self._difficulty == "Normal":
            return d - (d // 2)
        elif self._difficulty == "Hard":
            return d - 1
        return d
        
    def __max(self, values: list[list[int]]) -> list[list[int]] | list[int]:
        values = [tuple(_) for _ in values]
        r: list = [0, []]
        for v in set(values):
            c: int = values.count(v)
            print("C", c > r[0])
            r[1] = [v] if c > r[0] else r[1] + [v] if c == r[0] else r[1]
            r[0] = c if c > r[0] else r[0]
        return r[1]

    """
    Razonamiento logico del botico:

    Movimiento debe ser procesado de la siguiente manera: cada tipo de movimiento tendra un numero y un jugador asignado, se ejecutara el movimiento con el valor mas alto:
    0: Random move
    1: Random move en casilla adyacente a alguna del bot
    2: Cortar jugada gandora rival
    3: Ejecutar jugada gandora del bot
    Este es el metodo simple, para mayor complejidad:
    0: Random move teniendo en cuenta la mayor cantidad de casillas vacias adyacentes
    1: Random move en casilla adyacente a alguna del bot teniendo en cuenta si bloquea jugadas posteriores enemigas
    2: Cortar jugada gandora rival
    3: Ejecutar jugada gandora del bot
    Y para la mayor complejidad:
    0: Random move teniendo en cuenta la mayor cantidad de casillas vacias adyacentes
    1: Random move en casilla adyacente a alguna del bot teniendo en cuenta si bloquea jugadas posteriores enemigas y si se crea una doble posiblidad de nivel tres lo que asegura una victoria absoulta
    2: Cortar jugada gandora rival
    3: Ejecutar jugada gandora del bot


    Los posibles movimientos se conseguiran a traves de una funcion que calculara parte y delegara otra al archivo core

    Posible implementacion del cache de botico, con improbable analisis de toma de decisiones (Muy complejo)
    """
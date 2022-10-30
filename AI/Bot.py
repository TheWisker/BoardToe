from constructor import *
from random import randint

import AI.core as core

#Class intantiated on game start as a player, accepts a parameter the bot player number, and the enemy player number, each turn the get_move function should be called to get the move that this bot plays
class Bot:

    def __init__(self, players: tuple[int, int], difficulty: str = "Easy") -> None:
        self.bot = players[0]
        self.plr = players[1]
        ...
        

    def _get_cases(board: list[list[int]], player: int) -> list[tuple[int, int]]:
        results: bool | list[tuple[int, tuple[int, int]]] = core.check_matrix(board)
        cases: list[tuple[int, int]] = []
        if results is not bool:
            for case in results:
                if case[0] == player:
                    cases.append(case[1]) 
        return cases

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
    
    def get_move(self, board) -> tuple[int, int]:
        bot_cases: list[tuple[int, int]] = self._get_cases(board, self.bot)
        plr_cases: list[tuple[int, int]] = self._get_cases(board, self.plr)
        if bot_cases:
            return bot_cases[randint(0, len(bot_cases))]
        elif plr_cases:
            return plr_cases[randint(0, len(plr_cases))]
        else:

            ...





        #randint(..., ...)
        #vi = _enemy_cases(board)
        #vi = _enemy_cases(board)
        return (2,2)

 
    #def restart(): #restart the bot but could not be necesary if we just delete and create a new instance
     #   ...


    # def _get_value(): #get value for a case scenario
    #     ...
    # def _maximin():
    #     ...s
    # def _minimax():
    #     ...

    # def _add_cache(): #add cache to better process the current match and options
    #     ...
    


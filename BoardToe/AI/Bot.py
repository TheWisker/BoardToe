from random import randint
import sys
 
# setting path
sys.path.append('../BoardToe')
from BoardToe.Player import Player
import core as core

class Bot(Player):
    """
    Class intantiated on game start as a player, 
    accepts a parameter the bot player number, and the enemy player number, 
    each turn the get_move function should be called to get the move that this bot plays.
    """

    def __init__(self, players: tuple[int, int], difficulty: str = "Easy") -> None:
        self.bot = players[0]
        self.plr = players[1]

        ...

    #! IMPORTANTE: 0 es False y 1 es True (comprobado)
    def turn(matrix: list[list[int]], player: int, lang: str):
        matrix = core.transform2matrix(matrix)

        pmoves: list[tuple[int, tuple[int, int]]] = core.adjacent_check(matrix, 0 if player else 1)
        bmoves: list[tuple[int, tuple[int, int]]] = core.adjacent_check(matrix, player)
        pmove: tuple[int, tuple[int, int]] = ...
        bmove: tuple[int, tuple[int, int]] = ...
        

        ...
        # super().take_turn() to access to the base class method

    def _filter_moves(moves: list[tuple[int, tuple[int, int]]]) -> list[int, tuple[int, int]] | list[int, list[tuple[int, int]]]:   #! TYPE HINTS

        r: list = [moves[0][0], moves[0]]
        for v in moves[1:]:
            r[1] = [v[1]] if r[0] > v[0][0] else r[1] + [v[1]] if r[0] == v[0][0] else r[1]
            r[0] = v[0][0] if r[0] > v[0][0] else r[0]
        return r
        

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
    models: dict[str, str] = {
        6: [
            [4, 1, 0],
            [0, -1, 1],
            [1, 0, 2],
        ],
        7: [
            [5, 1, 0],
            [0, 2, 1],
            [1, 0, 2],
        ],
        8: [
            [4, 1, 0],
            [0, 2, 1],
            [1, 0, 2],
        ],
        9: [
            [4, 1, 0],
            [0, 2, 1],
            [1, 0, 2],
        ]
    } 
    print(_filter_moves(models[6], 1))
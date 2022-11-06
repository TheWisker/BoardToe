from random import randint
from Player import Player
import core as core


class Bot(Player):
    """
    Class intantiated on game start as a player, 
    accepts a parameter the bot player number, and the enemy player number, 
    each turn the get_move function should be called to get the move that this bot plays.
    """

    def __init__(self, players: tuple[int, int] = (0,1), difficulty: str = "Easy") -> None:
        self.bot = players[0]
        self.plr = players[1]

        ...

    def filter_moves(self, pmoves: list[tuple[int, list[list[int]]]], bmoves: list[tuple[int, list[list[int]]]]) -> list[list[int]]:   #! TYPE HINTS
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
        return r[0][1] if len(r) == 1 else r[1][1] if r[1][0] <= r[0][0] else r[0][1]
            
        """ PROBLEM WITH set() unhashable type: 'list'
        if len(set(str(r[1]))) < len(r[1]):
            t: list = [r[1].count(r[1][0]), r[1][0]]
            for v in r[1][1:]:
                t[1] = v if r[1].count(v) > t[0] else t[1]
                t[0] = r[1].count(v) if r[1].count(v) > t[0] else t[0]
        """


    #! IMPORTANTE: 0 es False y 1 es True (comprobado)
    def turn(self, matrix: list[list[int]], player: int, lang: str):
        matrix = core.transform2matrix(matrix)
        moves: list[list[int, int]] = self.filter_moves(core.adjacent_check(matrix, 0 if player else 1), core.adjacent_check(matrix, player))
        return moves[randint(0 , len(moves)-1)]
        # super().take_turn() to access to the base class method


    

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
        [0, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
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
print(Bot().turn(models[6], 0, ""))
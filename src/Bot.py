from random import randint
from Player import Player
import core as core
from datetime import datetime


class Bot(Player):
    """
    Class intantiated on game start as a player, 
    accepts a parameter the bot player number, and the enemy player number, 
    each turn the get_move function should be called to get the move that this bot plays.
    """

    def __init__(self, token):
        self._token = token
        self._name = "CPU"
        self._color = None
        self.cache: dict = self._init_cache()
        self.__custom_doc__ =  None


    def filter_moves(self, pmoves: list[tuple[int, list[list[int]]]], bmoves: list[tuple[int, list[list[int]]]]) -> list[list[int]]:
        r: list = []

        if not pmoves:
            print("Player l")
        elif not bmoves:
            print("Bot l")


        for moves in [pmoves, bmoves]:
            moves = [v for v in moves if v]
            if moves:
                rr: list = [moves[0][0], moves[0][1]]
                for v in moves[1:]:
                    if v:
                        rr[1] = [_ for _ in v[1]] if rr[0] > v[0] else [_ for _ in rr[1]] + [_ for _ in v[1]] if rr[0] == v[0] else rr[1]
                        rr[0] = v[0] if rr[0] > v[0] else rr[0]
                r.append(rr)

        if r:
            return r[0][1] if len(r) == 1 else r[1][1] if r[1][0] <= r[0][0] else r[0][1]
        else:
            input("EMPATE")

    """
    Traceback (most recent call last):
    File "/home/kopi/GitHub/BoardToe/src/main.py", line 44, in <module>
        test.init_game()
    File "/home/kopi/GitHub/BoardToe/src/constructor.py", line 327, in init_game
        posx, posy = self.handle_turn()
    File "/home/kopi/GitHub/BoardToe/src/constructor.py", line 157, in handle_turn
        turn_time, postuple = self.actual_turn.turn(self.board, self.actual_turn.btoken, self.game_lang)   
    File "/home/kopi/GitHub/BoardToe/src/Bot.py", line 51, in turn
        moves: list[list[int, int]] = self.filter_moves(core.adjacent_check(matrix, 0 if player else 1), core.adjacent_check(matrix, player))
    File "/home/kopi/GitHub/BoardToe/src/Bot.py", line 43, in filter_moves
        return r[0][1] if len(r) == 1 else r[1][1] if r[1][0] <= r[0][0] else r[0][1]
    IndexError: list index out of range
    """
    def is_bot(self) -> bool:
        return True

    #! IMPORTANTE: 0 es False y 1 es True (comprobado)
    def turn(self, matrix: list[list[int]], player: int, lang: str):
        self.logic_time = datetime.now()
        moves: list[list[int, int]] = self.filter_moves(core.adjacent_check(matrix, 0 if player else 1), core.adjacent_check(matrix, player))
        self.logic_time = round((datetime.now()-self.logic_time).total_seconds(), 2)
        print(player, 0 if player else 1)
        print("X",core.adjacent_check(matrix, player))
        print("Y",core.adjacent_check(matrix, 0 if player else 1))
        print("Z",moves)
        moves = [max(set([tuple(m) for m in moves]), key = [tuple(m) for m in moves].count)]
        print("A",moves)
        [(3, [[0, 0], [0, 1], [0, 2]]), (3, [[1, 0], [1, 1], [1, 2]]), (3, [[2, 0], [2, 1], [2, 2]]), (3, [[2, 0], [1, 0], [0, 0]]), (3, [[2, 1], [1, 1], [0, 1]]), (3, [[2, 2], [1, 2], [0, 2]]), (3, [[0, 0], [1, 1], [2, 2]]), (3, [[0, 2], [1, 1], [2, 0]])]
        [(3, [[0, 0], [0, 1], [0, 2]]), (3, [[1, 0], [1, 1], [1, 2]]), (3, [[2, 0], [2, 1], [2, 2]]), (3, [[2, 0], [1, 0], [0, 0]]), (3, [[2, 1], [1, 1], [0, 1]]), (3, [[2, 2], [1, 2], [0, 2]]), (3, [[0, 0], [1, 1], [2, 2]]), (3, [[0, 2], [1, 1], [2, 0]])]
        [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [2, 0], [1, 0], [0, 0], [2, 1], [1, 1], [0, 1], [2, 2], [1, 2], [0, 2], [0, 0], [1, 1], [2, 2], [0, 2], [1, 1], [2, 0]]
        (1, 1)

        [(3, [[0, 0], [0, 1], [0, 2]]), (3, [[2, 0], [1, 0], [0, 0]]), (1, [[0, 1]]), (2, [[0, 0], [2, 2]]), None]

        [(3, [[0, 0], [0, 1], [0, 2]]), (1, [[2, 2]]), (3, [[2, 2], [1, 2], [0, 2]]), None, None]
        [[1, 0]]
        [(1, 0)]

        [(3, [[0, 0], [0, 1], [0, 2]]), (3, [[2, 0], [2, 1], [2, 2]]), (3, [[2, 0], [1, 0], [0, 0]]), (3, [[2, 2], [1, 2], [0, 2]]), None, None]
        [(3, [[0, 0], [0, 1], [0, 2]]), (2, [[1, 0], [1, 2]]), (3, [[2, 0], [2, 1], [2, 2]]), (3, [[2, 0], [1, 0], [0, 0]]), (2, [[2, 1], [0, 1]]), (3, [[2, 2], [1, 2], [0, 2]]), (2, [[0, 0], [2, 2]]), (2, [[0, 2], [2, 0]])]
        [[1, 0], [1, 2], [2, 1], [0, 1], [0, 0], [2, 2], [0, 2], [2, 0]]
        [(0, 1)]


        [(2, [[2, 0], [2, 1]]), None, None, None]
        [(1, [[0, 1]]), (1, [[1, 0]]), None, (1, [[2, 0]])]
        [[0, 1], [1, 0], [2, 0]]
        [(0, 1)]

        [(3, [[2, 0], [2, 1], [2, 2]]), (3, [[2, 2], [1, 2], [0, 2]]), None, None]
        [(2, [[1, 0], [1, 2]]), (3, [[2, 0], [2, 1], [2, 2]]), (2, [[2, 0], [1, 0]]), (3, [[2, 2], [1, 2], [0, 2]]), (1, [[2, 2]]), (2, [[0, 2], [2, 0]])]
        [[2, 2]]
        [(2, 2)]


        #BOT PRIORICES FUCKING PLAYER THAN HELPIN HIMSELF SOMETIMES


        x = moves[randint(0 , len(moves)-1)]
        return [self.logic_time, (x[0]+1, x[1]+1)]
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
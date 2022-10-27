from constructor import *
from random import randint

import AI.core as core


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
    


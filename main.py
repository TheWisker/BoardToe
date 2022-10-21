from utils import *

from random import choice, randint
from time import time, sleep
from datetime import datetime
from collections import namedtuple

from colorama import Fore
import pystyle as pys



class BoardGame:

    def __init__(self, _rows: int, _columns: int, tokenplayer1: str, tokenplayer2: str, player: str = "player1", player2: str = "player2"):
        
        if not multiple_instcheck((_rows, _columns), int):
            raise TypeError("Rows and columns must be a numerical parameters")
        
        elif _rows != _columns or _rows * _columns > 64:   #8x8 = 64 -> Max board size
            raise ValueError("The number of rows and columns must be equals to make an equitative boardgame or must be under 8 (Max table size of 8x8)")
        
        elif not multiple_instcheck((player, player2), str):
            raise ValueError("Player attribute must be a string saying the name of the player")
        elif not multiple_instcheck((tokenplayer1, tokenplayer2), str) or tokenplayer1 == tokenplayer2:
            raise TypeError("Token player must be X or O and each player must define a different token")

        self.rows = _rows
        self.columns = _columns

        self.player1 = self._make_player_cache(player, tokenplayer1)
        self.player2 = self._make_player_cache(player2, tokenplayer2)
        
        self.board = self._make_board()
        self.partycounter = 0
        self._party_cache = {"board_size": (_rows, _columns), "players": (self.player1, self.player2), "party": []}
        self._movtuple = namedtuple("Movement", ["token", "player", "position"]) #, "moviment_time"


    def _make_player_cache(self, player, token):
        _cache = {
            "name": player,
            "token": token.strip().upper(),
            "movements": [],
            "timings": [],
        }
        return _cache


    def _pprint(self, table) -> None:
        "Prints the table in a pretty way (without colons and token-colored)"
        for column in table:
            print(multiple_replace(f"\t{column}", 
                    (
                        ("'", ""), 
                        (",", " "), 
                        ("[", "| "),
                        ("]", " |"),
                        ("0", f"{Fore.LIGHTWHITE_EX}0{Fore.RESET}"), 
                        ("X", f"{Fore.LIGHTRED_EX}X{Fore.RESET}")
                    )
                )
            )

    def _make_board(self) -> list:
        "Private method to make a empty board"
        master_table = []
        
        for _ in range(0, self.columns):
            master_table.append([])
        
        for c in master_table:
            for _ in range(0, self.rows):
                    c.append("-")

        return master_table

    def turn(self):
        "Fuction to manage the turns"
        ...

    def draw_board(self, table, pos: tuple[int, int], player):
        """# Importante:
            @param ``pos`` es una tupla que describe las coordenadas ``X`` e ``Y``, el orden es sumamente importante.\n
            Las coordenadas deben estar entre ``[1, board_columns]`` para ``x`` e ``[1, board_rows]`` para ``y``
        """
        posx, posy = pos[0]-1, pos[1]-1
        
        if not (0 <= posx <= self.columns) or not (0 <= posy <= self.rows):
            return False  

        if table[posx][posy] != "-":
            #? la posicion ya esta cogida, evitamos que tenga que comprobar de que tipo es.
            return False
        elif table[posx][posy] == player["token"]:
            #? la posicion esta ocupada por una ficha del mismo tipo
            return True
        else:
            #? coloca la ficha
            table[posx][posy] = player["token"]
            #? Guarda el movimiento del jugador en su cache.
            player["movements"].append(pos)
            self._party_cache["party"].append(self._movtuple(player["token"], player["name"], pos))


    def checkWin(self) -> tuple[bool, str | None]:
        #? Devuelve un booleano para comprobar rapidamente si alguien ha ganado, y el jugador

        # vertical
        #! hacerla para que funcione con n subarrays, no solo checkee para tres indices.
        # for i,elem in enumerate(self.board):
        #     for _ in range(0, len(elem)[i]):
        #         if elem[i] == elem[i-_][i] and elem[i] != '':
        #             print("Has ganado! Gana el jugador de las fichas %s" % elem[i].upper())

        # horizontal
        # lo que hace es ver si todos los elementos de la lista son iguales al primero (conveniencia)
        for subarrays in self.board:
            if all(elem == subarrays[0] for elem in subarrays if elem != ''):
                print(f"\nHas ganado! Gana {self._party_cache['party'][-1][1]}")
            
        # diagonal
        return


    def init_game(self):
        "Game loop flow, unless you cancel the game or one player win, the game will be cancelled"
        self.timecounter = datetime.now()

        def calc_passed_time_format():
            "Main loop timer, this function needs to be refreshed every time."
            passed_seconds = (datetime.now() - self.timecounter).total_seconds()
            
            hours = int(passed_seconds / 60 / 60)
            passed_seconds -= hours*60*60
            minutes = int(passed_seconds/60)
            passed_seconds -= minutes*60
            return f"{hours:02d}:{minutes:02d}:{passed_seconds:02d}"
        
        cls()
        while True:
            ...
            

# TESTS  
      
test = BoardGame(3,3, "0", "X") 

movements = [
    (test.player2, (1, 1)),
    (test.player2, (2, 3)),
    (test.player1,(3,2)),
    (test.player1, (2,1)),
    (test.player1, (3,1)),
    (test.player1, (3,3))
]
for mov in movements:
    test.draw_board(test.board, mov[1], player = mov[0]) #board, pos (tuple x,y) and player (to know the player name (if it has one) and her token)
test._pprint(test.board)
test.checkWin()

print(f"\n{Fore.LIGHTGREEN_EX}DEBUGGING INFO:{Fore.RESET}\n")
print(f"Party cache: {test._party_cache}\n")
print(f"Player1 cache: {test.player1}\n")
print(f"Player2 cache: {test.player2}\n")


    
        





    

    
from utils import *

from random import choice, randint
from time import time, sleep
from datetime import datetime
from collections import namedtuple

from colorama import Fore



class BoardGame:

    def __init__(self, _rows: int, _columns: int, tokenplayer1: str, tokenplayer2: str, player: str = "player1", player2: str = "player2"):
        
        if not multiple_instcheck((_rows, _columns), int):
            raise TypeError("Rows and columns must be a numerical parameters")
        
        elif _rows != _columns or not 9 <= _rows * _columns <= 64:   #3x3 - 8x8 -> Min & max board range
            raise ValueError("The number of rows and columns must be equals or the table size is minor than 3x3 or mayor than 8x8 (Max table size of 8x8)")
        
        elif not multiple_instcheck((player, player2), str):
            raise ValueError("Player attribute must be a string saying the name of the player")
        elif not multiple_instcheck((tokenplayer1, tokenplayer2), str) or tokenplayer1 == tokenplayer2:
            raise TypeError("Token player must be X or O and each player must define a different token")

        self.rows           = _rows
        self.columns        = _columns

        self.player1        = self._make_player_cache(player, tokenplayer1)
        self.player2        = self._make_player_cache(player2, tokenplayer2)
        
        self.board          = self._make_board()
        self.partycounter   = 0
        
        self._movtuple      = namedtuple("Movement", ["token", "player_name", "position", "moviment_time"])
        self._ptycachetuple = namedtuple("PartyCache", ["dictmap"])
        self._party_cache   = self._make_party_cache()
        self.debuginfo      = self._ptycachetuple(self._party_cache)

    @property
    def playing(self):
        return self._playing

    def _make_party_cache(self) -> dict[str,]:
        "Makes a party cache."

        party_cache = {
            "board_size": (self.rows, self.columns), 
            "players": (self.player1, self.player2), 
            "party": {
                "win": False,    #? Cuando un jugador gana, este atributo se convierte en diccionario 
                "movements": [],
                "total_time": 0
            }
        }
        return party_cache
        
    def _make_player_cache(self, player, token) -> dict[str,]:
        "Makes a player cache."

        cache = {
            "name": player,
            "token": token.strip().upper(),
            "movements": [],    #? Aqui solo se guarda la posicion del movimiento.
            "timings": [],
        }
        return cache

    def _clear_caches(self):
        "Limpia la cache."
        player1n, tknpl1 = self.player1["name"], self.player1["token"]
        player2n, tknpl2 = self.player2["name"], self.player2["token"]
        self.player1        = self._make_player_cache(player1n, tknpl1)
        self.player2        = self._make_player_cache(player2n, tknpl2)
        self._party_cache = self._make_party_cache()
        return

    def _make_board(self) -> list:
        "Private method to make a empty board"
        master_table = []
        
        for _ in range(0, self.columns):
            master_table.append([])
        
        for c in master_table:
            for _ in range(0, self.rows):
                    c.append("-")

        return master_table

    def _pprint(self, table) -> None:
        "Prints the table in a pretty way (without colons and token-colored)"
        print("\n")     # white line to stylize
        for i, column in enumerate(table):
            print(multiple_replace(f"\t{i+1} {column}", 
                    (
                        ("'", ""), 
                        (",", "  "), 
                        ("[", f"{Fore.LIGHTBLUE_EX}|{Fore.RESET} "),
                        ("]", f" {Fore.LIGHTBLUE_EX}|{Fore.RESET}"),
                        ("0", f"{Fore.LIGHTWHITE_EX}0{Fore.RESET}"), 
                        ("X", f"{Fore.LIGHTRED_EX}X{Fore.RESET}")
                    )
                )
            )


    #! PUBLIC METHODS   ----------------------------------------------------------------

    def turn(self) -> tuple[int, int]:
        "Fuction to manage the turns"
        self.turn_time = datetime.now()
        posx = input(f"{Fore.LIGHTGREEN_EX}[{self.actual_turn['name']}]{Fore.LIGHTGREEN_EX}{Fore.RESET}: {Fore.LIGHTWHITE_EX}Coloca la coordenada X -> {Fore.RESET}")
        posy = input(f"{Fore.BLUE}[{self.actual_turn['name']}]{Fore.BLUE}{Fore.RESET}: {Fore.LIGHTWHITE_EX}Coloca la coordenada Y -> {Fore.RESET}")
        self.turn_time = (datetime.now()-self.turn_time).total_seconds()
        try:
            posx = int(posx)
            posy = int(posy)
        except:
            print(f"{Fore.RED}[WARNING]{Fore.RED}Las coordenadas deben ser numeros!")
            self.turn()

        if (not 1 <= posx <= self.rows) or (not 1 <= posy <= self.columns) or (not 1 <= posx <= self.rows and not 1 <= posy <= self.columns):
            print(f"Las coordenadas deben estar comprendidas entre 1 y {self.rows}!!")
            self.turn()

        self.actual_turn = self._party_cache["players"][1-self._turn_index] #* para obtener el otro jugador.
        return posx, posy
        

    def draw_board(self, table, pos: tuple[int, int], player) -> None | bool:
        """# Importante:
            @param ``pos`` es una tupla que describe las coordenadas ``X`` e ``Y``, el orden es sumamente importante.\n
            Las coordenadas deben estar entre ``[1, board_columns] ∈ x``  --- ``[1, board_rows] ∈ y``
        """
        posx, posy = pos[0]-1, pos[1]-1


        if table[posx][posy] != "-":
            #? la posicion ya esta cogida, evitamos que tenga que comprobar de que tipo es.
            print(f"{Fore.RED}[WARNING]{Fore.RED}Ops! Esa posicion ya esta ocupada")
            return False
            
                  
        elif table[posx][posy] == player["token"]:
            #? la posicion esta ocupada por una ficha del mismo tipo
            print(f"{Fore.RED}[WARNING]{Fore.RED}Ops! Ya has puesto una ficha en esta posicion!")
            return False

        else:
            #? coloca la ficha
            table[posx][posy] = player["token"]
            
            #? Guarda el movimiento del jugador en su cache. SOLO LAS COORDENADAS
            player["movements"].append(pos)
            self._party_cache["party"]["movements"].append(self._movtuple(player["token"], player["name"], pos, self.turn_time))
            return    


    def checkWin(self) -> bool:
        """
        Metodo que alberga 4 metodos independientes:
        - Horizontal
        - Vertical 
        - Diagonal en tablas par
        - Diagonal en tablas impar
        
        
        #### Metodo horizontal
        ``Si todos los elementos de una sublista de la matriz son iguales, ha ganado.``

        #### Metodo vertical:

        ``Hace un range de la longitud de la matriz con la variable i.    
        Si el elemento i de la ultima subarray no es igual al de la primera o el elemento i de
        la primera subarray es "-" se salta a la siguiente iteracion (i+1).``\n
        ``Si los elementos de los extremos son iguales, se hace un range de la matriz de nuevo menos los extremos y se guardan los valores de la sublista[_][i] en
        otra lista checks.
        Si todos los elementos de la lista checks son iguales, ha ganado un jugador.
        Si no son iguales se continua iterando.``
        """

        def _save_win_to_cache(method: str):
            self._party_cache["party"]["win"] = {"method": method,}
            self._party_cache["party"]["win"]["player_name"] = self._party_cache ["party"]["movements"][-1][1]  #? 1 es el indice del nombre del jugador dentro de la namedtuple de Movimient



        for subarrays in self.board:
            if all(elem == subarrays[0] for elem in subarrays):
                _save_win_to_cache("Horizontal")
                return True
        

        for i in range(len(self.board)):
            if (self.board[0][i] == "-" or self.board[-1][i] == "-") or (self.board[-1][i] != self.board[0][i]):
                continue
            checks = [self.board[_][i] for _ in range(1, len(self.board)-1)]
            if all(elem == checks[0] for elem in checks):
                _save_win_to_cache("Vertical")
                return True


        #! Metodo diagonal con impares
        if len(self.board) % 2 != 0: 
            token = self.board[(len(self.board)//2)][(len(self.board)//2)]  #? centro de la matriz
        
            if token == "-":    #* si el centro de la matriz no es X o 0, no hay ninguna diagonal
                return False

            if self.board[0][0] == self.board[-1][-1] and self.board[0][0] == token:
                for i in range(1, len(self.board)-1):  #* evitamos pasar otra vez por las esquinas que sabemos que son iguales. 
                    if self.board[i][i] != token:
                        break
                    elif i == len(self.board)-2:   #* Si la ultima iteracion i es igual a la longitud de la tabla-2, quiere decir que todas las iteraciones anteriores son True, formando una diagonal.
                        _save_win_to_cache("Downwards diagonal")
                        return True

            if self.board[0][-1] == self.board[-1][0] and self.board[0][-1] == token:
                for i,s in zip(range(len(self.board)-1, 1, -1), range(1, len(self.board)-1), strict=True):
                    if self.board[i-1][s] != token:
                        break
                    elif s == len(self.board)-2:   #* Si la ultima iteracion i es igual a la longitud de la tabla-2, quiere decir que todas las iteraciones anteriores son True, formando una diagonal.
                        _save_win_to_cache("Upwards diagonal")
                        return True

        #! Metodo diagonal con impares
        else:
            if self.board[0][0] == "-" or self.board[0][-1] == "-":     #* Si alguna de las esquinas de las diagonales posibles esta vacia, no hay diagonales.
                return False

            if self.board[0][0] == self.board[-1][-1]:
                for i in range(1, len(self.board)-1):  #* evitamos pasar otra vez por las esquinas que sabemos que son True
                    if self.board[i][i] != self.board[0][0]:
                        break
                    elif i == len(self.board)-2:   #* Si la ultima iteracion i es igual a la longitud de la tabla-2 
                        #* (la posicion anterior a la esquina que no cuenta), quiere decir que todas las iteraciones anteriores son True, formando una diagonal.
                        _save_win_to_cache("Downwards diagonal")
                        return True

            if self.board[0][-1] == self.board[-1][0]:
                for i,s in zip(range(len(self.board)-1,1), range(1, len(self.board)-1)):
                    if self.board[i][s] != self.board[0][0]:    #* si alguna del medio no es igual a la primera, no es diagonal.
                        break
                    elif s == len(self.board)-2:  
                        _save_win_to_cache("Upwards diagonal")
                        return True
        return False


    def check_draw(self):
        ...


    def init_game(self):
        "Game loop flow, unless you cancel the game or one player win, the game will be cancelled"
        self.timecounter = 0
        self._playing = True
        self.actual_turn, self._turn_index = None, None

        # def game_loop():
        #     "Main loop timer, this function needs to be refreshed every time."
        #     self._initime = datetime.now()
        #     passed_seconds = (datetime.now() - self._initime).total_seconds()
            
        #     hours = int(passed_seconds / 60 / 60)
        #     passed_seconds -= hours*60*60
        #     minutes = int(passed_seconds/60)
        #     passed_seconds -= minutes*60
        #     return f"{hours:02d}:{minutes:02d}:{passed_seconds:02d}"
        
        def choice_start() -> None:
            self.actual_turn = choice(self._party_cache["players"])
            self._turn_index = self._party_cache["players"].index(self.actual_turn)
        
        cls()
        choice_start()
        try:
            while self._playing:
                # self.timecounter = game_loop()
                posx, posy = self.turn()
                draw = self.draw_board(self.board, (posx, posy), self.actual_turn)
                if not draw and draw is not None:
                    cls()
                    self.turn()
                    self.draw_board(self.board, (posx, posy), self.actual_turn)
                self._pprint(self.board)
                cwin = self.checkWin()
                if cwin:
                    print(f"{self._party_cache['party']['win']['player_name']} ha ganado !!!")
                    self._party_cache["party"]["total_time"] = self.timecounter
                    self._playing = False
                    break
        except KeyboardInterrupt:
            print(f"{Fore.LIGHTYELLOW_EX}Se ha finalizado el juego forzosamente.{Fore.RESET}")
            exit()


if __name__ == "__main__":
    er = [
        ['', '', '0'],
        ['', '0', ''],
        ['0', '', '']
    ]

    er2 = [
        ['', '', '', '0'],
        ['', '', '0', ''],
        ['', '0', '', ''],
        ['0', '', '', '']
    ]

    er3 = [
        ['', '', '', '', '0'],
        ['', '', '', '0', ''],
        ['', '', '0', '', ''],
        ['', '0', '', '', ''],
        ['0', '', '', '', '']
    ]

    def checkWin(l) -> bool:

        for subarrays in l:
            if all(elem == subarrays[0] for elem in subarrays if elem != "-"):
                return True
        

        for i in range(len(l)):
            if (l[0][i] == "-" or l[-1][i] == "-") or (l[-1][i] != l[0][i]):
                continue
            checks = [l[_][i] for _ in range(len(l))]
            if all(elem == checks[0] for elem in checks):
                return True


        if len(l) % 2 != 0:
            token = l[(len(l)//2)][(len(l)//2)]  #? center of the matrix
        
            if token == "-":    #* si el centro de la matriz no esta completo, no hay ninguna diagonal
                return False

            if l[0][0] == l[-1][-1] and l[0][0] == token:
                for i in range(1, len(l)-1):  #* evitamos pasar otra vez por las esquinas que sabemos que son True
                    if l[i][i] != token:
                        break
                    elif i == len(l)-2:   
                        return True

                
            if l[0][-1] == l[-1][0] and l[0][-1] == token:
                for i,s in zip(range(len(l)-1,1,-1), range(1, len(l)-1), strict=True):
                    if l[i-1][s] != token:
                        break
                    elif s == len(l)-2:   
                        return True
        else:
            if l[0][0] == "-" or l[0][-1] == "-":
                return False
            if l[0][0] == l[-1][-1]:
                for i in range(1, len(l)-1):  #* evitamos pasar otra vez por las esquinas que sabemos que son True
                    if l[i][i] != l[0][0]:
                        break
                    elif i == len(l)-2:   
                        return True

            if l[0][-1] == l[-1][0]:
                for i,s in zip(range(len(l)-1,1), range(1, len(l)-1)):
                    if l[i][s] != l[0][0]:
                        break
                    elif s == len(l)-2:   
                        return True
        return False
    
    print(checkWin(er))
    print(checkWin(er2))
    print(checkWin(er3))

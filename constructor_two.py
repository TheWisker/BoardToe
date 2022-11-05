from utils import *
from langs import Langs
from AI.Bot import Bot
from Player import Player
import core

from random import choice, randint
from time import time, sleep
from datetime import datetime
from collections import namedtuple
from os import get_terminal_size
from threading import Thread

from pybeaut import Col as _Col
from colorama import Fore





class BoardGame:

    _movtuple           = namedtuple("Movement", ["token", "player_name", "position", "moviment_time"])
    _ptycachetuple      = namedtuple("PartyCache", ["partymapping"])

    AVAILABLE_COLORS    = [c for c in vars(Fore).keys() if c != "RESET" or not c.endswith("_EX")]
    XCOLOR              = Fore.LIGHTRED_EX      #* static color for 'X' if player does not give any color
    OCOLOR              = Fore.LIGHTWHITE_EX    #* static color for '0' if player does not give any color
    XTOKEN              = "❌"
    OTOKEN              = "⭕"

    def __init__(
        self, 
        _rows: int, 
        _columns: int, 
        player1: Player,
        player2: Player,
        game_mode: int = 1,
        game_lang: str = "SPANISH",
        _show_stats: bool = True
        
    ):
        
        if not multiple_instcheck((_rows, _columns), int):
            raise TypeError("Rows and columns must be a numerical parameters")
        
        elif _rows != _columns or not 9 <= _rows * _columns <= 64:   #3x3 - 8x8 -> Min & max board range
            raise ValueError("The number of rows and columns must be equals or the table size is minor than 3x3 or mayor than 8x8 (Max table size of 8x8)")
        
        elif not game_lang in Langs.langs_supported():
            ...
        
        self.debuginfo = self.stats = self._ptycachetuple(self._party_cache)

        self.rows               = _rows
        self.columns            = _columns
        self.board              = None       #? para evitar crearla antes de comenzar el juego, se crea cuando se llama a init_game()

        self.game_lang          = game_lang
        self.game_mode          = game_mode 
        self._playing           = False
    
        self._party_cache       = self._make_party_cache()
        self._game_cache        = []

        self.player1: Player    = player1
        self.player2: Player    = player2

        if self.player1.name == "Player":
            self.player1._name = "Player1"
        if self.player2.name == "Player":
            self.player2._name = "Player2"

    @property
    def playing(self):
        return self._playing

    @property 
    def available_colors(self) -> list[str]:
        return self.AVAILABLE_COLORS


    def _make_party_cache(self) -> dict[str,]:
        "Makes a party cache."
        return {
            "board_size": (self.rows, self.columns), 
            "players": (self.player1, self.player2), 
            "party": {
                "total_time": 0,
                "win": False,    #? Cuando un jugador gana, este atributo se convierte en diccionario 
                "movements": []
            }
        }


    def _clear_caches(self) -> None:
        "Limpia la cache."
        self.player1._clear_cache()
        self.player2._clear_cache()
        self._party_cache   = self._make_party_cache()


    def _make_board(self) -> list:
        """``Metodo privado para crear una tabla vacia.``

        - Metodo mejorado para creacion de matrices vacias.
    
            Antes:
            >>>    t = []
            >>>    for _ in range(0, len(table)):
            >>>        t.append([])    
            >>>    for c in t:  
            >>>        c.append("-" for _ in range(0, len(table)))
            
            Despues: 
            >>> t = [['-' for _ in range(len(table))] for _ in range(len(table))]"""

        t = [['-' for _ in range(self.rows)] for _ in range(self.columns)]
        return t


    def _save_win_to_cache(self, method: str):
        self._party_cache["party"]["win"] = {"method": method}
        self._party_cache["party"]["win"]["player_name"] = self._party_cache["party"]["movements"][-1][1]  
        #? 1 es el indice del nombre del jugador dentro de la namedtuple de Movimient


    #! RETOCAR LA FUNCION
    def _pprint(self, table) -> None:
        "Prints the table in a pretty way (without colons and token-colored)"

        columns, lines = get_terminal_size().columns, get_terminal_size().lines
        print("\n")     # white line to stylize
        for i, column in enumerate(table):
            print(multiple_replace("{} {}{}".format(" "*(columns//2-self.rows//2), i+1, column), 
                    (
                        ("'", ""), 
                        (",", "  "), 
                        ("[", f"{Fore.LIGHTBLUE_EX}║{Fore.RESET} "),
                        ("]", f" {Fore.LIGHTBLUE_EX} ║{Fore.RESET}"),
                        ("⭕", f"{self.OCOLOR}⭕{Fore.RESET}"), 
                        ("❌", f"{self.XCOLOR}❌{Fore.RESET}")
                    )
                )
            )
        print("\n")     # white line to stylize


    def show_stats(self) -> str | dict[str,]:
        print(self.stats)


    #! PUBLIC METHODS   ----------------------------------------------------------------

    def turn(self) -> tuple[int, int]:
        "Fuction to manage the turns"
        
        try:
            posx, posy = self.actual_turn.take_turn()[1]
            posx = int(posx)
            posy = int(posy)
        except:
            print(f"\n{Fore.RED}[WARNING] -> {Langs.get_phrase(self.game_lang, 'errors', 0)}{Fore.RESET}") #Las coordenadas deben ser numeros!
            return self.turn()

        if (not 1 <= posx <= self.rows) or (not 1 <= posy <= self.columns) or (not 1 <= posx <= self.rows and not 1 <= posy <= self.columns):
            print(f"\n{Fore.RED}[WARNING] -> {Langs.get_phrase(self.game_lang, 'errors', 1).format(self.rows)}{Fore.RESET}") #Las coordenadas deben estar entre 1 y {}
            return self.turn()

        self.turn_time = self.actual_turn.take_turn[0]     #? Si el turno es valido, entonces se guarda el tiempo, no antes.
        return posx, posy
        

    def draw_board(self, table, pos: tuple[int, int], player: Player) -> None:
        """# Importante:
            @param ``pos`` es una tupla que describe las coordenadas ``X`` e ``Y``, el orden es sumamente importante.\n
            Las coordenadas deben estar entre ``[1, board_columns] ∈ x``  --- ``[1, board_rows] ∈ y``
        """
        posx, posy = pos[0]-1, pos[1]-1


        if table[posx][posy] != "-":
            #? la posicion ya esta cogida hmmm que rico, evitamos que tenga que comprobar de que tipo es.
            print(f"\n{Fore.RED}[WARNING] -> {Langs.get_phrase(self.game_lang, 'errors', 2).format(pos, table[posx][posy])}{Fore.RESET}") #¡Ops! Esa posicion ya esta ocupada. (Posicion: {}, token: {})

            posx, posy = self.turn()
            return self.draw_board(table, (posx, posy), player)
            
        elif table[posx][posy] == player.token:
            #? la posicion esta ocupada por una ficha del mismo tipo
            print(f"\n{Fore.RED}[WARNING] -> {Langs.get_phrase(self.game_lang, 'errors', 3)}{Fore.RESET}") #¡Ya has puesto una ficha en esta posicion!
            posx, posy = self.turn()
            return self.draw_board(table, (posx, posy), player)

        else:
            table[posx][posy] = player.token
            
            #? Guarda el movimiento del jugador en su cache. SOLO LAS COORDENADAS
            player.addmov(pos, self.turn_time)      #? tambien añade el tiempo
            self._party_cache["party"]["movements"].append(self._movtuple(player.token, player.name, pos, self.turn_time))
            
            _last_turn_index = self._party_cache["players"].index(self.actual_turn)
            self.actual_turn = self._party_cache["players"][_last_turn_index-1]   
            #* para obtener el otro jugador se busca el indice del jugador y se le resta 1.
            return    

    def checkWin(self) -> bool:
        """
            Metodo que alberga 4 metodos independientes:
            - Horizontal
            - Vertical 
            - Diagonal en tablas par
            - Diagonal en tablas impar
            
            #### Metodo horizontal:
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

        bmatrix = core.transform2matrix(self.board) #? la transformamos a binarios

        for subarrays in self.board:
            if subarrays[0] == "-":
                continue
            if all(elem == subarrays[0] for elem in subarrays):
                self._save_win_to_cache("Horizontal")
                return True


        for i in range(len(self.board)):
            if (self.board[0][i] == "-" or self.board[-1][i] == "-") or (self.board[-1][i] != self.board[0][i]):
                continue
            checks = [self.board[_][i] for _ in range(1, len(self.board)-1)]
            if all(elem == self.board[0][i] for elem in checks):
                self._save_win_to_cache("Vertical")
                return True


        if len(self.board) % 2 != 0: 
            token = self.board[(len(self.board)//2)][(len(self.board)//2)]  #? centro de la matriz

            if token == "-":    #* si el centro de la matriz no es X o 0, no hay ninguna diagonal
                return False

            if self.board[0][0] == self.board[-1][-1] and self.board[0][0] == token:
                for i in range(1, len(self.board)-1):  #* evitamos pasar otra vez por las esquinas que sabemos que son iguales. 
                    if self.board[i][i] != token:
                        break
                    elif i == len(self.board)-2:   #* Si la ultima iteracion i es igual a la longitud de la tabla-2, quiere decir que todas las iteraciones anteriores son True, formando una diagonal.
                        self._save_win_to_cache("Downwards diagonal")
                        return True

            if self.board[0][-1] == self.board[-1][0] and self.board[0][-1] == token:
                for i,s in zip(range(len(self.board)-1, 1, -1), range(1, len(self.board)-1), strict=True):
                    if self.board[i-1][s] != token:
                        break
                    elif s == len(self.board)-2:   #* Si la ultima iteracion i es igual a la longitud de la tabla-2, quiere decir que todas las iteraciones anteriores son True, formando una diagonal.
                        self._save_win_to_cache("Upwards diagonal")
                        return True

        else:
            if self.board[0][0] == "-" or self.board[0][-1] == "-":     #* Si alguna de las esquinas de las diagonales posibles esta vacia, no hay diagonales.
                return False

            if self.board[0][0] == self.board[-1][-1]:
                for i in range(1, len(self.board)-1):  #* evitamos pasar otra vez por las esquinas que sabemos que son True
                    if self.board[i][i] != self.board[0][0]:
                        break
                    elif i == len(self.board)-2:   #* Si la ultima iteracion i es igual a la longitud de la tabla-2 
                        #* (la posicion anterior a la esquina que no cuenta), quiere decir que todas las iteraciones anteriores son True, formando una diagonal.
                        self._save_win_to_cache("Downwards diagonal")
                        return True

            if self.board[0][-1] == self.board[-1][0]:
                for i,s in zip(range(len(self.board)-1,1), range(1, len(self.board)-1)):
                    if self.board[i][s] != self.board[0][0]:    #* si alguna del medio no es igual a la primera, no es diagonal.
                        break
                    elif s == len(self.board)-2:  
                        self._save_win_to_cache("Upwards diagonal")
                        return True
        return False

    def _checkwin2(self) -> bool:
        """Second option to make the win method"""

        bintable = core.transform2matrix(self.board)
        core.hcheck(bintable)
        core.hcheck(core.rotate_matrix(bintable))


    def checkDraw(self) -> bool:
        "Verifica si ha habido un empate. Por ahora solo verifica que ha habido un empate cuando en la tabla no hay mas posiciones libres y nadie a ganado"
        empty_locs = 0

        for i in range(len(self.board)):
            if any(elem == "-" for elem in self.board[i]):
                break
            if i == len(self.board)-1:
                self._save_win_to_cache("Draw")
                return True

        for i,s in zip(range(len(self.board)), range(0, len(self.board), -1)):
            if self.board[i][s] == "-":
                empty_locs += 1

        return False
                
        
    def init_game(self) -> str | None:
        "Game loop flow, unless you cancel the game or one player win, the game will be cancelled"

        self._clear_caches()     #* vacia la cache para iniciar una nueva partida, aunque ya se haya limpiado antes.  

        self.board: list[list]          = self._make_board()
        self._playing: bool             = True
        self.actual_turn: Player        = choice(self._party_cache["players"])

        try:
            while self._playing:
                self.partycounter  = datetime.now()

                self._pprint(self.board)
                posx, posy = self.turn()
                self.draw_board(self.board, (posx, posy), self.actual_turn)
                
                if self.checkWin():
                    self.partycounter = round((datetime.now()-self.partycounter).total_seconds())
                    self._pprint(self.board)
                    print(f"{Langs.get_phrase(self.game_lang, 'game', 2).format(self._party_cache['party']['win']['player_name'].upper())}") #¡{} ha ganado!
                    break

                elif self.checkDraw():
                    self.partycounter = round((datetime.now()-self.partycounter).total_seconds())
                    self._pprint(self.board)      
                    print(f"EMPATE!!")
                    break              

                cls()

        except KeyboardInterrupt:
            print(f"\n{Fore.LIGHTYELLOW_EX}[GAME LOOP STOPED] -> {Langs.get_phrase(self.game_lang, 'runtime', 0)}{Fore.RESET}") #Se ha finalizado el juego forzosamente.
            exit()

        self.player1.cache["best_timing"]     = min(self.player1["timings"])
        self.player1.cache["worst_timing"]    = max(self.player1["timings"])
        self.player2.cache["best_timing"]     = min(self.player2["timings"])
        self.player2.cache["worst_timing"]    = max(self.player2["timings"])

        self._party_cache["party"]["total_time"] = self.partycounter
        self._game_cache.append(self._party_cache)
        self._playing = False

        self._clear_caches()

        self.show_stats()

        
        
if __name__ == "__main__":
    ...

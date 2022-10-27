from constants import *
from langs import Langs
from constructor import BoardGame, Fore, time, sleep

from pystyle import Box, Colorate, Colors, Center, Write


def title() -> None:
    maintitle = Center.Center(Colorate.Horizontal(Colors.blue_to_green, WELCOME_TEXT2), yspaces= 8, xspaces=50)
    print(maintitle)
title()


lang = input(f"{Langs.get_phrase('SPANISH', 'game', 0)} -> ") #¿En que idioma desea jugar?

test = BoardGame(4,4, "0", "X", game_lang=lang) 

test._clear_caches()
test.init_game()


#* TESTS ///////////////////////

# movements = [
#     (test.player1, (1, 3)),
#     (test.player2, (3, 3)),
#     (test.player2, (2,2)),
#     (test.player1, (2,3)),s
#     (test.player2, (1,1))
# ]

# for mov in movements:
#     test.draw_board(test.board, mov[1], player = mov[0])
# test._pprint(test.board)
# test.checkWin()

# print(f"\n{Fore.LIGHTGREEN_EX}DEBUGGING INFO:{Fore.RESET}\n")
# print(f"Party cache: {test.debuginfo}\n")
# print(f"Player1 cache: {test.player1}\n")
# print(f"Player2 cache: {test.player2}\n")


    
        







    
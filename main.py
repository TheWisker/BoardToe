from constants import *
from langs import Langs
from constructor import BoardGame, Fore, time, sleep

try:
    from pybeaut import *
except (ImportError or ModuleNotFoundError) as i:
    from os import system, name
    print(f"\n[MISSING INDEPENDENCIES] -> It seems that you are missing a requeriment to play the game. Missing {i.name if i.name else 'one module'}.")
    print("Preparing...")
    system("pip install -U pybeaut" if name == "nt" else "pip3 install -U pybeaut")
    print(f"Successfully installed {i.name}\n")



def display_options(field_opts: list[list[str]], fields_names: list[str] = None, color: Colors = None) -> str:
    r= []
    for i,t in zip(range(len(field_opts)), field_opts):
        r.append(f"[{i+1}] {t}\n")
    
    e = Box.DoubleCube("".join(r))
    print(Center.Center(Colorate.Horizontal(Col.blue_to_red, e)))

display_options(["Human vs Human", "Human vs CPU", "CPU vs CPU"])

lang = input(f"{Langs.get_phrase('SPANISH', 'game', 0)} -> ") #¿En que idioma desea jugar?

test = BoardGame(5,5, "0", "X", game_lang=lang) 

test._clear_caches()
test.init_game()


#* TESTS ///////////////////////

# movements = [
#     (test.player1, (1, 3)),
#     (test.player2, (3, 3)),
#     (test.player2, (2,2)),
#     (test.player1, (2,3)),
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


    
        







    
from constants import *
from langs import Langs
from constructor import BoardGame, Fore
from Player import Player, _Col

try:
    from pybeaut import *
except (ImportError or ModuleNotFoundError) as i:
    from os import system, name
    print(f"\n[MISSING INDEPENDENCIES] -> It seems that you are missing a requeriment to play the game. Missing {i.name if i.name else 'one module'}.")
    print("Preparing...")
    system("pip install -U pybeaut" if name == "nt" else "pip3 install -U pybeaut")
    print(f"Successfully installed {i.name}\n")




#TODO ///////////////////////////////////////      TUI SECTION        ////////////////////////////////////////////////

def display_options(field_opts: list[list[str]], fields_names: list[str] = None, color: Colors = None) -> str:
    r= []
    for i,t in zip(range(len(field_opts)), field_opts):
        r.append(f"[{i+1}] {t}\n")
    
    e = Box.DoubleCube("".join(r))
    print(Center.Center(Colorate.Horizontal(Col.cyan_to_blue, e)))

display_options(["Human vs Human", "Human vs CPU", "CPU vs CPU"])

def load_menu():
    ...




#TODO ///////////////////////////////////////      MAIN GAME FLOW        ////////////////////////////////////////////////


# lang = input(f"{Langs.get_phrase('SPANISH', 'game', 0)} -> ") #¿En que idioma desea jugar?
player1 = Player("⭕", "Alvaritow", "red")
player2 = Player("❌", "Fanico", "green")
test = BoardGame(5,5, player1, player2, game_lang="SPANISH") 

test._clear_caches()
test.init_game()



#* TESTS ///////////////////////

...

    
        







    
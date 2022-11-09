from constants import *
from Bot import *
from time import sleep
from constructor import BoardGame, _Col, Logger, get_terminal_size
from Player import Player


try:
    from pybeaut import *
except (ImportError or ModuleNotFoundError) as e:
    from os import system, name
    print(f"\n[MISSING INDEPENDENCIES] -> It seems that you are missing a requeriment to play the game. Missing {e.name if e.name else 'one module'}.")
    print("Preparing...")
    system("pip install -U pybeaut" if name == "nt" else "pip3 install -U pybeaut")
    print(f"Successfully installed {e.name}\n")



#TODO ///////////////////////////////////////      TUI SECTION        ////////////////////////////////////////////////

#! Mirar el modulo 'climage' de python. Es un manejador de imagenes que convierte la imagen a su codigo de escape ansi.
#! Si el sistema es UNIX, se ofrece mejor compatibilidad con el modulo 'term-image'.


def make_box():
    ...

def display_header(header: str, banner: str = None):
    #Banner(header, banner)
    ...


def display_options(field_opts: list[list[str]], fields_names: list[str] = None, color: Colors = None) -> str:
    r= []
    for i,t in zip(range(len(field_opts)), field_opts):
        r.append(f"[{i+1}] {t}\n")
    
    e = Box.DoubleCube("".join(r))
    print(Center.Center(Colorate.Horizontal(Col.cyan_to_blue, e)))

def reveal_anim(t: str, color: _Col = _Col.white, interval: int | float = 0.08, overlap: bool = False):
    """Genera una animacion de texto donde las letras se van revelando poco a poco. 
    ``Metodo recursivo.``
    """
    for i in range(len(t)):
        print(f"{color}{t[:i]}", end="\r")
        sleep(interval)
        if t[i] == "\n":
            if overlap:
                reveal_anim(f"{color}{t[i+1:]}", color, interval, True)
                print("\r"+_Col.reset)
                break
            print("\r")
            reveal_anim(f"{color}{t[i+1:]}", color, interval)
            print("\r"+_Col.reset)
            break


def load_menu():
    ...




#TODO ///////////////////////////////////////      MAIN GAME FLOW        ////////////////////////////////////////////////

reveal_anim(SPLASH_TEXT, _Col.cyan)
# print(Box.DoubleCube(SPLASH_TEXT))
display_options(["Human vs Human", "Human vs CPU", "CPU vs CPU"])

lang = input(f"{Logger._get_phrase('game', 0)}:  ") #¿En que idioma desea jugar?
if input(f"{Logger._get_phrase('game', 1, lang).format(lang)}  ").lower() in ["yes", "y"]:
    pass

print("\n")

player1 = Player("❌", "Alvaritow", "red")
player2 = Player("❌", "Fanico", "green")

test = BoardGame((8,8), player1, Bot("⭕", color="red", difficulty="imposible"), game_lang=lang.upper()) 

test.init_game()



#* TESTS ///////////////////////

...

    
        






    
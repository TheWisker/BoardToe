from constants import *
from utils import *
from AI.Bot import *
from constructor import BoardGame, Logger
from Player import Player

from os import system, mkdir, get_terminal_size
from time import sleep
from getpass import getpass

from pybeaut import Col as _Col, Center, Cursor, Colorate
# from tempfile import tempdir, TemporaryDirectory, TemporaryFile


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

TERMSIZE: list[int, int] = [get_terminal_size().columns, get_terminal_size().lines]


#& ************  ALIGNMENT FUNCS **************

def _padding(size: int = 5, custom_icon: str = None) -> None:
    "Genera X saltos de linea o espacios"
    if custom_icon is not None:
        print(custom_icon*size)
    else:
        print("\n"*size)

def _charging(repeats: int = 3, _interval: int = 0.1, delay: int = 0.25, color: _Col = None, hc: bool = True) -> None:
    """Crea una animacion de cargar.\n## Parametros.\n
    - @repeats: Las veces que repite la animacion de carga 
    - @interval: Tiempo de espera entre cada punto
    - @delay: Tiempo de espera entre repeticiones.
    - @color: Color para la animacion de carga.
    - @hc: Esconde el cursor si es ``True``"""
    _ = "• • •"

    if hc:
        Cursor.HideCursor()
    def loop():
        for i in range(len(_)):
            print(_[:i+1], end= "\r")
            sleep(_interval)
            if color is not None:
                print(f"{color}{_[:i+1]}", end= "\r")
                sleep(_interval)
    
    for r in range(repeats):
        loop()
        print(" "*len(_), end= "\r")  #? len of _ (5 white spaces)
        sleep(delay)
    sleep(0.1)      #? smooth exit
    if hc:
        Cursor.ShowCursor()

#! Hacer para que se ajuste al tamaño de la terminal y haga un salto de linea automatico
def reveal_anim(t: str, color: _Col = _Col.white, interval: int | float = 0.05, overlap: bool = False):
    """Genera una animacion de texto donde las letras se van revelando poco a poco. 
    ``Metodo recursivo.``
    """
    for i in range(len(t)):
        print(f"{color}{t[:i]}", end="\r")
        sleep(interval)
        if t[i] == "\n":
            if overlap:
                reveal_anim(f"{color}{t[i+1:]}", color, interval)
                break
            print("\n")
            reveal_anim(f"{color}{t[i+1:]}", color, interval)
            break
    print(_Col.reset)
        

#& ************  TUI WRAPPERS **************

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
    print(Center.YCenter(Colorate.Horizontal(Col.cyan_to_blue, e)))




def load_menu():
    "Loads the main menu"

    Cursor.HideCursor()
    _charging(randint(2, 4), color= _Col.cyan, hc=False)

    cls()    
    getpass(Colorate.Horizontal(_Col.blue_to_cyan, "Press Enter Key to continue. . ."))
    cls()

    print(Center.Center(Colorate.Horizontal(_Col.blue_to_cyan, WELCOME_TEXT2)))
    _padding(3)
    reveal_anim(Center.XCenter(SPLASH_TEXT), _Col.light_gray)
    display_options(["Human vs Human", "Human vs CPU", "CPU vs CPU"])
    Cursor.ShowCursor()



def config_menu():
    ...



#TODO ///////////////////////////////////////      MAIN GAME FLOW        ////////////////////////////////////////////////
if __name__ == "__main__":

    load_menu()

    lang = input(f"{Logger._get_phrase('game', 0)}:  ").upper() #¿En que idioma desea jugar?
    if input(f"{Logger._get_phrase('game', 1, lang).format(lang)}  ").lower() in ["yes", "y"]:
        pass

    player1 = Player("❌", "Alvaritow", "red")
    player2 = Player("❌", "Fanico", "green")

    test = BoardGame((4,4), player1, Bot("⭕", color="red", difficulty="easy"), game_lang=lang.upper()) 

    test.init_game()

    
        






    
from constants import *
from utils import *
from AI.Bot import *
from constructor import BoardGame, Logger,AVAILABLE_LANGS
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

def _padding(size: int = 5, X: bool = False, custom_icon: str = None) -> None:
    "Genera espacios en la direccion dada (X, Y).\n``Predeteminadamente hace salto de linea (\\n)``"
    if custom_icon is not None:
            print(custom_icon*size)
    if X:
        print(" "*size)
    else:
        print("\n"*size)

def _charging(repeats: int = 3, interval: int = 0.1, delay: int = 0.25, color: _Col = None, hc: bool = True) -> None:
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
            sleep(interval)
            if color is not None:
                print(f"{color}{_[:i+1]}", end= "\r")
                sleep(interval)
    
    for r in range(repeats):
        loop()
        print(" "*len(_), end= "\r")  #? len of _ (5 white spaces)
        sleep(delay)
    sleep(0.1)      #? smooth exit
    if hc:
        Cursor.ShowCursor()

def adjust_content(text: str, termlen: int = get_terminal_size().columns) -> list[str]:
    fraction = round(len(text) / termlen)
    if fraction < 2:        #? si el resultado de la division es 0.xx se redondea a 1
        return [text]
    _ = []
    for i in range(fraction):
        e = text[:termlen+1]
        _.append(e)
        text = text[termlen+1:]
    return _

def reveal_anim(t: str, color: _Col = None, interval: int | float = 0.05, overlap: bool = False, center: bool = False, fit: bool = False) -> None:
    """Genera una animacion de texto donde las letras se van revelando poco a poco. 
    ``Metodo recursivo.``
    """

    if center:
        if fit:
            for i in adjust_content(t):
                reveal_anim(i, color, interval, overlap)
                return
        for i in t.splitlines(True):
            reveal_anim(Center.XCenter(i), color, interval, overlap)
            return
    elif fit:
        for i in adjust_content(t):
            reveal_anim(i, color, interval, overlap)
            return
        
    
    for i in range(len(t)):
        if color is not None:
            print(f"{color}{t[:i]}", end="\r")
        else:
            print(t[:i], end="\r")
        sleep(interval)
        if t[i] == "\n":
            if overlap:
                reveal_anim(t[i+1:], color, interval)
                break
            print("\r")
            reveal_anim(t[i+1:], color, interval)
            break
    print(_Col.reset)
        

#& ************  TUI WRAPPERS **************

def _make_box(fields: list[str], color: _Col = _Col.white, btitle: str = None, enum: bool = False, simplecube: bool = False):
 
    t = []
    # if btitle is not None:
    #     t.append(f"{btitle}\n")
    
    for i in range(len(fields)):
        if enum:
            t.append(f"[{i+1}] {fields[i]}")
        else:
            t.append(f"{fields[i]}")
    
    if simplecube:
        if color:
            return Colorate.Horizontal(color, Box.SimpleCube("\n".join(t)))
        return Box.SimpleCube("".join(t))
    
    return Box.SimpleCube(f"{btitle}\n")+ "\n" + Box.DoubleCube("".join(t)) if not color else Colorate.Color(color, Box.DoubleCube("\n".join(t)))

        
# print(_make_box(["Human vs Human", "Human vs CPU", "CPU vs CPU"], btitle="Game modes", enum=True))


def load_menu():
    "Loads the main menu"

    Cursor.HideCursor()
    _charging(randint(2, 4), color= _Col.cyan, hc=False)

    cls()    
    getpass(Colorate.Horizontal(_Col.blue_to_cyan, "Press Enter Key to continue. . ."))
    cls()

    print(Colorate.Horizontal(_Col.blue_to_cyan, BANNER))
    _padding(3)
    reveal_anim(SPLASH_TEXT, fit= True)
    Cursor.ShowCursor()



def config_menu():
    ...



#TODO ///////////////////////////////////////      MAIN GAME FLOW        ////////////////////////////////////////////////
if __name__ == "__main__":

    load_menu()

    lang = input(Center.XCenter(f"{_Col.cyan}{Logger._get_phrase('game', 0)}:  ")).upper() #¿En que idioma desea jugar?
    if lang not in AVAILABLE_LANGS:
        ...
    if input(f"{Logger._get_phrase('game', 1, lang).format(lang)}  ").lower() in ["yes", "y"]:
        pass

    player1 = Player("❌", "Alvaritow", "red")
    player2 = Player("❌", "Fanico", "green")

    test = BoardGame((5,5), player1, Bot("⭕", color="red", difficulty="easy"), game_lang=lang.upper()) 

    test.init_game()

    
        






    
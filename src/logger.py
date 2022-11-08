from pybeaut import Col as _Col
from constants import EMOJI_MAPPING, OTOKEN, XTOKEN
from _langs import *

# __all__ = ["Logger", "get_phrase", "AVAILABLE_LANGS"]

class Logger:
    ...



def get_phrase(lang: str, level: str, index: int) -> str:
    "Devuelve la frase con indice del idioma y nivel pasado"
    return langs[lang.upper()][level.lower()][index]
from deep_translator import GoogleTranslator

__all__ = ["LANGS"]


class LANGS:

    def __init__(self) -> None:
        # self._translate()
        ...
        

    langs: dict = {
        "SPANISH": {
            "errors": [
                "¡Las coordenadas deben ser numeros!", #0
                "Las coordenadas deben estar entre 1 y {}", #1
                "¡Ops! Esa posicion ya esta ocupada. (Posicion: {}, Token: {})", #2
                "¡Ya hay una ficha en esta posicion!" #3
            ],
            "runtime": [
                "Se ha finalizado el juego forzosamente." #0
            ],
            "game": [
                "¿En que idioma desea jugar?", #0
                "Su idioma es el {}, ¿Correcto?",
                "¡{} ha ganado el juego!", #2
                "Coloca la coordenada {}", #3
            ],
            "cache": []
        },
        "ENGLISH": {"errors": ["Coordinates must be numbers!","Coordinates must be between 1 and {}"], "game": []},
        "GERMAN": {"errors": [], "game": []},
        "RUSSIAN": {"errors": [], "game": []},
        "JAPANESE": {"errors": [], "game": []},
        "KOREAN": {"errors": [], "game": []},
        "FRENCH": {"errors": [], "game": []},
        "ITALIAN": {"errors": [], "game": []},
        "CHINESE": {"errors": [], "game": []},
        "VIETNAMESSE": {"errors": [], "game": []},
        "UKRANIAN": {"errors": [], "game": []},
        "LATIN": {"errors": [], "game": []},
        "GREEK": {"errors": [], "game": []},
        "CATALAN": {"errors": [], "game": []},
        "CZECH": {"errors": [], "game": []},
        "SLOVENIAN": {"errors": [], "game": []},
        "DANISH": {"errors": [], "game": []},
        "IRISH": {"errors": [], "game": []},
        "PORTUGUESE": {"errors": [], "game": []}
    }
    
    LANG_LIST = [l for l in langs.keys()] #langs.keys().mapping ???

    @staticmethod
    def get_phrase(lang: str, level: str, index: int) -> str:
        if not lang.upper() in LANGS.LANG_LIST:
            raise ValueError(f"This language is not set!!. Available langs: {LANGS.LANG_LIST}")
        return LANGS.langs[lang.upper()][level][index]

    def _translate(self):
        ...
            

        
    

    
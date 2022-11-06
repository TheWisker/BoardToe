from deep_translator import GoogleTranslator
#! https://pypi.org/project/deep-translator/

__all__ = ["LANGS"]

class Langs:
    
    traductor = GoogleTranslator
    langs_supported: list[str] = ["SPANISH", "ENGLISH", "CROATIAN", "GALICIAN", "CATALAN", "PORTUGUESE", "DUTCH", "GERMAN", "ITALIAN", "CHINESE (simplified)", "JAPANESE", "FRENCH", "RUSSIAN", "HINDI", "DANISH", "SERBIAN"] 

    langs = {
            "SPANISH": {
                "errors": [
                    "¡Las coordenadas deben ser numeros!", #0
                    "Las coordenadas deben estar entre 1 y {}", #1
                    "¡Ops! Esa posicion ya esta ocupada. (Posicion: {})", #2
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
        }


    def __init__(self) -> None:
        self._init_langs()
        self._load_langs()
    

    def _init_langs(self) -> None:
        "Inicializa la traducion de todos los idiomas y los guarda en el diccionario ``langs'' ya iniciado"
        for i in Langs.langs_supported:
            if i == "SPANISH":
                continue
            else:
                    self.langs[i.upper()] = {"errors": [], "game": []}
        return

    def _load_langs(self):
        for level,p in self.langs["SPANISH"].items():
            for ln, lv in self.langs.items():
                self.langs[ln][level] = self.traductor(source= "spanish", target=ln.lower().lower()).translate_batch(p)

    @staticmethod
    def get_phrase(lang: str, level: str, index: int) -> str:
        if not lang.upper() in Langs.langs_supported:
            raise ValueError(f"This language is not set!!. Available langs: {Langs.langs_supported}")
        return Langs.langs[lang.upper()][level][index]
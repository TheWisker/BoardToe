from pybeaut import Col as _Col
from constants import EMOJI_MAPPING
from _langs import *


# __all__ = ["Logger", "get_phrase", "AVAILABLE_LANGS"]


#? Para rapida lectura de los emojis
# EMOJI_MAPPING = {
#     "gearwheel": " ⚙️ ",
#     "megaphone": "📢",
#     "lock": "🔒",
#     "stop_signal": "⛔️",
#     "exclamation": "❕",
#     "loudspeaker": "🔊",
#     "tie": "🤝",
#     "robotic_arm": "🦾",
#     "first_medal": "🥇",
#     "cup": "🏆",
#     "robot": "🤖",
#     "magnifying_glass": "🔍"
#     "question": "❔"
# }

EM = EMOJI_MAPPING

loggers: dict[str, list[str, str]] = {
    "errors":       [_Col.blue, f"[{EM['gearwheel']} ][{EM['megaphone']}] ",   _Col.red],
    "runtime":      [_Col.blue, f"[{EM['megaphone']} ][{EM['exclamation']}] ", _Col.yellow],
    "game":     	[_Col.blue, f"[{EM['cup']} ][{EM['first_medal']}] ",       _Col.cyan],
    "victory":      [_Col.blue, f"[{EM['cup']} ][{EM['first_medal']}] ",       _Col.cyan],
    "message":     [_Col.blue, f"[{EM['gearwheel']} ][{EM['loudspeaker']}] ",       _Col.white],
    "question":     [_Col.blue, f"[{EM['gearwheel']} ][{EM['question']}] ",       _Col.white],
}


class Logger:

    def __init__(self, lang: str = "ENGLISH"):
        self.lang = lang
        
    @property
    def available_loggers(self):
        return loggers

    @staticmethod
    def _get_phrase(level: str, index: int, lang: str = "ENGLISH") -> str:
        "Retorna la frase del indice del nivel e idioma pasado."
        if not lang in AVAILABLE_LANGS:
            raise KeyError(f"{lang!r} is not a valid language")
        return langs[lang.upper()][level.lower()][index]

    @staticmethod
    def phrase(p: str, logger: list[str]):
        assert logger in loggers.values(), "That logger is not in loggers dictionary"
        return f"\n{logger[0]+logger[1]}{logger[2]+p+_Col.reset}"

    #TODO: //////////////////////////////////   ADD METHODS  ////////////////////////////////
    
    def change_logger(self, logname: str, new: list[str]) -> None:
        if not logname in loggers:
            raise ValueError("That logger is not in the dictionary logger")
        self.new_logger(logname, new)
    
    def new_logger(self, logname: str, build: list[str]) -> None:
        """Crea un nuevo logger dentro del diccionario loggers si no existe.
        
        ## Parametros:
        - logname: El nombre del logger
        - build: Lista que debe contener el color de prefijo, el logger, y el color final        
        """
        assert isinstance(logname, str), "@logname must be a valid string!"
        assert isinstance(build, list) and len(build) == 3, "Invalid build. @build is major than 3 elems or @build is not a list"

        if logname in loggers:
            raise ValueError("That logger already exists in the loggers dictionary")
        elif not isinstance(build[0], list) and not build[0].startswith("\\x"):
            raise ValueError("The fisrt parameter must be a ascii color code")
        elif build[1] in loggers.values():
            raise ValueError("The logger is registred in the logger dictionary with another logger name")
        elif build[1].count("[") < 1 or build[1].count("]") < 1:
            raise Exception("The logger clausure must be a open-closed brackets to be a logger!")
        loggers[logname] = build
    
    def delete_logger(self, logname: str) -> None:
        assert isinstance(logname, str), "@logname must be a valid string!"
        del loggers[logname]

    
    #TODO: //////////////////////////////////   LOGGERS  ////////////////////////////////
    #* Podria hacer un solo metodo que tambien pase el tipo de frase en vez de repetir, pero quiero que puedas acceder como si de un logger se tratara
    #* Logger.error(<index>) en vez de Logger.logger("errors", 1)

    def error(self, index: int) -> str:
        return self.logger("errors", index, loggers["errors"])
        
    def question(self, index: int) -> str:
        return self.logger("game", index, loggers["question"])
    
    def victory(self, index: int) -> str:
        "Se devuelve un mensaje logger con un mensaje de victoria"
        return self.logger("game", index, loggers["victory"])
    
    def message(self, index: int):
        return self.logger("game", index, loggers["message"])

    def runtime(self, index: int) -> str:
        "Se devuelve un mensaje logger con un mensaje relacionado con el flujo del juego"
        return self.logger("runtime", index, loggers["runtime"])

    def logger(self, level: str, index: int, logger: list[str]) -> str:
        assert isinstance(level, str), "This is not a valid level!"
        assert isinstance(index, int), "Index must be a integer!!"
        if not logger in loggers.values():
            raise TypeError("@logger param must be a valid logger type.")
        return f"\n{logger[0]+logger[1]}{logger[2]+self._get_phrase(level, index, self.lang)+_Col.reset}"

    ...


if __name__ == "__main__":
    r = Logger()
    print(r.logger("errors", 0, loggers["victory"]))

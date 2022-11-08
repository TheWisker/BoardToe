"Static private module that contains all the available languages"

__all__ = ["langs", "AVAILABLE_LANGS"]

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
    "ENGLISH": {
            "errors": [
                "Coordinates must be numbers!", 
                "The coordinates must be between 1 and {}", 
                "Oops! That position is already occupied (Position: {})", 
                "Oops! There's already a token in this position!" 
            ],
            "runtime": [
                "The game has been forcibly terminated." 
            ],
            "game": [
                "In which language do you wish to play?", 
                "Your language is {}, correct?",
                "{} has won the game!", 
                "Place the coordinate {}"
            ],
            "cache": []
        },
    "GERMAN": {
            "errors": [
                "Koordinaten müssen Zahlen sein!", 
                "Die Koordinaten müssen zwischen 1 und {} liegen", 
                "Ups! Diese Position ist bereits besetzt (Position: {})", 
                "Hoppla! An dieser Position befindet sich bereits ein Token!" 
            ],
            "runtime": [
                "Das Spiel wurde gewaltsam beendet." 
            ],
            "game": [
                "In welcher Sprache möchten Sie spielen?", 
                "Ihre Sprache ist {}, richtig?",
                "{} hat das Spiel gewonnen!", 
                "Platziere die Koordinate {}"
            ],
            "cache": []
        },
    "ITALIAN": {
            "errors": [
                "Le coordinate devono essere numeri!", 
                "Le coordinate devono essere comprese tra 1 e {}", 
                "Oops! Quella posizione è già occupata (posizione: {})", 
                "Ops! C'è già un token in questa posizione!",
            ],
            "runtime": [
                "Il gioco è stato forzatamente terminato"
            ],
            "game": [
                "In quale lingua desideri giocare?", 
                "La tua lingua è {}, giusto?",
                "{} ha vinto la partita!", 
                "Posiziona la coordinata {}"
            ],
            "cache": []
        },
    "RUSSIAN": {
            "errors": [
                "Координаты должны быть числами!", 
                "Координаты должны быть между 1 и {}", 
                "Упс! Эта позиция уже занята (Позиция: {})", 
                "Упс! В этой позиции уже есть маркер!"
            ],
            "runtime": [
                "Игра была принудительно прекращена"
            ],
            "game": [
                "На каком языке вы хотите играть?", 
                "Ваш язык - {}, верно?",
                "{} выиграл игру!", 
                "Поместите координату {}"
            ],
            "cache": []
        },
    "FRENCH" : {
            "errors" : [
                "Les coordonnées doivent être des nombres !", 
                "Les coordonnées doivent être comprises entre 1 et {}", 
                "Oups ! Cette position est déjà occupée (Position : {})", 
                "Oups ! Il y a déjà un jeton à cette position !" 
            ],
            "runtime" : [
                "Le jeu a été interrompu de force." 
            ],
            "game" : [
                "Dans quelle langue voulez-vous jouer ?", 
                "Votre langue est {}, correct ?",
                "{} a gagné la partie !", 
                "Placez la coordonnée {}"
            ],
            "cache" : []
        },
    "PORTUGUESE": {
            "errors": [
                "As coordenadas devem ser números!", 
                "As coordenadas têm de ser entre 1 e {}", 
                "Oops! Essa posição já está ocupada (Posição: {})", 
                "Oops! Já há uma ficha nesta posição"
            ],
            "runtime": [
                "O jogo foi terminado à força"
            ],
            "game": [
                "Em que língua deseja jogar?", 
                "A sua língua é {}, correcto?",
                "{} ganhou o jogo!", 
                "Coloque a coordenada {}", "Coloque a coordenada {}", "Coloque a coordenada {}"
            ],
            "cache": []
        },
    "JAPANESE": {
            "errors": [
                "座標は数字でなければなりません！", 
                "座標は1以上{}以下でなければなりません", 
                "おっと! その位置はすでに占有されています (位置: {})", 
                "おっと! この位置にはすでにトークンがいます！" 
            ],
            "runtime": [
                "ゲームは強制終了されました。" 
            ],
            "game": [
                "どの言語でプレイしますか？", 
                "あなたの言語は{}ですね?",
                "{}がゲームに勝ちました！", 
                "座標{}を配置します"
            ],
            "cache": []
        },
    "CHINESSE": {
            "errors": [
                "坐标必须是数字！"
                "坐标必须在1和{}之间"
                "哎呀! 该位置已被占用（位置：{}）"
                "哎呀! 这个位置上已经有一个代币了！" 
            ],
            "runtime": [
                "游戏已被强行终止。" 
            ],
            "game": [
                "你希望用哪种语言游戏？"
                "你的语言是{}，对吗？"
                "{}已经赢得了游戏！"
                "放置坐标{}"
            ],
            "cache": []
        },
    }

AVAILABLE_LANGS = list(langs.keys())
    


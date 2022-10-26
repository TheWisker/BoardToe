from constructor import *

class Bot:

    def __init__(self, player: bool, difficulty: str) -> None:
        
        self.player = 5

    def _get_cases(board: list[int], player: int) -> list[int]: #get all posible cases filtered by a parameter for the two players
        
        
        
        # Get posible moves, and set their levels, use methods in matrix class
        return 2
    
   

  
    def get_move(self, board) -> list[int]: # get next move
        bot_cases: list[int] = self._get_cases(board, 0)
        plr_cases: list[int] = self._get_cases(board, 1)
        #vi = _enemy_cases(board)
        #vi = _enemy_cases(board)
        return [2,2]

 






 
    #def restart(): #restart the bot but could not be necesary if we just delete and create a new instance
     #   ...


    # def _get_value(): #get value for a case scenario
    #     ...
    # def _maximin():
    #     ...
    # def _minimax():
    #     ...

    # def _add_cache(): #add cache to better process the current match and options
    #     ...
    


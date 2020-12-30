import chess


class AbstractEngine:
    # chess.color where white = True, black = False
    def __init__(self, color: chess.Color):
        self.color: chess.Color = color

    # returns chess.move
    def get_move(self, current_board: chess.Board) -> chess.Move:
        print("ERROR: Function not overriden in child class")
    
    # since the automated bots won't be able to handle an invalid move, just raise an exception
    def on_invalid_move(self, board, move):
        raise Exception("Your engine made an invalid move... exiting", move)
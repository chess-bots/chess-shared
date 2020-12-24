import chess


class AbstractEngine:
    # chess.color where white = True, black = False
    def __init__(self, color: chess.Color):
        self.color: chess.Color = color

    # returns chess.move
    def get_move(self, current_board: chess.Board) -> chess.Move:
        print("ERROR: Function not overriden in child class")

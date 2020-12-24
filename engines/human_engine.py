from abstract_engine import AbstractEngine
from chess import Board, Move


# Example implementation
class HumanEngine(AbstractEngine):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, current_board):
        legal_moves = current_board.legal_moves

        while True:
            string_move = input("Enter move:").lower()

            move = Move.from_uci(string_move)
            if move in legal_moves:
                return move

            print("\nIllegal move. Example move: a1b1\n")

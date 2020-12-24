from engines.abstract_engine import AbstractEngine
from chess import Board, Move


# Example implementation
def check_string(string_move):
    if len(string_move) < 4 or len(string_move) > 5:
        return False

    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ints = [1, 2, 3, 4, 5, 6, 7, 8]

    if string_move[0] not in chars or string_move[2] not in chars:
        return False
    if string_move[1] not in ints or string_move[3] not in ints:
        return False

    if len(string_move == 4):
        return True

    pieces = ['q', 'r', 'b', 'n']
    if string_move[4] not in pieces:
        return False
    else:
        return True


class HumanEngine(AbstractEngine):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, current_board):
        legal_moves = current_board.legal_moves

        while True:
            string_move = input("Enter move:").lower()

            if check_string(string_move):
                print("\nWrong string length - illegal move\n")
                continue

            move = Move.from_uci(string_move)
            if move in legal_moves:
                return move

            print("\nIllegal move. Example move: a1b1\n")

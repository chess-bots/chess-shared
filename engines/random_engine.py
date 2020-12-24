from engines.abstract_engine import AbstractEngine
import chess
import random


class RandomEngine(AbstractEngine):
    """
    Makes a random legal move
    """

    def get_move(self, board: chess.Board):
        return random.choice(list(board.legal_moves))

from engines.abstract_engine import AbstractEngine
import chess
import random


class RandomEngine(AbstractEngine):
    """
    Makes a random legal move
    """

    def __init__(self, color, seed=0):
        random.seed(0)

        super().__init__(color)

    def get_move(self, board: chess.Board):
        return random.choice(list(board.legal_moves))

from engines.random_engine import RandomEngine
from chess_engine import ChessEngine
import chess
import time

from datetime import datetime

if __name__ == "__main__":
    white = RandomEngine(chess.WHITE, seed=datetime.now())
    black = RandomEngine(chess.BLACK, seed=datetime.now())
    c = ChessEngine(white, black)
    c.run()

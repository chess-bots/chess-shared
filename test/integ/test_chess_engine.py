from engines.random_engine import RandomEngine
from chess_engine import ChessEngine
import chess

if __name__ == "__main__":
    white = RandomEngine(chess.WHITE)
    black = RandomEngine(chess.BLACK)
    c = ChessEngine(white, black)
    c.run()

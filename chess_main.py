# import engines here

import chess
from chess_engine import ChessEngine
from engines.human_engine import HumanEngine
from engines.random_engine import RandomEngine
from simple_engine import SimpleEngine


def main():
    white_engine = RandomEngine(chess.WHITE)
    black_engine = SimpleEngine(chess.BLACK)

    c = ChessEngine(white_engine, black_engine, True)
    c.run()


if __name__ == '__main__':
    main()

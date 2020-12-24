# import engines here

import chess
from chess_engine import ChessEngine
from engines.human_engine import HumanEngine
from engines.random_engine import RandomEngine
#from simple_engine import SimpleEngine


def main():
    white_engine = HumanEngine(chess.WHITE)
    black_engine = RandomEngine(chess.BLACK)

    c = ChessEngine(white_engine, black_engine)
    c.run()


if __name__ == '__main__':
    main()

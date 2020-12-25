# import engines here

import chess
from chess_engine import ChessEngine
from engines.human_engine import HumanEngine
from engines.random_engine import RandomEngine
from simple_engine import SimpleEngine


def main():
    white_engine = SimpleEngine(chess.WHITE, depth=3)
    black_engine = SimpleEngine(chess.BLACK, depth=2)

    c = ChessEngine(white_engine, black_engine, svg_graphics=True, min_display_time=4)
    c.run()


if __name__ == '__main__':
    main()

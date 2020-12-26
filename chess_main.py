# import engines here

import chess
from chess_engine import ChessEngine
from engines.human_engine import HumanEngine
from engines.random_engine import RandomEngine
from simple_engine import SimpleEngine
from engines.stockfish_engine import StockfishEngine, STOCKFISH_BENNETT_PATH, STOCKFISH_JUSTIN_PATH


def main():
    white_engine = SimpleEngine(chess.WHITE, depth=1)
    black_engine = StockfishEngine(False, 1.0, path=STOCKFISH_BENNETT_PATH)

    c = ChessEngine(white_engine, black_engine, svg_graphics=True, min_display_time=-1)
    c.run()


if __name__ == '__main__':
    main()

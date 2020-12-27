# import engines here

import chess
from chess_engine import ChessEngine
from engines.human_engine import HumanEngine
from engines.random_engine import RandomEngine
from engines.stockfish_engine import StockfishEngine, STOCKFISH_BENNETT_PATH, STOCKFISH_JUSTIN_PATH

import time as t

import argparse

def display_svg(svg):
    file_name = "temp.svg"

    f = open(file_name, "w")
    f.write(svg)
    f.close()

    os.system("start " + file_name)


def main(args):
    white_engine = RandomEngine(chess.WHITE)
    black_engine = RandomEngine(chess.BLACK)

    c = ChessEngine(white_engine, black_engine)

    while c.run_iter():
        if args.svg_graphics:
            display_svg(svg_renderer(self.board, lastmove=move))

        if args.cli_graphics:
            print(self.board, "\n")
        
        if args.min_display_time > 0:
            # time is a float, units are seconds
            toc = t.time()
            diff = toc - tic
            if diff < self.min_display_time:
                t.sleep(self.min_display_time - diff)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Chess Main Application')
    parser.add_argument('--svg_graphics', default=False)
    parser.add_argument('--cli_graphics', default=False)
    parser.add_argument('--min_display_time', default=-1)

    args = parser.parse_args()

    main(args)

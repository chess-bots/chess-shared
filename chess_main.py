# import engines here

import chess
from chess_engine import ChessEngine
from engines.human_engine import HumanEngine
from engines.random_engine import RandomEngine
from engines.stockfish_engine import StockfishEngine, STOCKFISH_BENNETT_PATH, STOCKFISH_JUSTIN_PATH

import time as t
from distutils.util import strtobool
from chess.svg import board as svg_renderer
import argparse
import os

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
        tic = t.time()
        if args.svg_graphics:
            display_svg(svg_renderer(c.board, lastmove=c.board.peek()))

        if args.cli_graphics:
            print(c.board, "\n")
        
        if args.min_display_time > 0:
            # time is a float, units are seconds
            toc = t.time()
            diff = toc - tic
            if diff < args.min_display_time:
                t.sleep(args.min_display_time - diff)



# cli_graphics enables printing of boardstate in the console
# svg_graphics enables svg display in your default app for displaying SVGs (web browsers work well, I use MS Edge)
# min_display_time will delay after a move is made to ensure a minimum duration for the turn
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Chess Main Application')
    parser.add_argument('--svg_graphics', default=False, type=strtobool)
    parser.add_argument('--cli_graphics', default=False, type=strtobool)
    parser.add_argument('--min_display_time', default=-1, type=int)

    args = parser.parse_args()

    main(args)

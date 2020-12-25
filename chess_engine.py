import chess
from chess.svg import board as svg_renderer
import os
import time as t


# import engines here


def display_svg(svg):
    file_name = "temp.svg"

    f = open(file_name, "w")
    f.write(svg)
    f.close()

    os.system("start " + file_name)


class ChessEngine:

    # cli_graphics enables printing of boardstate in the console
    # svg_graphics enables svg display in your default app for displaying SVGs (web browsers work well, I use MS Edge)
    # min_display_time will delay after a move is made to ensure a minimum duration for the turn
    def __init__(self, white_engine, black_engine, cli_graphics=False, svg_graphics=False, min_display_time=-1.0):
        self.white_engine = white_engine
        self.black_engine = black_engine
        self.cli_graphics = cli_graphics
        self.svg_graphics = svg_graphics
        self.board = chess.Board()
        self.min_display_time = float(min_display_time)

        if self.cli_graphics:
            print(self.board, "\n")

        if self.svg_graphics:
            display_svg(svg_renderer(self.board))

    def run(self):
        while True:
            tic = t.time()

            current_engine = None
            if self.board.turn == chess.WHITE:
                current_engine = self.white_engine
            if self.board.turn == chess.BLACK:
                current_engine = self.black_engine

            move = current_engine.get_move(self.board.copy())

            if self.min_display_time > 0:
                # time is a float, units are seconds
                toc = t.time()
                diff = toc - tic
                if diff < self.min_display_time:
                    t.sleep(self.min_display_time - diff)

            self.board.push(move)

            if self.svg_graphics:
                display_svg(svg_renderer(self.board, lastmove=move))

            if self.cli_graphics:
                print(self.board, "\n")

            if self.board.is_game_over():
                if self.board.result() == "1/2-1/2":
                    print("Game ended in draw")
                if self.board.result() == "1-0":
                    print("White won the game")
                if self.board.result() == "0-1":
                    print("Black won the game")
                break

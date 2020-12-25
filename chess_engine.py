import chess
from chess.svg import board as svg_renderer
import os


# import engines here


def display_svg(svg):
    file_name = "temp.svg"

    f = open(file_name, "w")
    f.write(svg)
    f.close()

    os.system("start " + file_name)


class ChessEngine:
    def __init__(self, white_engine, black_engine, cli_graphics=False, svg_graphics=False):
        self.white_engine = white_engine
        self.black_engine = black_engine
        self.cli_graphics = cli_graphics
        self.svg_graphics = svg_graphics
        self.board = chess.Board()

        if self.cli_graphics:
            print(self.board, "\n")

        if self.svg_graphics:
            display_svg(svg_renderer(self.board))

    def run(self):
        while True:
            current_engine = None
            if self.board.turn == chess.WHITE:
                current_engine = self.white_engine
            if self.board.turn == chess.BLACK:
                current_engine = self.black_engine

            move = current_engine.get_move(self.board.copy())
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

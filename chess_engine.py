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
    def __init__(self, white_engine, black_engine):
        self.white_engine = white_engine
        self.black_engine = black_engine
        self.board = chess.Board()

    def run_iter(self):
        tic = t.time()

        current_engine = None
        if self.board.turn == chess.WHITE:
            current_engine = self.white_engine
        if self.board.turn == chess.BLACK:
            current_engine = self.black_engine

        while True:
            move = current_engine.get_move(self.board.copy())

            if move in list(self.board.legal_moves):
                break
            else:
                current_engine.on_invalid_move(self.board, move)    
        
        self.board.push(move)

        if self.board.is_game_over():
            if self.board.result() == "1/2-1/2":
                print("Game ended in draw")
            if self.board.result() == "1-0":
                print("White won the game")
            if self.board.result() == "0-1":
                print("Black won the game")
            return False
        
        return True
    
    def run():
        while self.run_iter():
            pass
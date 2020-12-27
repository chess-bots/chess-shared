from engines.abstract_engine import AbstractEngine
from chess import Board, Move
import chess
import time
from functools import partial

class GUIEngine(AbstractEngine):
    def __init__(self, color, app, socketio):
        super().__init__(color)

        self.board = None

        self.socketio = socketio
        self.socketio.on_event("send_move", self.on_send_move)
        self.socketio.on_event("legal_moves", self.on_legal_moves)

        self.new_move = None
    
    def on_send_move(self, data):
        try:
            self.new_move = Move.from_uci(data["source"] + data["target"])
        except Exception as e:
            print("Error: invalid move!")
            self.new_move = None
    
    def on_legal_moves(self, data):
        legal_moves = list(self.board.legal_moves)

        moves_for_square = list(filter(lambda x: x.from_square == chess.parse_square(data["square"]), legal_moves))

        return {
            "square": data["square"],
            "moves": [x.uci() for x in moves_for_square]
        }

    def get_move(self, current_board):
        print("waiting for move from GUI")
        self.board = current_board

        while True:
            if self.new_move is not None:
                move = self.new_move
                self.new_move = None
                return move
            self.socketio.sleep(0.1)

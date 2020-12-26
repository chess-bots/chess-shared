from engines.abstract_engine import AbstractEngine
from chess import Board, Move
import time

class GUIEngine(AbstractEngine):
    def __init__(self, color, socketio):
        super().__init__(color)

        socketio.on_event("send_move", self.on_send_move)

        self.new_move = None
    
    def on_send_move(self, data):
        try:
            self.new_move = Move.from_uci(data["source"] + data["target"])
        except Exception as e:
            print("Error: invalid move!")
            self.new_move = None

    def get_move(self, current_board):
        legal_moves = current_board.legal_moves

        while True:
            if self.new_move is not None:
                move = self.new_move
                self.new_move = None
                return move
            time.sleep(0.1)
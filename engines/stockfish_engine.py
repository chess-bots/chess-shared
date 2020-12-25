import chess

from engines.abstract_engine import AbstractEngine

class StockfishEngine(AbstractEngine):
    def __init__(self, color, think_time = 5.0):
        super().__init__(color)
        self.engine = chess.engine.SimpleEngine.popen_uci("/var/run/stockfish/stockfish_10_x64")
        self.think_time = think_time
        
    def get_move(self, board: chess.Board):
        return self.engine.play(board, limit=chess.engine.Limit(self.think_time)).move
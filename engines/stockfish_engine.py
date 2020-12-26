import chess
import chess.engine as chess_engine
from engines.abstract_engine import AbstractEngine

STOCKFISH_JUSTIN_PATH = "/var/run/stockfish/stockfish_10_x64"
STOCKFISH_BENNETT_PATH = "C:\Code\Personal\Chess\stockfish\stockfish_12.exe"


class StockfishEngine(AbstractEngine):
    def __init__(self, color, think_time=5.0, path=STOCKFISH_JUSTIN_PATH):
        super().__init__(color)
        self.engine = chess_engine.SimpleEngine.popen_uci(path)
        self.think_time = think_time

    def get_move(self, board: chess.Board):
        return self.engine.play(board, limit=chess.engine.Limit(self.think_time)).move

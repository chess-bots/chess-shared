import chess
import chess.engine as chess_engine
from engines.abstract_engine import AbstractEngine

STOCKFISH_JUSTIN_PATH = "/var/run/stockfish/stockfish_12"
STOCKFISH_BENNETT_PATH = "C:\Code\Personal\Chess\stockfish\stockfish_12.exe"


class StockfishEngine(AbstractEngine):
    """
    Skill level is 1-7
    """
    def __init__(self, color, think_time = 10, elo = None, path=STOCKFISH_JUSTIN_PATH):
        super().__init__(color)
        self.engine = chess_engine.SimpleEngine.popen_uci(path)
        self.think_time = think_time
        self.elo = elo

    def get_move(self, board: chess.Board):
        return self.engine.play(board, limit=chess.engine.Limit(self.think_time), options={
            "UCI_LimitStrength": True if self.elo is not None else False,
            "UCI_Elo": self.elo
        }).move

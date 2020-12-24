import chess
# import engines here


class ChessEngine:
    def __init__(self, white_engine, black_engine):
        self.white_engine = white_engine
        self.black_engine = black_engine
        self.board = chess.Board()

    def run(self):
        while True:
            current_engine = None
            if self.board.turn == chess.WHITE:
                current_engine = self.white_engine
            if self.board.turn == chess.BLACK:
                current_engine = self.black_engine

            move = current_engine.get_move(self.board)
            self.board.push(move)

            if self.board.is_game_over():
                print("game is over")
                break

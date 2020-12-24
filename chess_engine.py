import chess


# import engines here


class ChessEngine:
    def __init__(self, white_engine, black_engine, show_moves=False):
        self.white_engine = white_engine
        self.black_engine = black_engine
        self.show_moves = show_moves
        self.board = chess.Board()

        if self.show_moves:
            print(self.board, "\n")

    def run(self):
        while True:
            current_engine = None
            if self.board.turn == chess.WHITE:
                current_engine = self.white_engine
            if self.board.turn == chess.BLACK:
                current_engine = self.black_engine

            move = current_engine.get_move(self.board)
            self.board.push(move)

            if self.show_moves:
                print(self.board, "\n")

            if self.board.is_game_over():
                if self.board.result() == "1/2-1/2":
                    print("Game ended in draw")
                if self.board.result() == "1-0":
                    print("White won the game")
                if self.board.result() == "0-1":
                    print("Black won the game")
                break

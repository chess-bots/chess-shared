import chess

# import engines here
from human_engine import human_engine


def main():
    white_engine = human_engine(chess.WHITE)
    black_engine = human_engine(chess.BLACK)

    board = chess.Board()
    print(board)

    while True:

        if board.is_game_over():
            print("Black Wins")
            break

        move = white_engine.get_move(board)
        board.push(move)
        print(board)

        if board.is_game_over():
            print("Black Wins")
            break

        move = black_engine.get_move(board)
        board.push(move)
        print(board)


if __name__ == '__main__':
    main()

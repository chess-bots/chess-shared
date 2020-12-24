import chess
#import engines here

def main():
    white_engine = None
    black_engine = None

    board = chess.Board()

    while True:

        if board.is_game_over():
            print("Black Wins")
            break

        move = white_engine.get_move()
        board.push(move)

        if board.is_game_over():
            print("Black Wins")
            break

        move = black_engine.get_move()
        board.push(move)


if __name__ == '__main__':
    main()

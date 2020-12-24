# import engines here

from chess_engine import ChessEngine


def main():
    white_engine = None
    black_engine = None

    c = ChessEngine(white_engine, black_engine)

    c.run()


if __name__ == '__main__':
    main()

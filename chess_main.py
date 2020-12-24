import chess
# import engines here

from engines import ChessEngine


def main():
    white_engine = None
    black_engine = None

    c = ChessEngine(white_engine, black_engine)

    c.run()


if __name__ == '__main__':
    main()

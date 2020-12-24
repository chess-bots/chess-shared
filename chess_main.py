# import engines here
from camden_engine import CamdenEngine

from chess_engine import ChessEngine


def main():
    white_engine = CamdenEngine(True)
    black_engine = CamdenEngine(False)

    c = ChessEngine(white_engine, black_engine, True)

    c.run()


if __name__ == '__main__':
    main()

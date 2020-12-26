from flask import Flask, render_template

from chess_engine import ChessEngine
from engines.random_engine import RandomEngine
#from engines.socket_engine import SocketEngine
from chess.svg import board as svg_renderer
import chess

from engine import Engine as JustinEngine

from flask_socketio import SocketIO

import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['TEMPLATES_AUTO_RELOAD'] = True
socketio = SocketIO(app)

white_engine = RandomEngine(chess.WHITE)
black_engine = JustinEngine(chess.BLACK)

chess_engine = ChessEngine(white_engine, black_engine, min_display_time=1)

def board_update_callback():
    socketio.emit("board_fen", chess_engine.board.fen())

def chess_worker():
    chess_engine.run(board_update_callback)

chess_thread = threading.Thread(target=chess_worker)

chess_thread.start()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/board.svg')
def board_svg():
    return svg_renderer(chess_engine.board)


if __name__ == '__main__':
    socketio.run(app)
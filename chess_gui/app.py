

from flask import Flask, render_template

from chess_engine import ChessEngine
from engines.random_engine import RandomEngine
from engines.gui_engine import GUIEngine
from engines.stockfish_engine import StockfishEngine, STOCKFISH_JUSTIN_PATH
from chess.svg import board as svg_renderer
import chess
from engine import Engine as JustinEngine

from flask_socketio import SocketIO

import threading


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['TEMPLATES_AUTO_RELOAD'] = True
socketio = SocketIO(app, cors_allowed_origins="*")

white_engine = JustinEngine(chess.WHITE)
black_engine = StockfishEngine(chess.BLACK, think_time=1, path=STOCKFISH_JUSTIN_PATH)

chess_engine = ChessEngine(white_engine, black_engine)

def send_board_state():
    socketio.emit("game_state", {
        "fen": chess_engine.board.fen(),
        "turn": "white" if chess_engine.board.turn else "black"
    })

GAME_OVER = False
GAME_RUNNING = False

def background_task():
    global GAME_OVER
    global GAME_RUNNING
    while True:
        send_board_state()
        socketio.sleep(1)

        if not chess_engine.run_iter():
            print("game is finished... exiting")
            GAME_RUNNING = False
            GAME_OVER = True
            break

@socketio.on("connect")
def on_connect():
    global GAME_OVER
    global GAME_RUNNING
    send_board_state()
    if not GAME_RUNNING and not GAME_OVER:
        GAME_RUNNING = True
        socketio.start_background_task(background_task)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/white')
def white_player():
    return render_template('player.html', color="white")

@app.route('/black')
def black_player():
    return render_template('player.html', color="black")


@app.route('/board.svg')
def board_svg():
    return svg_renderer(chess_engine.board)

if __name__ == '__main__':
    socketio.run(app, debug=True)
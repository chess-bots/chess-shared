

from flask import Flask, render_template

from chess_engine import ChessEngine
from engines.random_engine import RandomEngine
from engines.gui_engine import GUIEngine
from chess.svg import board as svg_renderer
import chess
from engine import Engine as JustinEngine

from flask_socketio import SocketIO

import threading


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['TEMPLATES_AUTO_RELOAD'] = True
socketio = SocketIO(app, cors_allowed_origins="*")

white_engine = RandomEngine(chess.WHITE)
black_engine = GUIEngine(chess.BLACK, app, socketio)

chess_engine = ChessEngine(white_engine, black_engine)

def send_board_state():
    socketio.emit("game_state", {
        "fen": chess_engine.board.fen()
    })

def background_task():
    while chess_engine.run_iter():
        send_board_state()
        socketio.sleep(1)

@socketio.on("connect")
def on_connect():
    send_board_state()
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
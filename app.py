from flask import Flask, request, redirect, session, render_template
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/')
def root():
    session["board"] = boggle_game.make_board()
    board = session["board"]
    return render_template('board.html',
                            board=board)

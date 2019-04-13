from flask import Flask, request, redirect, session, render_template, jsonify
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"


@app.route('/')
def root():
    global boggle_game
    boggle_game = Boggle()
    session["board"] = boggle_game.make_board()
    board = session["board"]
    return render_template('board.html', board=board)


@app.route('/answer', methods=["POST"])
def answer_handling():
    data = request.form['answer']
    result = boggle_game.check_valid_word(board=session["board"] , word=data)
    server_response = jsonify({'result': result, 'word': data})
    return server_response


@app.route('/new_game', methods=["POST"])
def user_handling():
    final = int(request.form['high'])
    print('**************')
    print(final)
    if session.get('user'):
        temp = session['user'].games
        temp += 1
        session['user'].games = temp
        if session['user'].high < final:
            session['user'].high = final
    else:
        session['user'] = {'high': final, 'games': 1}
    session['user'] = session['user']
    return redirect('/')

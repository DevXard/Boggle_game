from boggle import Boggle
from flask import Flask, render_template,session, request, jsonify

boggle_game = Boggle()
app = Flask(__name__)

app.config["SECRET_KEY"] = 'r23yg3geg456ges'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game_board')
def game():
    board = boggle_game.make_board()
    session['board'] = board
    best_score = session.get('best_score', 0)
    times_played = session.get('times_played', 0)
    return render_template('board.html', board=board, best_score=best_score, times_played=times_played)

@app.route('/check-awncer')
def check_awncer():
    word = request.args['guess']
    board = session['board']
    res = boggle_game.check_valid_word(board, word)
    return jsonify({'response': res})

@app.route('/get-scores', methods=['POST'])
def get_scores():

    score = request.json['score']
    hightscore = session.get('best_score', 0)
    times_played = session.get('times_played', 0)

    session['times_played'] = times_played + 1
    session['best_score'] = max(score, hightscore)
    return 'success'
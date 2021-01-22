from questions import questions_database
from quiz import parties_scores, VoteEnum

import random

from flask_socketio import SocketIO, emit
from flask_session import Session
from flask import Flask, render_template, request, session, url_for, redirect


app = Flask(__name__)
app.secret_key = 'add-yours'

# socket io
sio = SocketIO(app, async_mode='eventlet', manage_session=False, cors_allowed_origins='*')

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


party_colors = {
    "יהדות התורה": "#082970",
    "הליכוד": "#195AA6",
    "מרצ": "#40B339",
    "ישראל ביתנו": "#001B6C",
    "הבית היהודי": "#006088",
    "הרשימה המשותפת": "#000000",
    "יש עתיד": "#003DA5",
    "שס": "#000000",
    "כחול לבן": "#115FA4",
    "העבודה": "#003264",
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game')
def game():
    session['counter'] = 1
    session['scores'] = parties_scores
    session['question_answered'] = {}
    q = random.choice(questions_database)
    session['question'] = q
    return render_template('game.html', question=q.content)


@app.route('/party')
def party():
    if not session.get('win'):
        return redirect(url_for('index'))
    answers = {}
    for q in session['question_answered'].keys():
        answers[q.content] = q.parties[session['win']]

    return render_template('party.html', VoteEnum=VoteEnum, color=party_colors[session['win']], party=session['win'], question_dict=answers)


@sio.on('answer')
def on_answer(data):
    if session['counter'] <= 9:
        q = session['question']
        q.show_question(data['button'], session['scores'])

        session['question_answered'][q] = ''

        new_q = random.choice(questions_database)
        session['question'] = new_q

        session['counter'] += 1
        emit('new_question', {'content': new_q.content, 'counter': session['counter']})
    else:
        session['win'] = choose_winner(session['scores'])
        emit("redirect", {'url': url_for('party')})


@sio.on('error')
def on_error(data):
    raise(data['content'])


def choose_winner(scores):
    max = 0
    maxers = []

    for party, score in scores.items():
        if score > max:
            max = score

    for party, score in scores.items():
        if score == max:
            maxers.append(party)

    return random.choice(maxers)


sio.run(app, debug=False, use_reloader=True, port=8080, host="0.0.0.0")

from flask import Flask, escape, request, jsonify, render_template, send_from_directory
import sys
import os
import random
sys.path.append('./model/')
from model import get_speeches, get_persons, speeches_of, db
from repeater import repeater_say

app = Flask(__name__)
staic_folder = './static'
app.config.from_pyfile('settings.cfg')
db_ses = db(app.config)
@app.route('/')
@app.route('/dashboard.html')
def index():
    return send_from_directory(staic_folder, 'dashboard.html')
@app.route('/xinhua_news_piracy_check.html')
def xinhua_news_piracy_check():
    return send_from_directory(staic_folder, 'xinhua_news_piracy_check.html')

@app.route('/clumsy_repeater.html')
def clumsy_repeater():
    return send_from_directory(staic_folder, 'clumsy_repeater.html')

@app.route('/img/nlparade.png')
def logo():
    return send_from_directory(staic_folder+'/assets/img/', 'nlparade.png')

@app.route('/map.html')
def map():
    return send_from_directory(staic_folder, 'user.html')

@app.route('/most_speech_count.html')
def most_speech_count():
    return send_from_directory(staic_folder, 'most_speech_count.html')

@app.route('/speech_count.html')
def speech_count():

    return send_from_directory(staic_folder, 'speech_count.html')

@app.route('/speeches')
def speech():
    speeches = get_speeches(db_ses)
    return jsonify(speeches) 

@app.route('/speech_of_person/')
def speach_of_person():
    name = request.args.get('name', type=str)
    print(name)
    speeches = speeches_of(db_ses, name)
    speech = random.choice(speeches)
    print(speech[0])
    return speech[0]

@app.route('/persons')
def person():
    min_count = request.args.get('min_count', type=int)
    if min_count != None:
        persons = get_persons(db_ses, min_count=min_count)
    else:
        persons = get_persons(db_ses)
    return jsonify(persons)

@app.route('/repeater')
def repeater():
    sentence = request.args.get('sentence', type=str)
    if not sentence:
        return ''
    return repeater_say(sentence);

'''
@app.teardown_appcontext
def session_clear(exception):
    if exception and db_ses.is_active:
        db_ses.rollback()
    else:
        db_ses.commit()

    db_ses.close()
'''
if __name__ == '__main__':
    app.run()

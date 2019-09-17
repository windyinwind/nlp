from flask import Flask, escape, request, jsonify, render_template, send_from_directory
import sys
import os
import random
sys.path.append('./model/')
from model import get_speeches, get_persons, speeches_of

app = Flask(__name__)
staic_folder = './static'
@app.route('/')
@app.route('/dashboard.html')
def index():
    #return render_template('dashboard.html')
    return send_from_directory(staic_folder, 'dashboard.html')

@app.route('/user.html')
def user():
    #return render_template('dashboard.html')
    return send_from_directory(staic_folder, 'user.html')

@app.route('/most_speech_count.html')
def most_speech_count():
    #return render_template('dashboard.html')
    return send_from_directory(staic_folder, 'most_speech_count.html')

@app.route('/speech_count.html')
def speech_count():
    #return render_template('dashboard.html')
    return send_from_directory(staic_folder, 'speech_count.html')

@app.route('/speeches')
def speech():
    speeches = get_speeches()
    return jsonify(speeches) 

@app.route('/speech_of_person/')
def speach_of_person():
    name = request.args.get('name', type=str)
    print(name)
    speeches = speeches_of(name)
    speech = random.choice(speeches)
    return speech[0]

@app.route('/persons')
def person():
    min_count = request.args.get('min_count', type=int)
    if min_count != None:
        persons = get_persons(min_count=min_count)
    else:
        persons = get_persons()
    return jsonify(persons)

if __name__ == '__main__':
    app.run()

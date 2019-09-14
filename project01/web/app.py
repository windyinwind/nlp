from flask import Flask, escape, request, jsonify, render_template, send_from_directory
import sys
import os
sys.path.append('./model/')
from model import get_speeches

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

@app.route('/speeches')
def speech():
    speeches = get_speeches();
    print(speeches)
    return jsonify(speeches) 

if __name__ == '__main__':
    app.run()
from flask import Flask, escape, request
from flask import jsonify
import sys
sys.path.append('./model/')
from model import get_speeches

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/speeches')
def speech():
    speeches = get_speeches();
    print(speeches)
    return jsonify(speeches) 

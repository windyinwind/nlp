from flask import Flask, escape, request
import sys
sys.path.append('../model/')
from model import get_speeches

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/speeches')
def speech():
    return str(get_speeches()[0])
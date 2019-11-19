from flask import Flask, render_template, request, session, abort
from config import Config
import os
import sys

app = Flask(__name__)

app.config.from_object(Config)
app.config['SECRET_KEY'] = '1234'

@app.route('/')
def home():
    return render_template('index.html')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1234'


if __name__ == '__main__':
    app.run(host='192.168.0.133',port=5000,debug=True)

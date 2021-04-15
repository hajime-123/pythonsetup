# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 10:04:59 2021

@author: 18530
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

## おまじない
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000,threaded=True)


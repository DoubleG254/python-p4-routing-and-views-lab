#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f"<h1>{parameter}</h1>"

@app.route('/count/<int:parameter>')
def count(parameter):
    items = ''.join([f"<li>{n}</li>" for n in range(parameter)])
    return f"<ul>{items}</ul>"

@app.route('/math/<int:num1>/<operator>/<int:num2>')
def math(num1,operator,num2):
    if operator=='div':
        ans=num1 / num2
    elif operator == '+':
        ans = num1 + num2
    elif operator == '-':
        ans = num1 - num2
    elif operator =='*':
        ans = num1 * num2
    elif operator == "%":
        ans = num1 % num2
    return f"<h1>{ans}</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)

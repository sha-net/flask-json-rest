from flask import Flask
import sys
import optparse
import time

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world from Docker! v2"

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)

@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

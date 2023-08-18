from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    print("Mi modificación1")
    return '<h1>Mi modificacion</h1>'
    return '<h1>Hello, World!</h1>   software el mejor curso'

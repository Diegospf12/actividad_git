from flask import Flask

from flask import request

 

app = Flask(__name__)

 

@app.route('/')

def hello():
    print("Mi modificación1")
 

    return '<h1>Mi modificacion</h1>'

def multiplicar(var1, var2):
    print(var1 * var2)

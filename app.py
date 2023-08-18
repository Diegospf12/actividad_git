from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    print("Mi modificación1")
    return '<h1>Mi modificacion</h1>'
<<<<<<< HEAD

@app.route('/sumar')
def sumar():
    param1 = float(request.args.get('param1'))
    param2 = float(request.args.get('param2'))
    resultado = param1 + param2
    return f'La suma de {param1} y {param2} es: {resultado}'

@app.route('/multiplicar')
def multiplicar():
    param1 = float(request.args.get('param1'))
    param2 = float(request.args.get('param2'))
    resultado = param1 * param2
    return f'El producto de {param1} y {param2} es: {resultado}'

if __name__ == '__main__':
    app.run()

=======
    return '<h1>Hello, World!</h1>   software el mejor curso'
>>>>>>> a6d852a23e8536d0e4770c305fd346b5ff6db7f3

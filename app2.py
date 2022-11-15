import flask
import os
from flask import Flask

app2 = flask.Flask(__name__)

@app2.route('/')
def pag_inicio_usuario():
    return "<h1>Pagina de inicio del usuario</h1>"


if __name__ == '__main__':
    app2.run(host='0.0.0.0', port=80)


from flask import Flask, render_template, request
import mysql.connector
from funciones import Conectar_BD, empleados, Desconectar_BD

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/consulta', methods=['POST'])
def result():
    user = request.form['user']
    password = request.form['password']
    database = request.form['database']

    db = Conectar_BD(user, password, database)
    registros = empleados(db)
    Desconectar_BD(db)

    return render_template('consulta.html', registros=registros)

if __name__ == '__main__':
    app.run(debug=True)

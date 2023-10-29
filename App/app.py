from flask import Flask, render_template, request
import mysql.connector
from funciones import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/tablas', methods=['POST'])
def result():
    user = request.form['user']
    password = request.form['password']
    database = request.form['database']
    db = Conectar_BD(user, password, database)

    cursor = db.cursor()
    cursor.execute("show tables;")
    tablas = cursor.fetchall()
    cursor.close()

    Desconectar_BD(db)

    return render_template('tablas.html', tablas=tablas, user=user, password=password, database=database)

@app.route('/tabla/<nombre_tabla>')
def mostrar_tabla(nombre_tabla):
    user = request.args.get('user')
    password = request.args.get('password')
    database = request.args.get('database')
    
    db = Conectar_BD(user, password, database)
    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {nombre_tabla};")
    contenido_tabla = cursor.fetchall()
    cursor.close()
    Desconectar_BD(db)

    return render_template('tabla.html', contenido_tabla=contenido_tabla)

if __name__ == '__main__':
    app.run(debug=True)
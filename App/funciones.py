import sys
import mysql.connector

def Conectar_BD(user, password, database):
    try:
        db = mysql.connector.connect(
            host="192.168.122.153",
            user=user,
            password=password,
            database=database
        )
    except mysql.connector.Error as e:
        print("No se pudo conectar a la base de datos:", e)
        sys.exit(1)
    return db


def Desconectar_BD(db):
    db.close()
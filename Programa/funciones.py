import sys
import mysql.connector

def Conectar_BD(host, user, password, database):
    try:
        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    except mysql.connector.Error as e:
        print("No se pudo conectar a la base de datos:", e)
        sys.exit(1)
    return db

def empleados(db):
    sql = "select * from emp"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("A continuación se muestra la tabla de empleados:")
        print("")
        print("EMPNO - ENAME - JOB - MGR - HIREDATE - SAL - COMM - DEPTNO")
        for registro in registros:
            print(registro[0], "-", registro[1], "-", registro[2], "-", registro[3], "-", registro[4], "-", registro[5], "-", registro[6], "-", registro[7])
    except Exception as e:
        print("Se ha producido un error en la consulta:", e)

def Desconectar_BD(db):
    db.close()
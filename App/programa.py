from web.funciones import *

print("¡Bienvenido al programa de base de datos!")
print("")
host = input("Introduce la dirección IP del servidor: ")
user = input("Introduce el nombre de usuario: ")
password = input("Introduce la contraseña: ")
database = input("Introduce el nombre de la base de datos: ")
print("")
print("Conectando a la base de datos...")
db = Conectar_BD(host, user, password, database)
print("Conexión establecida correctamente.\n")
empleados(db)
Desconectar_BD(db)

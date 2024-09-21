import mysql.connector
from mysql.connector import Error


# datos/db.py
class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Cambia a tu usuario de MySQL
            password="",  # Cambia a tu contraseña de MySQL
            database="rol_de_pagos"
        )
        self.cursor = self.connection.cursor()

    # Método para crear usuario (ya existente)
    def crear_usuario(self, ci, nombre, apellido, cargo, fecha_ingreso, sueldo, username, password):
        print(f"Hashed password: {password}")  # Para verificar el valor
        query = "INSERT INTO usuarios (ci, nombre, apellido, cargo, fecha_ingreso, sueldo, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (ci, nombre, apellido, cargo, fecha_ingreso, sueldo, username, password)
        self.cursor.execute(query, values)
        self.connection.commit()


    # Método para obtener usuario por nombre de usuario (ya existente)
    def obtener_usuario_por_username(self, username):
        query = "SELECT * FROM usuarios WHERE username = %s"
        self.cursor.execute(query, (username,))
        user = self.cursor.fetchone()
        if user:
            print(f"Password recuperado de la base de datos: {user[6]}")  # user[6] es la contraseña
        return user


    # Método para editar la información del usuario
    def editar_usuario(self, user_id, nombre, apellido, cargo, sueldo):
        query = "UPDATE usuarios SET nombre = %s, apellido = %s, cargo = %s, sueldo = %s WHERE id = %s"
        values = (nombre, apellido, cargo, sueldo, user_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    # Método para eliminar usuario
    def eliminar_usuario(self, user_id):
        query = "DELETE FROM usuarios WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()

    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexion a la base de datos cerrada.")

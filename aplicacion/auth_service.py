import bcrypt

class AuthService:
    def __init__(self, db):
        self.db = db

    # Método para crear cuenta (ya existente)
    def create_account(self, ci, nombre, apellido, cargo, fecha_ingreso, sueldo, username, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.db.crear_usuario(ci, nombre, apellido, cargo, fecha_ingreso, sueldo, username, hashed_password.decode('utf-8'))

    # Método para iniciar sesión (ya existente)
    def login(self, username, password):
        user = self.db.obtener_usuario_por_username(username)
        if user:
            print(type(user[8]))  # Verifica el tipo de la contraseña almacenada
            if isinstance(user[8], str):
                if bcrypt.checkpw(password.encode('utf-8'), user[8].encode('utf-8')):
                    return user
        return None


    # Método para editar la información del usuario
    def editar_usuario(self, user_id):
        print("\n--- Editar Información del Usuario ---")
        nuevo_nombre = input("Nuevo Nombre: ")
        nuevo_apellido = input("Nuevo Apellido: ")
        nuevo_cargo = input("Nuevo Cargo: ")
        nuevo_sueldo = float(input("Nuevo Sueldo: "))

        self.db.editar_usuario(user_id, nuevo_nombre, nuevo_apellido, nuevo_cargo, nuevo_sueldo)
        print("Información del usuario actualizada con éxito.")

    # Método para eliminar la cuenta del usuario
    def eliminar_usuario(self, user_id):
        confirmacion = input("¿Estás seguro de que quieres eliminar tu cuenta? (s/n): ")
        if confirmacion.lower() == 's':
            self.db.eliminar_usuario(user_id)
            print("Cuenta eliminada con éxito.")
        else:
            print("Cancelado. No se eliminó la cuenta.")

    def close(self):
        self.db.close()

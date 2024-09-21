from db import Database

def create_tables():
    db = Database()

    usuarios_table = '''
    CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ci VARCHAR(10) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    fecha_ingreso DATE NOT NULL,
    sueldo DECIMAL(10, 2) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
    );
    '''

    ingresos_table = '''
    CREATE TABLE IF NOT EXISTS ingresos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        usuario_id INT,
        nombre VARCHAR(100),
        sueldo DECIMAL(10, 2),
        comision DECIMAL(10, 2),
        transporte DECIMAL(10, 2),
        alimentacion DECIMAL(10, 2),
        decimotercer_sueldo DECIMAL(10, 2),
        decimocuarto DECIMAL(10, 2),
        fondos_reserva DECIMAL(10, 2),
        horas_extras DECIMAL(10, 2),
        vacaciones DECIMAL(10, 2),
        total_ingresos DECIMAL(10, 2),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    );
    '''

    egresos_table = '''
    CREATE TABLE IF NOT EXISTS egresos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        usuario_id INT,
        iess_aportes DECIMAL(10, 2),
        prestamos_quirografarios DECIMAL(10, 2),
        prestamos_hipotecarios DECIMAL(10, 2),
        impuestos DECIMAL(10, 2),
        seguro DECIMAL(10, 2),
        multas DECIMAL(10, 2),
        bonos_comisariato DECIMAL(10, 2),
        total_egresos DECIMAL(10, 2),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    );
    '''
    
    db.execute_query(usuarios_table)
    db.execute_query(ingresos_table)
    db.execute_query(egresos_table)
    db.close()

if __name__ == '__main__':
    create_tables()

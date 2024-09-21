from datos.db import Database

class PayrollService:
    def __init__(self):
        self.db = Database()

    def add_ingresos(self, usuario_id, nombre, sueldo, comision, transporte, alimentacion, decimotercer_sueldo, decimocuarto, fondos_reserva, horas_extras, vacaciones):
        total_ingresos = sueldo + comision + transporte + alimentacion + decimotercer_sueldo + decimocuarto + fondos_reserva + horas_extras + vacaciones
        query = '''
        INSERT INTO ingresos (usuario_id, nombre, sueldo, comision, transporte, alimentacion, decimotercer_sueldo, decimocuarto, fondos_reserva, horas_extras, vacaciones, total_ingresos)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        self.db.execute_query(query, (usuario_id, nombre, sueldo, comision, transporte, alimentacion, decimotercer_sueldo, decimocuarto, fondos_reserva, horas_extras, vacaciones, total_ingresos))

    def add_egresos(self, usuario_id, iess_aportes, prestamos_quirografarios, prestamos_hipotecarios, impuestos, seguro, multas, bonos_comisariato):
        total_egresos = iess_aportes + prestamos_quirografarios + prestamos_hipotecarios + impuestos + seguro + multas + bonos_comisariato
        query = '''
        INSERT INTO egresos (usuario_id, iess_aportes, prestamos_quirografarios, prestamos_hipotecarios, impuestos, seguro, multas, bonos_comisariato, total_egresos)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        self.db.execute_query(query, (usuario_id, iess_aportes, prestamos_quirografarios, prestamos_hipotecarios, impuestos, seguro, multas, bonos_comisariato, total_egresos))

    def get_resumen(self, usuario_id):
        query_ingresos = "SELECT total_ingresos FROM ingresos WHERE usuario_id = %s ORDER BY id DESC LIMIT 1"
        query_egresos = "SELECT total_egresos FROM egresos WHERE usuario_id = %s ORDER BY id DESC LIMIT 1"

        total_ingresos = self.db.fetch_all(query_ingresos, (usuario_id,))
        total_egresos = self.db.fetch_all(query_egresos, (usuario_id,))

        if total_ingresos and total_egresos:
            ingresos = total_ingresos[0][0]
            egresos = total_egresos[0][0]
            sueldo_neto = ingresos - egresos
            return {
                'total_ingresos': ingresos,
                'total_egresos': egresos,
                'sueldo_neto': sueldo_neto
            }
        else:
            return None

    def close(self):
        self.db.close()

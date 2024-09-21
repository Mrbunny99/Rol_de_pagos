from aplicacion.auth_service import AuthService
from aplicacion.payroll_service import PayrollService
from datos.db import Database

def main():
    db = Database()
    auth_service = AuthService(db)

    while True:
        print("=== Bienvenido al Sistema de Rol de Pagos ===")
        print("1. Crear cuenta")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ci = input("Ingrese su cédula de identidad: ")
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            cargo = input("Ingrese su cargo: ")
            fecha_ingreso = input("Ingrese su fecha de ingreso (YYYY-MM-DD): ")
            sueldo = float(input("Ingrese su sueldo: "))
            username = input("Ingrese un nombre de usuario: ")
            password = input("Ingrese una contraseña: ")
            auth_service.create_account(ci, nombre, apellido, cargo, fecha_ingreso, sueldo, username, password)
            print("Cuenta creada con éxito.")
        elif opcion == "2":
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            user = auth_service.login(username, password)
            if user:
                user_id = user[0]
                print("Inicio de sesión exitoso.")
                payroll_service = PayrollService()

                while True:
                    print("\n--- Menú Principal ---")
                    print("1. Añadir Ingresos")
                    print("2. Añadir Egresos")
                    print("3. Ver Resumen de Ingresos y Egresos")
                    print("4. Editar informacion del usuario")
                    print("5. Eliminar cuenta")
                    print("6. Cerrar Sesión")
                    opcion_menu = input("Seleccione una opción: ")

                    if opcion_menu == "1":
                        nombre = input("Nombre y Apellido: ")
                        try:
                            sueldo = float(input("Sueldo: "))
                            comision = float(input("Comisión o Bonificación: "))
                            transporte = float(input("Transporte: "))
                            alimentacion = float(input("Alimentación: "))
                            decimotercer_sueldo = float(input("Decimotercer Sueldo: "))
                            decimocuarto = float(input("Decimocuarto Sueldo: "))
                            fondos_reserva = float(input("Fondos de Reserva: "))
                            horas_extras = float(input("Horas Extras: "))
                            vacaciones = float(input("Vacaciones: "))
                        except ValueError:
                            print("Por favor, ingrese valores numéricos válidos.")
                            continue

                        # Aqui se añade los ingresos :)
                        payroll_service.add_ingresos(
                            user[0], nombre, sueldo, comision, transporte, alimentacion,
                            decimotercer_sueldo, decimocuarto, fondos_reserva, horas_extras, vacaciones
                        )
                        print("Datos de ingresos añadidos con éxito.")
                    
                    elif opcion_menu == "2":
                        try:
                            iess_aportes = float(input("IESS Aportes (9.45%): "))
                            prestamos_quirografarios = float(input("Préstamos Quirografarios: "))
                            prestamos_hipotecarios = float(input("Préstamos Hipotecarios: "))
                            impuestos = float(input("Impuestos a la Renta: "))
                            seguro = float(input("Seguro: "))
                            multas = float(input("Multas: "))
                            bonos_comisariato = float(input("Bonos de Comisariato: "))
                        except ValueError:
                            print("Por favor, ingrese valores numéricos válidos.")
                            continue

                        # Aqui se añade los egresos >:(
                        payroll_service.add_egresos(
                            user[0], iess_aportes, prestamos_quirografarios, prestamos_hipotecarios,
                            impuestos, seguro, multas, bonos_comisariato
                        )
                        print("Datos de egresos añadidos con éxito.")
                    
                    elif opcion_menu == "3":
                        resumen = payroll_service.get_resumen(user[0])
                        if resumen:
                            print("\n--- Resumen de Ingresos y Egresos ---")
                            print(f"Total Ingresos: {resumen['total_ingresos']}")
                            print(f"Total Egresos: {resumen['total_egresos']}")
                            print(f"Sueldo Neto: {resumen['sueldo_neto']}")
                        else:
                            print("No hay datos disponibles.")
                    
                    elif opcion_menu == "4":
                        auth_service.editar_usuario(user_id)
                    elif opcion_menu == "5":
                        auth_service.eliminar_usuario(user_id)
                        break
                    elif opcion_menu == "6":
                        print("Sesión cerrada.")
                        payroll_service.close()
                        break
                    else:
                        print("Opción no válida. Por favor, intente de nuevo.")
            else:
                print("Usuario o contraseña incorrectos.")
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            auth_service.close()
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

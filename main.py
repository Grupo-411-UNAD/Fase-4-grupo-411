"""
Programa: Ingeniería de Sistemas
Curso: Programación
Código: 213023
Grupo 411 

Ejercicio 1: Sistema Integral de Gestión de Clientes, Servicios y Reservas

Descripción:
En un equipo conformado por cinco (5) estudiantes, deberán desarrollar un sistema integral orientado a objetos, 
sin uso de bases de datos, capaz de gestionar clientes, servicios y reservas para una empresa llamada Software FJ 
que ofrece varios tipos de servicios (reservas de salas, alquiler de equipos y asesorías especializadas). 
El objetivo de esta tarea es construir una aplicación estable, modular y extensible que implemente de forma rigurosa 
los principios de abstracción, herencia, polimorfismo, encapsulación y manejo avanzado de excepciones, garantizando 
que el sistema siga funcionando aun cuando se presenten errores durante su ejecución.

El sistema debe incluir clases abstractas, clases derivadas, métodos sobrecargados, manejo de listas internas y validaciones estrictas, 
demostrando un diseño orientado a objetos completamente funcional. 
La información no debe almacenarse en bases de datos; toda la gestión debe hacerse mediante objetos, listas y manejo de archivos únicamente 
para el registro de eventos y errores.

Como parte esencial de la tarea, el sistema deberá incorporar manejo robusto de excepciones, incluyendo excepciones personalizadas, 
uso de bloques try/except, try/except/else, try/except/finally, y encadenamiento de excepciones. Cada error detectado debe registrarse 
en un archivo de logs, manteniendo la aplicación activa y estable en todo momento. El sistema debe ser capaz de manejar errores provenientes 
de datos inválidos, parámetros faltantes, operaciones no permitidas, intentos de reserva incorrectos, servicios no disponibles, 
cálculos inconsistentes y cualquier otra situación que pueda comprometer la operación normal de la aplicación.

El trabajo debe basarse en una arquitectura orientada a objetos, incluyendo al menos:

• Una clase abstracta que represente entidades generales del sistema.
• Una clase Cliente con validaciones robustas y encapsulación de datos personales.
• Una clase abstracta Servicio y al menos tres servicios especializados que hereden de ella, implementando polimorfismo y métodos sobrescritos 
para calcular costos, describir servicios y validar parámetros.
• Una clase Reserva que integre cliente, servicio, duración y estado, e implemente confirmación, cancelación y procesamiento con manejo de 
excepciones.
• Métodos sobrecargados (por ejemplo, diferentes variantes del cálculo de costos con impuestos, descuentos o parámetros opcionales).
• Un archivo de logs donde se registren todos los errores y eventos relevantes.

El sistema, sin utilizar ningún motor de base de datos, debe simular al menos 10 operaciones completas, incluyendo registros válidos e inválidos 
de clientes, creación correcta e incorrecta de servicios, y reservas exitosas y fallidas, demostrando la capacidad del programa para continuar 
funcionando ante errores graves y manejar excepciones de manera controlada y profesional.

El equipo debe entregar un único proyecto completamente funcional, organizado, documentado y capaz de ejecutarse sin interrupciones, demostrando 
la correcta aplicación de la programación orientada a objetos y el manejo avanzado de excepciones en un entorno sin base de datos.

"""

# ============================================================
# FUNCIÓN PRINCIPAL DEL PROGRAMA
# ============================================================

# Importación de módulos necesarios para la ejecución del programa principal.
from cliente import Cliente
from servicio import Servicio
from reserva import Reserva
import excepciones

# Listas globales para almacenar clientes, servicios y reservas

clientes = []
servicios = []
reservas = []

def menu():
    salir = False
    while True:
        try:
            # Mostrar menú de opciones al usuario
            print("\n ====== EMPRESA SOFTWARE FJ ====== \n")
            print("1. Registrar cliente")
            print("2. Crear servicio")
            print("3. Crear reserva")
            print("4. Ver reservas")
            print("5. Cancelar reserva")
            print("6. Salir")

            # Solicita opción al usuario
            opcion = int(input("\n - Seleccione el número de la opción:  "))

            # Validación de opción
            if opcion < 1 or opcion > 6:
                raise ValueError("Opción fuera de rango")

        except ValueError as e:
            # Manejo de error
            print(f"Error: {e}")
            excepciones.registrar_log(f"Error de valor: {e}")
#se captura cualquier excepción de tipo ValueError que pueda ocurrir durante la selección de la opción del menú, se registra el error en el archivo de logs y se muestra un mensaje de error al usuario, luego se regresa al menú para que el usuario pueda intentar nuevamente
        else:
            # Flujo normal
            if opcion == 1:
                try:
                    cliente = Cliente.registrar_cliente()
                    clientes.append(cliente)
                    print(f"\n • {cliente.nombre} ha sido registrado exitosamente \n ")
                    excepciones.registrar_log(f"Cliente registrado: {cliente.nombre}")
                    
                except excepciones.ClienteError as e:
                    print(f"Error al registrar cliente: {e}")
                    excepciones.registrar_log(f"Error al registrar cliente: {e}")
#se captura cualquier excepción que pueda ocurrir durante el proceso de registro del cliente, se registra el error en el archivo de logs y se muestra un mensaje de error al usuario
            elif opcion == 2:
                try:
                    servicio = Servicio.crear_servicio()
                    servicios.append(servicio)
                    print(f" \n • Servicio {servicio.nombre} creado exitosamente: \n\n{servicio.descripcion()}")
                    excepciones.registrar_log(f"Servicio creado: {servicio.descripcion()}")
                except excepciones.ServicioError as e:
                    print(f"Error al crear servicio, causa: {e}")
                    excepciones.registrar_log(f"Error al crear servicio: {e}")
                except ValueError as e:
                    print(f"Error al crear servicio: {e}")
                    excepciones.registrar_log(f"Error al crear servicio: {e}")
#se captura cualquier excepción que pueda ocurrir durante el proceso de creación del servicio, se registra el error en el archivo de logs y se muestra un mensaje de error al usuario
            elif opcion == 3:
                try:
                    if len(clientes) == 0:
                        raise excepciones.ReservaError("No hay clientes registrados")
                    elif len(servicios) == 0:
                        raise excepciones.ReservaError("No hay servicios disponibles")
                    else:
                        print("\nCLIENTES")
                        for i, c in enumerate(clientes):
                            print(i, "-", c.nombre)

                        seleccionar_cliente = int(input("\n - Seleccione cliente: "))

                        print("\nSERVICIOS")
                        for i, s in enumerate(servicios):
                            print(i, "-", s.nombre)

                        seleccionar_servicio = int(input("\n - Seleccione servicio: "))
                        
                        reserva = Reserva.crear_reserva(clientes[seleccionar_cliente], servicios[seleccionar_servicio])
                        reservas.append(reserva)
                        print(f" \n • Reserva creada exitosamente: \n\n {reserva.mostrar_informacion()}")
                        excepciones.registrar_log(f" Reserva creada: {reserva.mostrar_informacion()}")
                except ValueError as e:
                    print(f"Error al crear reserva: {e}")
                    excepciones.registrar_log(f"Error al crear reserva: {e}")
                except excepciones.ReservaError as e:
                    print(f"Error al crear reserva: {e}")
                    excepciones.registrar_log(f"Error al crear reserva: {e}")
#se captura cualquier excepción que pueda ocurrir durante el proceso de creación de la reserva, se registra el error en el archivo de logs y se muestra un mensaje de error al usuario
            elif opcion == 4:
                try:
                    if len(reservas) == 0:
                        print("No se han creado reservas")
                    else:
                        for r in reservas:
                            print ("\n ======== Reservas creadas: ======== \n")
                            print(r.mostrar_informacion())
                except Exception as e:
                    excepciones.registrar_log(f"Error mostrando reservas: {e}")
                    print("Error al mostrar reservas")
 #se captura cualquier excepción que pueda ocurrir al mostrar las reservas, se registra el error en el archivo de logs y se muestra un mensaje de error al usuario                   
            elif opcion == 5:
                try:
                    if len(reservas) == 0:
                        print("No se han creado reservas")
                    else:
                        print("\nRESERVAS")
                        for i, r in enumerate(reservas):
                            print(i, "-", r.servicio.nombre)

                        seleccionar_reserva = int(input("\n - Seleccione reserva: "))
                        if seleccionar_reserva < 0 or seleccionar_reserva >= len(reservas):
                            raise ValueError("Índice de reserva inválido")
                        
                        reserva_a_cancelar = reservas[seleccionar_reserva]
                        reserva_a_cancelar.cancelar()
                        reservas.remove(reserva_a_cancelar)
                        print(f" \n • Reserva cancelada exitosamente: \n\n {reserva_a_cancelar.mostrar_informacion()}")
                        excepciones.registrar_log(f" Reserva cancelada: {reserva_a_cancelar.mostrar_informacion()}")
                except ValueError as e:
                    print(f"Error al cancelar reserva: {e}")
                    excepciones.registrar_log(f"Error al cancelar reserva: {e}")
                except Exception as e:
                    print(f"Error al cancelar reserva: {e}")
                    excepciones.registrar_log(f"Error al cancelar reserva: {e}")

            elif opcion == 6:
                print("\n Saliendo del sistema... \n")
                excepciones.registrar_log("Saliendo del sistema...")
                salir = True
                break

        finally:
            # Siempre se ejecuta
            if not salir:
                print("\n Regresando al menú...\n")
    
    print(clientes)
    print(servicios)
    print(reservas)
    print("\n Gracias por usar el sistema de Software FJ. ¡Hasta luego! \n")
    excepciones.registrar_log("Programa finalizado")



# Punto de entrada del programa
if __name__ == "__main__":
    # Llama al menú
    menu()
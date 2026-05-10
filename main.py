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

# =====================================================================================
# INICIO DEL PROGRAMA PRINCIPAL
# =====================================================================================
# -----------------------------------------------------------------------------------
# Importación de módulos necesarios para la ejecución del programa principal.
# -----------------------------------------------------------------------------------
from cliente import Cliente
from servicio import Servicio, ReservaSala, AlquilerEquipo, ServiciosEspeciales
from reserva import Reserva
import excepciones

# -----------------------------------------------------------------------------------
# Listas globales para almacenar clientes, servicios y reservas
# -----------------------------------------------------------------------------------
clientes = []
servicios = []
reservas = []

# =====================================================================================
# SIMULACIÓN DE USO DEL SISTEMA CON OPERACIONES VÁLIDAS E INVÁLIDAS
# =====================================================================================

def simular():
    """
    Ejecuta 10 simulaciones de uso del sistema con operaciones válidas e inválidas.
    Cada operación muestra su resultado y registra el evento en el archivo de logs.
    """
    sim_clientes = []
    sim_servicios = []
    sim_reservas = []
    separador = "=" * 55
    print(f"\n{separador}")
    print("   INICIO DE SIMULACIONES - SOFTWARE FJ")
    print(separador)
    excepciones.registrar_log("=== Inicio de simulaciones ===")
    # ----------------------------------------------------------
    # SIMULACIÓN 1 — Registro de cliente VÁLIDO
    # ----------------------------------------------------------
    print("\n[Sim 1] Registrar cliente válido: Ana García")
    try:
        c1 = Cliente("Ana García", "123456789", "3001234567")
        sim_clientes.append(c1)
        print(f"  ✔ Cliente registrado: {c1}")
        excepciones.registrar_log(f"[Sim 1] Cliente registrado: {c1}")
    except excepciones.ClienteError as e:
        print(f"  ✘ Error inesperado: {e}")
        excepciones.registrar_log(f"[Sim 1] Error: {e}")
    # ----------------------------------------------------------
    # SIMULACIÓN 2 — Registro de cliente INVÁLIDO (nombre con números)
    # ----------------------------------------------------------
    print("\n[Sim 2] Registrar cliente inválido: nombre 'Ana123'")
    try:
        nombre = "Ana123"
        if not nombre.replace(" ", "").isalpha():
            raise excepciones.ClienteError("El nombre solo debe contener letras")
        sim_clientes.append(Cliente(nombre, "987654321", "3109876543"))
    except excepciones.ClienteError as e:
        print(f"  ✘ Error capturado correctamente: {e}")
        excepciones.registrar_log(f"[Sim 2] Error esperado: {e}")
    finally:
        print("  → Bloque finally: validación de nombre finalizada")
    # ----------------------------------------------------------
    # SIMULACIÓN 3 — Registro de cliente VÁLIDO
    # ----------------------------------------------------------
    print("\n[Sim 3] Registrar cliente válido: Carlos López")
    try:
        c2 = Cliente("Carlos López", "987654321", "3109876543")
        sim_clientes.append(c2)
        print(f"  ✔ Cliente registrado: {c2}")
        excepciones.registrar_log(f"[Sim 3] Cliente registrado: {c2}")
    except excepciones.ClienteError as e:
        print(f"  ✘ Error inesperado: {e}")
        excepciones.registrar_log(f"[Sim 3] Error: {e}")
    # ----------------------------------------------------------
    # SIMULACIÓN 4 — Registro de cliente INVÁLIDO (documento empieza en 0)
    # ----------------------------------------------------------
    print("\n[Sim 4] Registrar cliente inválido: documento '0123456'")
    try:
        documento = "0123456"
        if not documento.isdigit() or len(documento) < 6 or len(documento) > 12 or documento[0] == '0':
            raise excepciones.ClienteError("Documento inválido")
        sim_clientes.append(Cliente("Pedro Ruiz", documento, "3207654321"))
    except excepciones.ClienteError as e:
        print(f"  ✘ Error capturado correctamente: {e}")
        excepciones.registrar_log(f"[Sim 4] Error esperado: {e}")
    finally:
        print("  → Bloque finally: validación de documento finalizada")
    # ----------------------------------------------------------
    # SIMULACIÓN 5 — Creación de servicio VÁLIDO (ReservaSala)
    # ----------------------------------------------------------
    print("\n[Sim 5] Crear servicio válido: Reserva de Sala por 3 horas")
    try:
        s1 = ReservaSala(3)
        sim_servicios.append(s1)
        print(f"  ✔ Servicio creado: {s1.descripcion()} | Costo: {s1.calcular_costo()} pesos")
        excepciones.registrar_log(f"[Sim 5] Servicio creado: {s1.descripcion()}")
    except excepciones.ServicioError as e:
        print(f"  ✘ Error inesperado: {e}")
        excepciones.registrar_log(f"[Sim 5] Error: {e}")
    # ----------------------------------------------------------
    # SIMULACIÓN 6 — Creación de servicio INVÁLIDO (ReservaSala con 0 horas)
    # ----------------------------------------------------------
    print("\n[Sim 6] Crear servicio inválido: Reserva de Sala con 0 horas")
    try:
        s_invalido = ReservaSala(0)
        sim_servicios.append(s_invalido)
    except excepciones.ServicioError as e:
        print(f"  ✘ Error capturado correctamente: {e}")
        excepciones.registrar_log(f"[Sim 6] Error esperado: {e}")
    finally:
        print("  → Bloque finally: validación de duración de sala finalizada")
    # ----------------------------------------------------------
    # SIMULACIÓN 7 — Creación de servicio VÁLIDO (AlquilerEquipo)
    # ----------------------------------------------------------
    print("\n[Sim 7] Crear servicio válido: Alquiler de Laptop por 5 días")
    try:
        s2 = AlquilerEquipo("Laptop", 5)
        sim_servicios.append(s2)
        print(f"  ✔ Servicio creado: {s2.descripcion()} | Costo con 10% impuesto: {s2.calcular_costo(impuesto=10)} pesos")
        excepciones.registrar_log(f"[Sim 7] Servicio creado: {s2.descripcion()}")
    except excepciones.ServicioError as e:
        print(f"  ✘ Error inesperado: {e}")
        excepciones.registrar_log(f"[Sim 7] Error: {e}")
    # ----------------------------------------------------------
    # SIMULACIÓN 8 — Creación de servicio VÁLIDO (ServicioEspecial) + reserva válida
    # ----------------------------------------------------------
    print("\n[Sim 8] Crear servicio especial válido y reserva para Ana García")
    try:
        s3 = ServiciosEspeciales("Asesoría en Ciberseguridad", 250000)
        sim_servicios.append(s3)
        print(f"  ✔ Servicio creado: {s3.descripcion()}")
        excepciones.registrar_log(f"[Sim 8] Servicio creado: {s3.descripcion()}")
        r1 = Reserva(sim_clientes[0], s3, 2)
        r1.confirmar()
        sim_reservas.append(r1)
        print(f"  ✔ Reserva creada: {r1.mostrar_informacion()}")
        excepciones.registrar_log(f"[Sim 8] Reserva creada: {r1.mostrar_informacion()}")
    except (excepciones.ServicioError, excepciones.ReservaError) as e:
        print(f"  ✘ Error inesperado: {e}")
        excepciones.registrar_log(f"[Sim 8] Error: {e}")
    # ----------------------------------------------------------
    # SIMULACIÓN 9 — Creación de reserva INVÁLIDA (duración 0)
    # ----------------------------------------------------------
    print("\n[Sim 9] Crear reserva inválida: duración 0 horas")
    try:
        r_invalida = Reserva(sim_clientes[0], sim_servicios[0], 0)
        sim_reservas.append(r_invalida)
    except excepciones.ReservaError as e:
        print(f"  ✘ Error capturado correctamente: {e}")
        excepciones.registrar_log(f"[Sim 9] Error esperado: {e}")
    except Exception as e:
        raise excepciones.ReservaError("Error al crear reserva inválida") from e
    finally:
        print("  → Bloque finally: validación de duración de reserva finalizada")
    # ----------------------------------------------------------
    # SIMULACIÓN 10 — Cancelación de reserva VÁLIDA
    # ----------------------------------------------------------
    print("\n[Sim 10] Cancelar la reserva de Ana García")
    try:
        if len(sim_reservas) == 0:
            raise excepciones.ReservaError("No hay reservas para cancelar")
        reserva_a_cancelar = sim_reservas[0]
        reserva_a_cancelar.cancelar()
        sim_reservas.remove(reserva_a_cancelar)
        print(f"  ✔ Reserva cancelada: {reserva_a_cancelar.mostrar_informacion()}")
        excepciones.registrar_log(f"[Sim 10] Reserva cancelada: {reserva_a_cancelar.mostrar_informacion()}")
    except excepciones.ReservaError as e:
        print(f"  ✘ Error al cancelar: {e}")
        excepciones.registrar_log(f"[Sim 10] Error: {e}")
    print(f"\n{separador}")
    print("   FIN DE SIMULACIONES")
    print(f"   Clientes registrados: {len(sim_clientes)}")
    print(f"   Servicios creados:    {len(sim_servicios)}")
    print(f"   Reservas activas:     {len(sim_reservas)}")
    print(separador)
    excepciones.registrar_log("=== Fin de simulaciones ===")
    
# ============================================================
# MENÚ PRINCIPAL DEL SISTEMA
# ============================================================

def menu():
    
    """
    Función principal del sistema.
    Muestra el menú y gestiona todas las operaciones.
    """
    salir = False
    separador = "=" * 60
    while True:
        try:
            # ----------------------------------------------------------
            # Mostrar menú de opciones al usuario
            # ----------------------------------------------------------
            print(f"\n{separador}")
            print("\n ====== EMPRESA SOFTWARE FJ ====== \n")
            print("1. Registrar cliente")
            print("2. Crear servicio")
            print("3. Crear reserva")
            print("4. Ver reservas")
            print("5. Cancelar reserva")
            print("6. Salir")
            print(f"\n{separador}")

            # ----------------------------------------------------------
            # Solicita opción al usuario
            # ----------------------------------------------------------
            opcion = int(input("\n - Seleccione el número de la opción:  "))

            # ----------------------------------------------------------
            # Validación de opción
            # ----------------------------------------------------------
            if opcion < 1 or opcion > 6:
                raise ValueError("Opción fuera de rango")

        except ValueError as e:
            # Manejo de error
            print(f"Error: {e}")
            excepciones.registrar_log(f"Error de valor: {e}")
            
        else:
            # ----------------------------------------------------------
            # Flujo normal del programa para cada opción
            # ----------------------------------------------------------
            if opcion == 1:
                try:
                    cliente = Cliente.registrar_cliente()
                    clientes.append(cliente)
                    print(f"\n • {cliente.nombre} ha sido registrado exitosamente \n ")
                    excepciones.registrar_log(f"Cliente registrado: {cliente.nombre}")
                    
                except excepciones.ClienteError as e:
                    print(f"Error al registrar cliente: {e}")
                    excepciones.registrar_log(f"Error al registrar cliente: {e}")

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
            # --------------------------------------
            # Siempre se ejecuta
            # --------------------------------------
            if not salir:
                print("\n Regresando al menú...\n")
    
    # ------------------------------------------------------------------------------------------------------------------------------------
    # Al salir del programa, muestra un resumen de clientes, servicios y reservas, y registra el cierre del programa en el archivo de logs
    # ------------------------------------------------------------------------------------------------------------------------------------
    print(f"\n{separador}\n")
    print("Resumen final del sistema:\n")
    print(clientes)
    print(servicios)
    print(reservas)
    print("\n Gracias por utilizar los servicios de Software FJ. ¡Hasta luego! ")
    print(f"\n{separador}")
    excepciones.registrar_log("Programa finalizado")


# ------------------------------------------------------------------------------------------------------------------------------------------
# Punto de entrada del programa
# ------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    """
    Punto de entrada del programa.
    Llama al menú y a la función de simulación para ejecutar las operaciones completas.
    """
    menu()
    simular()
# Fase_4_Grupo_411
Fase 4 - Componente práctico - Prácticas simuladas de programación 

#------------------------------------------------------------------------------------------------------------------
# INTEGRANTES 
#------------------------------------------------------------------------------------------------------------------

Cristian Daniel Neira Palacios
Jeiry Arenilla Moreno
Juan Pablo Bonilla González
Leidy Nicole Jara Gamba
Nestor Hugo Caicedo Vanegas

#------------------------------------------------------------------------------------------------------------------
# Necesidades del sistema
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
| Req. | Descripción                           | Entradas                          | Salidas                       |
#------------------------------------------------------------------------------------------------------------------
| R1   | Validar los datos de un cliente       | Documento, nombre y teléfono      | Cliente válido o excepción    |
|      |                                       |                                   | personalizada                 |
#------------------------------------------------------------------------------------------------------------------
| R2   | Validar atributos de un servicio      | Horas, días, costo o              | Servicio válido o excepción   |
|      |                                       | disponibilidad                    | personalizada                 |
#------------------------------------------------------------------------------------------------------------------
| R3   | Calcular el costo de un servicio      | Objeto servicio, descuento        | Valor total calculado o       |
|      |                                       | o impuesto                        | excepción                     |
#------------------------------------------------------------------------------------------------------------------
| R4   | Mostrar la descripción de un servicio | Objeto servicio                   | Cadena de texto descriptiva   |
#------------------------------------------------------------------------------------------------------------------
| R5   | Registrar una reserva                 | Cliente, servicio y duración      | Reserva creada o excepción    |
#------------------------------------------------------------------------------------------------------------------
| R6   | Confirmar una reserva                 | Objeto reserva                    | Estado actualizado a          |
|      |                                       |                                   | “confirmada” o excepción      |
#------------------------------------------------------------------------------------------------------------------
| R7   | Cancelar una reserva                  | Objeto reserva                    | Estado actualizado a          |
|      |                                       |                                   | “cancelada” o excepción       |
#------------------------------------------------------------------------------------------------------------------
| R8   | Validar disponibilidad del servicio   | Servicio seleccionado             |Servicio disponible o excepción|
#------------------------------------------------------------------------------------------------------------------
| R9   | Registrar errores y eventos           | Descripción del error             | Archivo de logs actualizado   |
|      | del sistema                           | o evento                          |                               |
#------------------------------------------------------------------------------------------------------------------
| R10  | Mostrar información de una reserva    | Objeto reserva                    | Texto con cliente, servicio   |
|      |                                       |                                   | y estado                      |
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
# Guia basica del sistema
#------------------------------------------------------------------------------------------------------------------

# ejecucion del sitema

PASO 1 
DIRIJASE AL MODULO MAIN.PY

PASO 2
PRESIONE RUN PARA INICIAR LOS POCESOS
(El sistema manifestara las opcione mediante la terminal)
============================================================
====== EMPRESA SOFTWARE FJ ====== 

1. Registrar cliente
2. Crear servicio
3. Crear reserva
4. Ver reservas
5. Cancelar reserva
6. Salir

============================================================

PASO 3
SELECCIONE EL NÚMERO DE LA OPCIÓN:
(Ejemplo "1" El progrma pedira el ingreso de datos basicos)
# Nombre
# Documento
# Teléfono

============================================================

# NOTA
(Dependiendo de la opcion selecionada los requsitos u datos de
ingreseo seran distos segun la tarea a derrollar dentro del sistema)

# Informacion resumida de esturtura del proyecto
El proyecto sigue una estructura basada en la Programación Orientada a Objetos (POO) aplicada en un sistema que implementa modulación estructural, validando la división de tareas en archivos .py y facilitando el mantenimiento y actualización del sistema.

La arquitectura se dirige a la atención de módulos base como (Cliente, Reservas, Servicios). Sin uso de bases de datos, aplicando métodos de herencia, listas o encapsulamiento y aplicación de abstracción general, sujetas a validaciones y excepciones aplicadas a las necesidades.

El sistema se manifiesta mediante el módulo (main.py), que importa la información de métodos privados o validaciones y excepciones según las necesidades de la tarea, además de almacenar mediante un logger los errores o procesos de ejecución.

Cada módulo gestiona de manera general sus necesidades, solicitando e importando información de los módulos que lo acompañan y que interactúan con su información.
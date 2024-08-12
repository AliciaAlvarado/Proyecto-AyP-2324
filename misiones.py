import pandas as pd
from personaje import Personaje
from planeta import Planeta
from nave import Nave
from arma import Arma

# Lista global para almacenar las misiones
misiones_definidas = []

def mostrar_opciones(opciones):
    for i, opcion in enumerate(opciones, 1):
        print(f"{i:02d}. {opcion}")

def elegir_opcion(opciones, max_seleccion=1, permitir_repetidos=True):
    opciones_elegidas = []
    while len(opciones_elegidas) < max_seleccion:
        mostrar_opciones(opciones)
        seleccion = input(f"Introduzca el número de su elección (opciones desde el número 1 al número {len(opciones)}): ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(opciones):
            opcion_elegida = opciones[int(seleccion) - 1]
            if not permitir_repetidos and opcion_elegida in opciones_elegidas:
                print("Esta opción ya fue seleccionada. Por favor, elija una diferente.")
            else:
                opciones_elegidas.append(opcion_elegida)
        else:
            print("Entrada no válida. Por favor, intente nuevamente.")
    return opciones_elegidas

def guardar_misiones_en_archivo():
    if not misiones_definidas:
        print("No hay misiones para guardar.")
        return

    with open("misiones.txt", "w") as file:
        for mision in misiones_definidas:
            mision["armas"] = ','.join(mision["armas"])
            mision["integrantes"] = ','.join(mision["integrantes"])
            line = f'{mision["nombre"]}|{mision["planeta_destino"]}|{mision["nave"]}|{mision["armas"]}|{mision["integrantes"]}\n'
            file.write(line)
            mision["armas"] = mision["armas"].split(',')
            mision["integrantes"] = mision["integrantes"].split(',')

    print("Las misiones se han guardado correctamente.")

def cargar_misiones_desde_archivo():
    try:
        global misiones_definidas
        misiones_definidas = []

        with open("misiones.txt", "r") as file:
            for line in file:
                nombre, planeta_destino, nave, armas, integrantes = line.strip().split('|')
                mision = {
                    "nombre": nombre,
                    "planeta_destino": planeta_destino,
                    "nave": nave,
                    "armas": armas.split(','),
                    "integrantes": integrantes.split(',')
                }
                misiones_definidas.append(mision)

        print("Las misiones se han cargado correctamente.")
    except FileNotFoundError:
        print("No se encontró el archivo misiones.txt. Asegúrese de haber guardado misiones previamente.")

def crear_nueva_mision():
    if len(misiones_definidas) >= 5:
        print("Se alcanzó el máximo de 5 misiones permitidas.")
        return

    nueva_mision = {}
    
    nueva_mision["nombre"] = input("Introduzca el nombre de la misión: ")

    print("Elija el planeta de destino:")
    planetas_disponibles = [planet.nombre for planet in Planeta.lista_planetas]
    nueva_mision["planeta_destino"] = elegir_opcion(planetas_disponibles, max_seleccion=1)[0]

    print("Seleccione la nave que se utilizará:")
    naves_disponibles = [nave.nombre for nave in Nave.lista_naves]
    nueva_mision["nave"] = elegir_opcion(naves_disponibles, max_seleccion=1)[0]

    print("Elija hasta 7 armas:")
    armas_disponibles = [arma.nombre for arma in Arma.lista_armas]
    nueva_mision["armas"] = elegir_opcion(armas_disponibles, max_seleccion=7)

    print("Elija hasta 7 miembros del equipo:")
    integrantes_disponibles = [personaje.nombre for personaje in Personaje.lista_personajes]
    nueva_mision["integrantes"] = elegir_opcion(integrantes_disponibles, max_seleccion=7, permitir_repetidos=False)

    misiones_definidas.append(nueva_mision)
    print(f"La misión '{nueva_mision['nombre']}' ha sido creada exitosamente.")

def modificar_mision_existente():
    if not misiones_definidas:
        print("No existen misiones para modificar.")
        return

    print("Lista de misiones disponibles:")
    mostrar_opciones([mision['nombre'] for mision in misiones_definidas])
    
    seleccion = input(f"Seleccione una misión para editar (opciones desde el número 1 al número {len(misiones_definidas)}): ")
    if not seleccion.isdigit() or not 1 <= int(seleccion) <= len(misiones_definidas):
        print("Selección incorrecta.")
        return

    mision_index = int(seleccion) - 1
    mision = misiones_definidas[mision_index]

    print(f"Editando la misión '{mision['nombre']}'")

    while True:
        print("\n¿Qué desea modificar?")
        print("1. Armas")
        print("2. Miembros del equipo")
        print("3. Volver al menú anterior")

        opcion = input(">>>> ")
        
        if opcion == "1":
            print("Elija las nuevas armas:")
            armas_disponibles = [arma.nombre for arma in Arma.lista_armas]
            nuevas_armas = elegir_opcion(armas_disponibles, max_seleccion=7)
            mision["armas"] = nuevas_armas
            print(f"Armas actualizadas: {mision['armas']}")
        elif opcion == "2":
            print("Elija los nuevos miembros del equipo:")
            nuevos_integrantes = elegir_opcion([personaje.nombre for personaje in Personaje.lista_personajes], max_seleccion=7, permitir_repetidos=False)
            mision["integrantes"] = nuevos_integrantes
            print(f"Miembros del equipo actualizados: {mision['integrantes']}")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

    print(f"Los cambios en la misión '{mision['nombre']}' se han guardado correctamente.")

def ver_detalles_mision():
    if not misiones_definidas:
        print("No hay misiones disponibles para mostrar.")
        return

    print("Lista de misiones disponibles:")
    mostrar_opciones([mision['nombre'] for mision in misiones_definidas])
    
    seleccion = input(f"Seleccione una misión para ver sus detalles (opciones desde el número 1 al número {len(misiones_definidas)}): ")
    if not seleccion.isdigit() or not 1 <= int(seleccion) <= len(misiones_definidas):
        print("Selección incorrecta.")
        return

    mision_index = int(seleccion) - 1
    mision = misiones_definidas[mision_index]

    print(f"\nDetalles de la misión '{mision['nombre']}':")
    print(f"Planeta destino: {mision['planeta_destino']}")
    print(f"Nave utilizada: {mision['nave']}")
    print(f"Armas: {', '.join(mision['armas'])}")
    print(f"Miembros del equipo: {', '.join(mision['integrantes'])}")

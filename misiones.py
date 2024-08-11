import pandas as pd
from personaje import Personaje
from planeta import Planeta
from nave import Nave

misiones = []  # Lista global para almacenar las misiones
armas_disponibles = [
    "Bláster", 
    "Sable de luz", 
    "Detonador térmico", 
    "Bowcaster", 
    "Pistola de iones", 
    "Rifle de francotirador", 
    "Lanza misiles", 
    "Cañón láser", 
    "Arco energético", 
    "Daga vibro", 
    "Látigo de energía", 
    "Granada de fragmentación"
]

def listar_opciones(opciones):
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")

def seleccionar_opcion(opciones, max_seleccion=1, permitir_repetidos=True):
    seleccionados = []
    while len(seleccionados) < max_seleccion:
        listar_opciones(opciones)
        seleccion = input(f"Seleccione una opción (1-{len(opciones)}), o presione Enter para terminar: ")
        if seleccion == "":
            break
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(opciones):
            opcion_seleccionada = opciones[int(seleccion) - 1]
            if not permitir_repetidos and opcion_seleccionada in seleccionados:
                print("Esa opción ya ha sido seleccionada. Por favor, elija otra.")
            else:
                seleccionados.append(opcion_seleccionada)
        else:
            print("Selección no válida. Por favor, intente de nuevo.")
    return seleccionados

def construir_mision():
    if len(misiones) >= 5:
        print("No se pueden definir más de 5 misiones.")
        return

    mision = {}
    
    mision["nombre"] = input("Nombre de la misión: ")

    print("Seleccione el planeta destino:")
    planetas = [planet.nombre for planet in Planeta.lista_planetas]
    mision["planeta_destino"] = seleccionar_opcion(planetas, max_seleccion=1)[0]

    print("Seleccione la nave a utilizar:")
    naves = [nave.nombre for nave in Nave.lista_naves]
    mision["nave"] = seleccionar_opcion(naves, max_seleccion=1)[0]

    print("Seleccione hasta 7 armas:")
    mision["armas"] = seleccionar_opcion(armas_disponibles, max_seleccion=7)

    print("Seleccione hasta 7 integrantes:")
    integrantes = [personaje.nombre for personaje in Personaje.lista_personajes]
    mision["integrantes"] = seleccionar_opcion(integrantes, max_seleccion=7, permitir_repetidos=False)

    misiones.append(mision)
    print(f"Misión '{mision['nombre']}' construida exitosamente.")

def modificar_mision():
    if not misiones:
        print("No hay misiones definidas.")
        return

    print("Misiones definidas:")
    listar_opciones([mision['nombre'] for mision in misiones])
    
    seleccion = input(f"Seleccione una misión para modificar (1-{len(misiones)}): ")
    if not seleccion.isdigit() or not 1 <= int(seleccion) <= len(misiones):
        print("Selección no válida.")
        return

    mision_index = int(seleccion) - 1
    mision = misiones[mision_index]

    print(f"Modificando misión '{mision['nombre']}'")

    while True:
        print("\nSeleccione qué desea modificar:")
        print("1. Armas")
        print("2. Integrantes")
        print("3. Regresar")

        opcion = input(">>>> ")
        
        if opcion == "1":
            print("Seleccione las armas:")
            nuevas_armas = seleccionar_opcion(armas_disponibles, max_seleccion=7)
            mision["armas"] = nuevas_armas
            print(f"Armas actualizadas: {mision['armas']}")
        elif opcion == "2":
            print("Seleccione los integrantes:")
            nuevos_integrantes = seleccionar_opcion([personaje.nombre for personaje in Personaje.lista_personajes], max_seleccion=7, permitir_repetidos=False)
            mision["integrantes"] = nuevos_integrantes
            print(f"Integrantes actualizados: {mision['integrantes']}")
        elif opcion == "3":
            break
        else:
            print("Selección no válida. Por favor, intente de nuevo.")

    print(f"Misión '{mision['nombre']}' modificada exitosamente.")

def visualizar_mision():
    if not misiones:
        print("No hay misiones definidas.")
        return

    print("Misiones definidas:")
    listar_opciones([mision['nombre'] for mision in misiones])
    
    seleccion = input(f"Seleccione una misión para visualizar (1-{len(misiones)}): ")
    if not seleccion.isdigit() or not 1 <= int(seleccion) <= len(misiones):
        print("Selección no válida.")
        return

    mision_index = int(seleccion) - 1
    mision = misiones[mision_index]

    print(f"\nDetalles de la misión '{mision['nombre']}':")
    print(f"Planeta destino: {mision['planeta_destino']}")
    print(f"Nave a utilizar: {mision['nave']}")
    print(f"Armas: {', '.join(mision['armas'])}")
    print(f"Integrantes: {', '.join(mision['integrantes'])}")

def guardar_misiones():
    if not misiones:
        print("No hay misiones definidas para guardar.")
        return

    for mision in misiones:
        mision["armas"] = ','.join(mision["armas"])
        mision["integrantes"] = ','.join(mision["integrantes"])

    df = pd.DataFrame(misiones)
    df.to_csv("misiones.csv", index=False)
    print("Misiones guardadas exitosamente.")

    for mision in misiones:
        mision["armas"] = mision["armas"].split(',')
        mision["integrantes"] = mision["integrantes"].split(',')

def cargar_misiones():
    try:
        df = pd.read_csv("misiones.csv")
        global misiones
        misiones = df.to_dict(orient="records")
        
        for mision in misiones:
            mision["armas"] = mision["armas"].split(',')
            mision["integrantes"] = mision["integrantes"].split(',')
        
        print("Misiones cargadas exitosamente.")
    except FileNotFoundError:
        print("No se encontró el archivo misiones.csv. Asegúrese de haber guardado misiones previamente.")

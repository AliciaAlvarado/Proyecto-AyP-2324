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
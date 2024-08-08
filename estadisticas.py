import matplotlib.pyplot as plt
import pandas as pd
from personaje import Personaje
from nave import Nave

def grafico_personajes_por_planeta():
    data = {}

    for personaje in Personaje.lista_personajes:
        if personaje.planeta_origen:
            if personaje.planeta_origen not in data:
                data[personaje.planeta_origen] = 0
            data[personaje.planeta_origen] += 1

    if not data:
        print("No hay datos disponibles para mostrar el gráfico.")
        return

    df = pd.DataFrame(list(data.items()), columns=['Planeta', 'Cantidad'])
    df.plot(x='Planeta', y='Cantidad', kind='bar', legend=False)
    plt.title('Cantidad de personajes nacidos en cada planeta')
    plt.xlabel('Planeta')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45)
    plt.show()

def grafico_caracteristicas_naves():
    print("\nSeleccione la clase de nave que desea comparar:")
    clases_naves = list(set([nave.clase for nave in Nave.lista_naves]))
    for i, clase in enumerate(clases_naves):
        print(f"{i + 1}. {clase}")
    
    while True:
        try:
            seleccion = int(input("Ingrese el número correspondiente a la clase de nave: "))
            if 1 <= seleccion <= len(clases_naves):
                clase_seleccionada = clases_naves[seleccion - 1]
                break
            else:
                print("Selección no válida. Por favor, intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    naves_filtradas = [nave for nave in Nave.lista_naves if nave.clase == clase_seleccionada]

    if not naves_filtradas:
        print("No se encontraron naves para la clase seleccionada.")
        return

    data = {
        "Nombre": [nave.nombre for nave in naves_filtradas],
        "Longitud": [float(nave.longitud.replace(',', '')) if nave.longitud.replace(',', '').isdigit() else 0 for nave in naves_filtradas],
        "Capacidad de Carga": [int(nave.capacidad_carga.replace(',', '')) if nave.capacidad_carga.replace(',', '').isdigit() else 0 for nave in naves_filtradas],
        "Clasificación de Hiperimpulsor": [float(nave.hiperimpulsor) if nave.hiperimpulsor.replace('.', '', 1).isdigit() else 0 for nave in naves_filtradas],
        "MGLT": [int(nave.mglt) if nave.mglt.isdigit() else 0 for nave in naves_filtradas]
    }

    df = pd.DataFrame(data)

    if df.empty:
        print("No hay datos disponibles para mostrar el gráfico.")
        return
    
    plt.figure(figsize=(10, 6))

    # Gráfico de Longitud
    plt.subplot(2, 2, 1)
    df.plot(x='Nombre', y='Longitud', kind='bar', ax=plt.gca(), title='Longitud de las naves')

    # Gráfico de Capacidad de Carga
    plt.subplot(2, 2, 2)
    df.plot(x='Nombre', y='Capacidad de Carga', kind='bar', ax=plt.gca(), title='Capacidad de Carga')

    # Gráfico de Clasificación de Hiperimpulsor
    plt.subplot(2, 2, 3)
    df.plot(x='Nombre', y='Clasificación de Hiperimpulsor', kind='bar', ax=plt.gca(), title='Clasificación de Hiperimpulsor')

    # Gráfico de MGLT
    plt.subplot(2, 2, 4)
    df.plot(x='Nombre', y='MGLT', kind='bar', ax=plt.gca(), title='MGLT')
    
    plt.tight_layout()
    plt.show()

def estadisticas_naves():
    print("\nSeleccione la clase de nave para ver estadísticas:")
    clases_naves = list(set([nave.clase for nave in Nave.lista_naves]))
    for i, clase in enumerate(clases_naves):
        print(f"{i + 1}. {clase}")
    
    while True:
        try:
            seleccion = int(input("Ingrese el número correspondiente a la clase de nave: "))
            if 1 <= seleccion <= len(clases_naves):
                clase_seleccionada = clases_naves[seleccion - 1]
                break
            else:
                print("Selección no válida. Por favor, intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    
    naves_filtradas = [nave for nave in Nave.lista_naves if nave.clase == clase_seleccionada]

    if not naves_filtradas:
        print("No se encontraron naves para la clase seleccionada.")
        return

    # Imprimir el nombre de la clase de la nave seleccionada
    print(f"\nEstadísticas para la clase de nave: {clase_seleccionada}\n")

    data = {
        "Nombre": [nave.nombre for nave in naves_filtradas],
        "Longitud": [float(nave.longitud.replace(',', '')) if nave.longitud.replace(',', '').isdigit() else 0 for nave in naves_filtradas],
        "Capacidad de Carga": [int(nave.capacidad_carga.replace(',', '')) if nave.capacidad_carga.replace(',', '').isdigit() else 0 for nave in naves_filtradas],
        "Clasificación de Hiperimpulsor": [float(nave.hiperimpulsor) if nave.hiperimpulsor.replace('.', '', 1).isdigit() else 0 for nave in naves_filtradas],
        "MGLT": [int(nave.mglt) if nave.mglt.isdigit() else 0 for nave in naves_filtradas],
        "Velocidad Máxima en Atmósfera": [int(nave.velocidad_atmosfera.replace(',', '')) if nave.velocidad_atmosfera.replace(',', '').isdigit() else 0 for nave in naves_filtradas],
        "Costo en Créditos": [int(nave.costo_creditos.replace(',', '')) if nave.costo_creditos.replace(',', '').isdigit() else 0 for nave in naves_filtradas]
    }

    df = pd.DataFrame(data)

    if df.empty:
        print("No hay datos disponibles para mostrar las estadísticas.")
        return

    print(df.describe().T)

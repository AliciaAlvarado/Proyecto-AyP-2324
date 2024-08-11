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

    def safe_convert(value, conversion_func, default=0):
        try:
            return conversion_func(value.replace(',', '').replace('unknown', '')) if value else default
        except ValueError:
            return default

    data = {
        "Nombre": [nave.nombre for nave in naves_filtradas],
        "Longitud": [safe_convert(nave.longitud, float) for nave in naves_filtradas],
        "Capacidad de Carga": [safe_convert(nave.capacidad_carga, float) for nave in naves_filtradas],
        "Clasificación de Hiperimpulsor": [safe_convert(nave.hiperimpulsor, float) for nave in naves_filtradas],
        "MGLT": [safe_convert(nave.MGLT, int) for nave in naves_filtradas]
    }

    df = pd.DataFrame(data)

    if df.empty:
        print("No hay datos disponibles para mostrar el gráfico.")
        return

    # Eliminamos columnas con todos los valores cero
    df = df.loc[:, (df != 0).any(axis=0)]

    # Verificamos si hay datos en cada columna antes de graficar
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    plot_idx = 0
    column_titles = {
        'Longitud': 'Longitud de las naves',
        'Capacidad de Carga': 'Capacidad de Carga',
        'Clasificación de Hiperimpulsor': 'Clasificación de Hiperimpulsor',
        'MGLT': 'MGLT'
    }

    for column in ['Longitud', 'Capacidad de Carga', 'Clasificación de Hiperimpulsor', 'MGLT']:
        if column in df.columns:
            ax = axs[plot_idx // 2, plot_idx % 2]
            df.plot(x='Nombre', y=column, kind='bar', ax=ax)
            ax.set_title(column_titles[column])
            ax.set_xlabel('')
            ax.tick_params(axis='x', rotation=45)
            plot_idx += 1
        else:
            axs[plot_idx // 2, plot_idx % 2].axis('off')
            plot_idx += 1

    plt.tight_layout()
    plt.show()

def estadisticas_naves():
    for nave in Nave.lista_naves:
        print(nave.__repr__)
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

    print(f"\nEstadísticas para la clase de nave: {clase_seleccionada}\n")

    def safe_convert(value, conversion_func, default=None):
        try:
            return conversion_func(value.replace(',', '').replace('unknown', '')) if value else default
        except ValueError:
            return default

    data = {
        "Nombre": [nave.nombre for nave in naves_filtradas],
        "Longitud": [safe_convert(nave.longitud, float) for nave in naves_filtradas],
        "Capacidad de Carga": [safe_convert(nave.capacidad_carga, float) for nave in naves_filtradas],
        "Clasificación de Hiperimpulsor": [safe_convert(nave.hiperimpulsor, float) for nave in naves_filtradas],
        "MGLT": [safe_convert(nave.MGLT, int) for nave in naves_filtradas],
        "Velocidad Máxima en Atmósfera": [safe_convert(nave.velocidad_maxima, float) for nave in naves_filtradas],
        "Costo en Créditos": [safe_convert(nave.costo_en_creditos, float) for nave in naves_filtradas]
    }

    df = pd.DataFrame(data)

    if df.empty:
        print("No hay datos disponibles para mostrar las estadísticas.")
        return

    # Eliminamos columnas con todos los valores None
    df = df.dropna(axis=1, how='all')

    # Seleccionamos solo las estadísticas que queremos mostrar
    stats = df.describe().T[['count', 'mean', 'std', 'min', 'max']]
    print(stats)
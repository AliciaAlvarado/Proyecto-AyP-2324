import csv
import os

class Arma:
    lista_armas = []

    def __init__(self, id, nombre, modelo, fabricante, costo_en_creditos, longitud, tipo, descripcion, peliculas):
        self.id = id
        self.nombre = nombre
        self.modelo = modelo
        self.fabricante = fabricante
        self.costo_en_creditos = costo_en_creditos
        self.longitud = longitud
        self.tipo = tipo
        self.descripcion = descripcion
        self.peliculas = peliculas



def cargar_armas_desde_csv():
    Arma.lista_armas = []
    ruta_csv = os.path.join(os.path.dirname(__file__), 'csv', 'weapons.csv')
    with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            a = Arma(
                id=fila['id'],
                nombre=fila['name'],
                modelo=fila['model'],
                fabricante=fila['manufacturer'],
                costo_en_creditos=fila['cost_in_credits'],
                longitud=fila['length'],
                tipo=fila['type'],
                descripcion=fila['description'],
                peliculas=fila['films']
            )
            Arma.lista_armas.append(a)
    
    print('Armas cargadas del CSV exitosamente')


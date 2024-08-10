import requests
import csv
import os

class Nave:
    lista_naves = []

    def __init__(self, nombre, modelo, fabricante, costo_en_creditos, longitud, velocidad_maxima, tripulacion, pasajeros, capacidad_carga, consumibles, hiperimpulsor, MGLT, clase, pilotos, peliculas, url, creado, editado):
        self.nombre = nombre
        self.modelo = modelo
        self.fabricante = fabricante
        self.costo_en_creditos = costo_en_creditos
        self.longitud = longitud
        self.velocidad_maxima = velocidad_maxima
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
        self.capacidad_carga = capacidad_carga
        self.consumibles = consumibles
        self.hiperimpulsor = hiperimpulsor
        self.MGLT = MGLT
        self.clase = clase
        self.pilotos = pilotos
        self.peliculas = peliculas
        self.url = url
        self.creado = creado
        self.editado = editado
    
    @property
    def episodios(self):
        return self.peliculas

    def __repr__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Modelo: {self.modelo}\n"
                f"Fabricante: {self.fabricante}\n"
                f"Costo en créditos: {self.costo_en_creditos}\n"
                f"Longitud: {self.longitud}\n"
                f"Velocidad máxima: {self.velocidad_maxima}\n"
                f"Tripulación: {self.tripulacion}\n"
                f"Pasajeros: {self.pasajeros}\n"
                f"Capacidad de carga: {self.capacidad_carga}\n"
                f"Consumibles: {self.consumibles}\n"
                f"Hiperimpulsor: {self.hiperimpulsor}\n"
                f"MGLT: {self.MGLT}\n"
                f"Clase: {self.clase}\n"
                f"Pilotos: {', '.join(self.pilotos)}\n"
                f"Películas: {', '.join(self.peliculas)}\n"
                f"URL: {self.url}\n"
                f"Creado: {self.creado}\n"
                f"Editado: {self.editado}\n")

def cargar_nombres_de_urls(urls): # Funcion inutilizada permanece por si acaso
    nombres = []
    for url in urls:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            nombres.append(datos['result']['properties']['name'])
    return nombres

def cargar_naves():
    Nave.lista_naves = []
    url_api = "https://www.swapi.tech/api/starships"
    while url_api:
        respuesta = requests.get(url_api)
        datos = respuesta.json()
        for nave in datos['results']:
            detalles_respuesta = requests.get(nave['url'])
            detalles = detalles_respuesta.json()['result']['properties']

            n = Nave(
                nombre=detalles['name'],
                modelo=detalles['model'],
                fabricante=detalles['manufacturer'],
                costo_en_creditos=detalles['cost_in_credits'],
                longitud=detalles['length'],
                velocidad_maxima=detalles['max_atmosphering_speed'],
                tripulacion=detalles['crew'],
                pasajeros=detalles['passengers'],
                capacidad_carga=detalles['cargo_capacity'],
                consumibles=detalles['consumables'],
                hiperimpulsor=detalles['hyperdrive_rating'],
                MGLT=detalles['MGLT'],
                clase=detalles['starship_class'],
                pilotos=detalles['pilots'],  # List of URLs
                peliculas=detalles.get('films', []),  # List of URLs
                url=detalles['url'],
                creado=detalles['created'],
                editado=detalles['edited']
            )
            Nave.lista_naves.append(n)
        
        url_api = datos.get('next')

def cargar_naves_desde_csv():
    Nave.lista_naves = []
    ruta_csv = os.path.join(os.path.dirname(__file__), 'csv', 'starships.csv')
    with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            n = Nave(
                nombre=fila['name'], 
                modelo=fila['model'],
                fabricante=fila['manufacturer'],
                costo_en_creditos=fila['cost_in_credits'], 
                longitud=fila['length'], 
                velocidad_maxima=fila['max_atmosphering_speed'], 
                tripulacion=fila['crew'], 
                pasajeros=fila['passengers'], 
                capacidad_carga=fila['cargo_capacity'], 
                consumibles=fila['consumables'], 
                hiperimpulsor=fila['hyperdrive_rating'], 
                MGLT=fila['MGLT'], 
                clase=fila['starship_class'], 
                pilotos=fila['pilots'].split(';') if fila['pilots'] else [],
                peliculas=fila['films'].split(';') if fila['films'] else [],
                url=None,
                creado=None,
                editado=None
            )
            Nave.lista_naves.append(n)
    
    print('Naves cargadas del CSV exitosamente')

if __name__ == "__main__":
    # Para cargar desde la API
    # cargar_naves()
    
    # Para cargar desde el CSV
    cargar_naves_desde_csv()
    
    # Imprimir naves cargadas
    for nave in Nave.lista_naves:
        print(nave)
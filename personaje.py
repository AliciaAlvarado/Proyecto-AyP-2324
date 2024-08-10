import requests
import csv
import os

class Personaje:
    lista_personajes = []

    def __init__(self, nombre, nacimiento, color_ojos, genero, color_cabello, altura, peso, color_piel, planeta_origen, peliculas, naves, vehiculos, especie, url, creado, editado):
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.color_ojos = color_ojos
        self.genero = genero
        self.color_cabello = color_cabello
        self.altura = altura
        self.peso = peso
        self.color_piel = color_piel
        self.planeta_origen = planeta_origen
        self.peliculas = peliculas
        self.naves = naves
        self.vehiculos = vehiculos
        self.especie = especie
        self.url = url
        self.creado = creado
        self.editado = editado
    
    @property
    def episodios(self):
        return self.peliculas

    def __repr__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Nacimiento: {self.nacimiento}\n"
                f"Color de ojos: {self.color_ojos}\n"
                f"Género: {self.genero}\n"
                f"Color de cabello: {self.color_cabello}\n"
                f"Altura: {self.altura}\n"
                f"Peso: {self.peso}\n"
                f"Color de piel: {self.color_piel}\n"
                f"Planeta de origen: {self.planeta_origen}\n"
                f"Películas: {', '.join(self.peliculas)}\n"
                f"Naves: {', '.join(self.naves)}\n"
                f"Vehículos: {', '.join(self.vehiculos)}\n"
                f"Especie: {self.especie}\n"
                f"URL: {self.url}\n"
                f"Creado: {self.creado}\n"
                f"Editado: {self.editado}\n")

def cargar_nombres_de_urls(urls):
    nombres = []
    for url in urls:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            nombres.append(datos['result']['properties']['name'])
    return nombres

def cargar_personajes():
    Personaje.lista_personajes = []
    url_api = "https://www.swapi.tech/api/people"
    while url_api:
        respuesta = requests.get(url_api)
        datos = respuesta.json()
        for personaje in datos['results']:
            detalles_respuesta = requests.get(personaje['url'])
            detalles = detalles_respuesta.json()['result']['properties']
            
            p = Personaje(
                nombre=detalles['name'],
                nacimiento=detalles['birth_year'],
                color_ojos=detalles['eye_color'],
                genero=detalles['gender'],
                color_cabello=detalles['hair_color'],
                altura=detalles['height'],
                peso=detalles['mass'],
                color_piel=detalles['skin_color'],
                planeta_origen= detalles['homeworld'],
                peliculas=[],
                naves=[],
                vehiculos=[],
                especie=[],
                url=personaje['url'],
                creado=None,
                editado=None
            )
            Personaje.lista_personajes.append(p)
        
        url_api = datos.get('next')

def cargar_personajes_desde_csv():
    Personaje.lista_personajes = []
    ruta_csv = os.path.join(os.path.dirname(__file__), 'csv', 'characters.csv')
    with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            p = Personaje(
                nombre=fila['name'],
                nacimiento=fila['year_born'],
                color_ojos=fila['eye_color'],
                genero=fila['gender'],
                color_cabello=fila['hair_color'],
                altura=fila['height'],
                peso=fila['weight'],
                color_piel=fila['skin_color'],
                planeta_origen=fila['homeworld'],
                peliculas=None,
                naves=None,
                vehiculos=None,
                especie=None,
                url=None,
                creado=None,
                editado=None
            )
            Personaje.lista_personajes.append(p)
    print('Personajes cargados exitosamente desde el csv')

if __name__ == "__main__":
    # Para cargar desde la API
    # cargar_personajes()
    
    # Para cargar desde el CSV
    cargar_personajes_desde_csv()
    
    # Imprimir personajes cargados
    for personaje in Personaje.lista_personajes:
        print(personaje)

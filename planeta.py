import requests
import csv
import os

class Planeta:
    lista_planetas = []

    def __init__(self, nombre, clima, diametro, gravedad, periodo_orbital, poblacion, periodo_rotacion, terreno, agua_superficial, url, creado, editado, residentes, peliculas):
        self.nombre = nombre
        self.clima = clima
        self.diametro = diametro
        self.gravedad = gravedad
        self.periodo_orbital = periodo_orbital
        self.poblacion = poblacion
        self.periodo_rotacion = periodo_rotacion
        self.terreno = terreno
        self.agua_superficial = agua_superficial
        self.url = url
        self.creado = creado
        self.editado = editado
        self.residentes = []
        self.peliculas = []



def cargar_nombres_de_urls(urls):
    nombres = []
    for url in urls:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            nombres.append(datos['result']['properties']['name'])
    return nombres

def cargar_planetas():
    Planeta.lista_planetas = []
    url_api = "https://www.swapi.tech/api/planets"
    while url_api:
        respuesta = requests.get(url_api)
        datos = respuesta.json()
        for planeta in datos['results']:
            detalles_respuesta = requests.get(planeta['url'])
            detalles = detalles_respuesta.json()['result']['properties']
            p = Planeta(
                nombre=detalles['name'],
                clima=detalles['climate'],
                diametro=detalles['diameter'],
                gravedad=detalles['gravity'],
                periodo_orbital=detalles['orbital_period'],
                poblacion=detalles['population'],
                periodo_rotacion=detalles['rotation_period'],
                terreno=detalles['terrain'],
                agua_superficial=detalles['surface_water'],
                url=detalles['url'],
                creado=detalles['created'],
                editado=detalles['edited'],
                residentes=[],
                peliculas = []
            )
            Planeta.lista_planetas.append(p)
        
        url_api = datos.get('next')

def cargar_planetas_desde_csv():
    Planeta.lista_planetas = []
    ruta_csv = os.path.join(os.path.dirname(__file__), 'csv', 'planets.csv')
    with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            p = Planeta(
                nombre=fila['name'],
                clima=fila['climate'],
                diametro=fila['diameter'],
                gravedad=fila['gravity'],
                periodo_orbital=fila['orbital_period'],
                poblacion=fila['population'],
                periodo_rotacion=fila['rotation_period'],
                terreno=fila['terrain'],
                agua_superficial=fila['surface_water'],
                residentes=fila['residents'].split(';') if fila['residents'] else [],
                peliculas=fila['films'].split(';') if fila['films'] else [],
                url=None,
                creado=None,
                editado=None
            )
            Planeta.lista_planetas.append(p)
    
    print('Planetas cargados del CSV exitosamente')



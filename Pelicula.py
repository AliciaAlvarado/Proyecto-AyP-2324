import requests

class Pelicula:
    lista_peliculas = []

    def __init__(self, titulo, episodio, introduccion, director, productor, fecha_lanzamiento, especies, naves, vehiculos, personajes, planetas, url, creado, editado):
        self.titulo = titulo
        self.episodio = episodio
        self.introduccion = introduccion
        self.director = director
        self.productor = productor
        self.fecha_lanzamiento = fecha_lanzamiento
        self.especies = especies
        self.naves = naves
        self.vehiculos = vehiculos
        self.personajes = personajes
        self.planetas = planetas
        self.url = url
        self.creado = creado
        self.editado = editado

def __repr__(self):
        return f"Pelicula(titulo={self.titulo}, episodio={self.episodio}, introduccion={self.introduccion}, director={self.director}, productor={self.productor}, fecha_lanzamiento={self.fecha_lanzamiento}, especies={self.especies}, naves={self.naves}, vehiculos={self.vehiculos}, personajes={self.personajes}, planetas={self.planetas}, url={self.url}, creado={self.creado}, editado={self.editado})"

def cargar_nombres_de_urls(urls):
    nombres = []
    for url in urls:
        respuesta = requests.get(url)
        datos = respuesta.json()
        nombres.append(datos['result']['properties']['name'])
    return nombres

def cargar_peliculas():
    url_api = "https://www.swapi.tech/api/films"
    respuesta = requests.get(url_api)
    datos = respuesta.json()
    for pelicula in datos['result']:
        detalles = pelicula['properties']
        p = Pelicula(
            titulo=detalles['title'],
            episodio=detalles['episode_id'],
            introduccion=detalles['opening_crawl'],
            director=detalles['director'],
            productor=detalles['producer'],
            fecha_lanzamiento=detalles['release_date'],
            especies=cargar_nombres_de_urls(detalles['species']),
            naves=cargar_nombres_de_urls(detalles['starships']),
            vehiculos=cargar_nombres_de_urls(detalles['vehicles']),
            personajes=cargar_nombres_de_urls(detalles['characters']),
            planetas=cargar_nombres_de_urls(detalles['planets']),
            url=detalles['url'],
            creado=detalles['created'],
            editado=detalles['edited']
        )
        Pelicula.lista_peliculas.append(p)
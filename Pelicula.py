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
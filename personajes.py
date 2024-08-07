import requests

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
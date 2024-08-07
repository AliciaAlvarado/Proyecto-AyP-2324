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

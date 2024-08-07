import requests

class Planeta:
    lista_planetas = []

    def __init__(self, nombre, diametro, periodo_rotacion, periodo_orbita, gravedad, poblacion, clima, terreno, agua_superficial, residentes, peliculas, url, creado, editado):
        self.nombre = nombre
        self.diametro = diametro
        self.periodo_rotacion = periodo_rotacion
        self.periodo_orbita = periodo_orbita
        self.gravedad = gravedad
        self.poblacion = poblacion
        self.clima = clima
        self.terreno = terreno
        self.agua_superficial = agua_superficial
        self.residentes = residentes
        self.peliculas = peliculas
        self.url = url
        self.creado = creado
        self.editado = editado

    @property
    def habitantes(self):
        return self.poblacion

    def __repr__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Diámetro: {self.diametro}\n"
                f"Periodo de rotación: {self.periodo_rotacion}\n"
                f"Periodo de órbita: {self.periodo_orbita}\n"
                f"Gravedad: {self.gravedad}\n"
                f"Población: {self.poblacion}\n"
                f"Clima: {self.clima}\n"
                f"Terreno: {self.terreno}\n"
                f"Agua superficial: {self.agua_superficial}\n"
                f"Residentes: {', '.join(self.residentes)}\n"
                f"Películas: {', '.join(self.peliculas)}\n"
                f"URL: {self.url}\n"
                f"Creado: {self.creado}\n"
                f"Editado: {self.editado}\n")
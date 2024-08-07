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

def cargar_nombres_de_urls(urls):
    nombres = []
    for url in urls:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            nombres.append(datos['result']['properties']['name'])
    return nombres

def cargar_planetas():
    url_api = "https://www.swapi.tech/api/planets"
    while url_api:
        respuesta = requests.get(url_api)
        datos = respuesta.json()
        for planeta in datos['results']:
            detalles_respuesta = requests.get(planeta['url'])
            detalles = detalles_respuesta.json()['result']['properties']
            
            p = Planeta(
                nombre=detalles['name'],
                diametro=detalles['diameter'],
                periodo_rotacion=detalles['rotation_period'],
                periodo_orbita=detalles['orbital_period'],
                gravedad=detalles['gravity'],
                poblacion=detalles['population'],
                clima=detalles['climate'],
                terreno=detalles['terrain'],
                agua_superficial=detalles['surface_water'],
                residentes=cargar_nombres_de_urls(detalles['residents']) if 'residents' in detalles else [],
                peliculas=cargar_nombres_de_urls(detalles['films']) if 'films' in detalles else [],
                url=detalles['url'],
                creado=detalles['created'],
                editado=detalles['edited']
            )
            Planeta.lista_planetas.append(p)
        
        url_api = datos.get('next')

if __name__ == "__main__":
    cargar_planetas()

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

def cargar_personajes():
    url_api = "https://www.swapi.tech/api/people"
    while url_api:
        respuesta = requests.get(url_api)
        datos = respuesta.json()
        for personaje in datos['results']:
            detalles_respuesta = requests.get(personaje['url'])
            detalles = detalles_respuesta.json()['result']['properties']
            
            planeta_origen = None
            if detalles['homeworld']:
                planeta_respuesta = requests.get(detalles['homeworld'])
                planeta_origen = planeta_respuesta.json()['result']['properties']['name']

            especies = cargar_nombres_de_urls(detalles['species']) if 'species' in detalles else ["Desconocido"]
            especie = especies[0] if especies else "Desconocido"

            p = Personaje(
                nombre=detalles['name'],
                nacimiento=detalles['birth_year'],
                color_ojos=detalles['eye_color'],
                genero=detalles['gender'],
                color_cabello=detalles['hair_color'],
                altura=detalles['height'],
                peso=detalles['mass'],
                color_piel=detalles['skin_color'],
                planeta_origen=planeta_origen,
                peliculas=cargar_nombres_de_urls(detalles['films']) if 'films' in detalles else [],
                naves=cargar_nombres_de_urls(detalles['starships']) if 'starships' in detalles else [],
                vehiculos=cargar_nombres_de_urls(detalles['vehicles']) if 'vehicles' in detalles else [],
                especie=especie,
                url=detalles['url'],
                creado=detalles['created'],
                editado=detalles['edited']
            )
            Personaje.lista_personajes.append(p)
        
        url_api = datos.get('next')

if __name__ == "__main__":
    cargar_personajes()
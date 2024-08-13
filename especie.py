import requests

class Especie:
    lista_especies = []

    def __init__(self, nombre, clasificacion, designacion, altura, esperanza_vida, colores_ojos, colores_cabello, colores_piel, lengua, planeta_origen, personajes, url, creado, editado):
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.designacion = designacion
        self.altura = altura
        self.esperanza_vida = esperanza_vida
        self.colores_ojos = colores_ojos
        self.colores_cabello = colores_cabello
        self.colores_piel = colores_piel
        self.lengua = lengua
        self.planeta_origen = planeta_origen
        self.personajes = personajes
        self.url = url
        self.creado = creado
        self.editado = editado
        self.peliculas = None

    @property
    def peliculas_relacionadas(self):
        return self.peliculas

    def __repr__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Clasificación: {self.clasificacion}\n"
                f"Designación: {self.designacion}\n"
                f"Altura: {self.altura}\n"
                f"Esperanza de vida: {self.esperanza_vida}\n"
                f"Colores de ojos: {', '.join(self.colores_ojos)}\n"
                f"Colores de cabello: {', '.join(self.colores_cabello)}\n"
                f"Colores de piel: {', '.join(self.colores_piel)}\n"
                f"Lengua: {self.lengua}\n"
                f"Planeta de origen: {self.planeta_origen}\n"
                f"Personajes: {', '.join(self.personajes)}\n"
                f"Peliculas: {self.peliculas_relacionadas}"
                f"Episodios: {', '.join(self.episodios)}\n"
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

def cargar_especies():
    url_api = "https://www.swapi.tech/api/species"
    while url_api:
        respuesta = requests.get(url_api)
        datos = respuesta.json()
        for especie in datos['results']:
            detalles_respuesta = requests.get(especie['url'])
            detalles = detalles_respuesta.json()['result']['properties']
           
            e = Especie(
                nombre=detalles.get['name'],
                clasificacion=detalles.get['classification'],
                designacion=detalles.get['designation'],
                altura=detalles.get['average_height'],
                esperanza_vida=detalles.get['average_lifespan'],
                colores_ojos=detalles.get['eye_colors'],
                colores_cabello=detalles.get['hair_colors'],
                colores_piel=detalles.get['skin_colors'],
                lengua=detalles.get['language'],
                planeta_origen=detalles.get['homeworld'],
                personajes=detalles.get['people'],
                url=detalles.get['url'],
                creado=detalles.get['created'],
                editado=detalles.get['edited']
                peliculas = None
            )
            Especie.lista_especies.append(e)
        
        url_api = datos.get('next')

if __name__ == "__main__":
    cargar_especies()

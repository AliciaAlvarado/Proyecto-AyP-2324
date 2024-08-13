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
        self.peliculas = []

    
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
                nombre=detalles['name'],
                clasificacion=detalles['classification'],
                designacion=detalles['designation'],
                altura=detalles['average_height'],
                esperanza_vida=detalles['average_lifespan'],
                colores_ojos=detalles['eye_colors'],
                colores_cabello=detalles['hair_colors'],
                colores_piel=detalles['skin_colors'],
                lengua=detalles['language'],
                planeta_origen=detalles['homeworld'],
                personajes=detalles['people'],
                url=detalles['url'],
                creado=detalles['created'],
                editado=detalles['edited'],
                peliculas = None
            )
            Especie.lista_especies.append(e)
        
        url_api = datos.get('next')



import requests

class Nave:
    lista_naves = []

    def __init__(self, nombre, modelo, clase, fabricante, costo_creditos, longitud, tripulacion, pasajeros, velocidad_atmosfera, hiperimpulsor, mglt, capacidad_carga, consumibles, pilotos, peliculas, url, creado, editado):
        self.nombre = nombre
        self.modelo = modelo
        self.clase = clase
        self.fabricante = fabricante
        self.costo_creditos = costo_creditos
        self.longitud = longitud
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
        self.velocidad_atmosfera = velocidad_atmosfera
        self.hiperimpulsor = hiperimpulsor
        self.mglt = mglt
        self.capacidad_carga = capacidad_carga
        self.consumibles = consumibles
        self.pilotos = pilotos
        self.peliculas = peliculas
        self.url = url
        self.creado = creado
        self.editado = editado

    def __repr__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Modelo: {self.modelo}\n"
                f"Clase: {self.clase}\n"
                f"Fabricante: {self.fabricante}\n"
                f"Costo en créditos: {self.costo_creditos}\n"
                f"Longitud: {self.longitud}\n"
                f"Tripulación: {self.tripulacion}\n"
                f"Pasajeros: {self.pasajeros}\n"
                f"Velocidad en atmósfera: {self.velocidad_atmosfera}\n"
                f"Hiperimpulsor: {self.hiperimpulsor}\n"
                f"MGLT: {self.mglt}\n"
                f"Capacidad de carga: {self.capacidad_carga}\n"
                f"Consumibles: {self.consumibles}\n"
                f"Pilotos: {', '.join(self.pilotos)}\n"
                f"Películas: {', '.join(self.peliculas)}\n"
                f"URL: {self.url}\n"
                f"Creado: {self.creado}\n"
                f"Editado: {self.editado}\n")

def cargar_naves():
    url_api = "https://www.swapi.tech/api/starships"
    while url_api:
        respuesta = requests.get(url_api)
        datos = respuesta.json()
        for nave in datos['results']:
            detalles_respuesta = rnave['url'])
            detalles = detalles_respuesta.json()['result']['properties']

            n = Nave(
                nombre=detalles['name'],
                modelo=detalles['model'],
                clase=detalles['starship_class'],
                fabricante=detalles['manufacturer'],
                costo_creditos=detalles['cost_in_credits'],
                longitud=detalles['length'].replace(',', ''),  # Eliminar comas para convertir a float
                tripulacion=detalles['crew'],
                pasajeros=detalles['passengers'],
                velocidad_atmosfera=detalles['max_atmosphering_speed'],
                hiperimpulsor=detalles.get('hyperdrive_rating', '0'),  # Usar '0' si no está disponible
                mglt=detalles.get('MGLT', '0'),  # Usar '0' si no está disponible
                capacidad_carga=detalles['cargo_capacity'],
                consumibles=detalles['consumables'],
                pilotos=cargar_nombres_de_urls(detalles.get('pilots', [])),
                peliculas=cargar_nombres_de_urls(detalles.get('films', [])),
                url=detalles['url'],
                creado=detalles['created'],
                editado=detalles['edited']
            )
            Nave.lista_naves.append(n)
        url_api = datos['next']

def cargar_nombres_de_urls(urls):
    nombres = []
    for url in urls:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            nombres.append(datos['result']['properties']['name'])
    return nombres

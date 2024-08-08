import requests

class Vehiculo:
    lista_vehiculos = []

    def __init__(self, nombre, modelo, clase, fabricante, longitud, costo, tripulacion, pasajeros, velocidad_maxima, capacidad_carga, consumibles, peliculas, pilotos, url, creado, editado):
        self.nombre = nombre
        self.modelo = modelo
        self.clase = clase
        self.fabricante = fabricante
        self.longitud = longitud
        self.costo = costo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
        self.velocidad_maxima = velocidad_maxima
        self.capacidad_carga = capacidad_carga
        self.consumibles = consumibles
        self.peliculas = peliculas
        self.pilotos = pilotos
        self.url = url
        self.creado = creado
        self.editado = editado

    def __repr__(self):
        return f"Vehiculo(nombre={self.nombre}, modelo={self.modelo}, clase={self.clase}, fabricante={self.fabricante}, longitud={self.longitud}, costo={self.costo}, tripulacion={self.tripulacion}, pasajeros={self.pasajeros}, velocidad_maxima={self.velocidad_maxima}, capacidad_carga={self.capacidad_carga}, consumibles={self.consumibles}, peliculas={self.peliculas}, pilotos={self.pilotos}, url={self.url}, creado={self.creado}, editado={self.editado})"

def cargar_nombres_de_urls(urls):
    nombres = []
    for url in urls:
        respuesta = requests.get(url)
        datos = respuesta.json()
        nombres.append(datos['result']['properties']['name'])
    return nombres

def cargar_vehiculos():
    url_api = "https://www.swapi.tech/api/vehicles"
    while url_api:
        respuesta = requests.get(url_api)
        datos = respuesta.json()
        for vehiculo in datos['results']:
            detalles_respuesta = requests.get(vehiculo['url'])
            detalles = detalles_respuesta.json()['result']['properties']
            p = Vehiculo(
                nombre=detalles['name'],
                modelo=detalles['model'],
                clase=detalles['vehicle_class'],
                fabricante=detalles['manufacturer'],
                longitud=int(detalles['length'].replace(',', '')) if detalles['length'].replace(',', '').isdigit() else 0,
                costo=int(detalles['cost_in_credits']) if detalles['cost_in_credits'].isdigit() else 0,
                tripulacion=detalles['crew'],
                pasajeros=detalles['passengers'],
                velocidad_maxima=detalles['max_atmosphering_speed'],
                capacidad_carga=detalles['cargo_capacity'],
                consumibles=detalles['consumables'],
                peliculas=cargar_nombres_de_urls(detalles['films']) if 'films' in detalles else [],
                pilotos=cargar_nombres_de_urls(detalles['pilots']) if 'pilots' in detalles else [],
                url=detalles['url'],
                creado=detalles['created'],
                editado=detalles['edited']
            )
            Vehiculo.lista_vehiculos.append(p)
        url_api = datos['next']

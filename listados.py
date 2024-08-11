from pelicula import Pelicula
from personaje import Personaje
from planeta import Planeta
from especie import Especie
from nave import Nave
from vehiculo import Vehiculo

def listar_peliculas():
    for pelicula in Pelicula.lista_peliculas:
        print(f"Título: {pelicula.titulo}")
        print(f"Episodio: {pelicula.episodio}")
        print(f"Fecha de lanzamiento: {pelicula.fecha_lanzamiento}")
        print(f"Introducción: {pelicula.introduccion}")
        print(f"Director: {pelicula.director}")
        print("="*40)

def listar_especies():

    for especie in Especie.lista_especies:
        print(f"Nombre: {especie.nombre}")
        print(f"Altura: {especie.altura}")
        print(f"Clasificación: {especie.clasificacion}")
        
        homeworld_name = next((planeta.nombre for planeta in Planeta.lista_planetas if planeta.url == especie.planeta_origen), "Unknown")
        print(f"Planeta origen: {homeworld_name}")
        print(f"Lengua: {especie.lengua}")
        nombres_personajes = [persona.nombre for persona in Personaje.lista_personajes if persona.url in especie.personajes]
        print(f"Personajes: {', '.join(nombres_personajes) if nombres_personajes else 'None'}")

        peliculas = [f"{pelicula.titulo}, episodio {pelicula.episodio}" for pelicula in Pelicula.lista_peliculas if especie.url in pelicula.especies]
        print(f"Episodes: {', '.join(peliculas) if peliculas else 'None'}")

        print("="*40)

def listar_planetas():
    for planeta in Planeta.lista_planetas:
        print(f"Nombre: {planeta.nombre}")
        print(f"Período de órbita: {planeta.periodo_orbital}")
        print(f"Período de rotación: {planeta.periodo_rotacion}")
        print(f"Cantidad de habitantes: {planeta.poblacion}")
        print(f"Clima: {planeta.clima}")

        nombres_personajes = [persona.nombre for persona in Personaje.lista_personajes if persona.planeta_origen == planeta.url]
        print(f"Personajes: {', '.join(nombres_personajes) if nombres_personajes else 'None'}")

        peliculas = [f"{pelicula.titulo}, episode {pelicula.episodio}" for pelicula in Pelicula.lista_peliculas if planeta.url in pelicula.planetas]
        print(f"Peliculas: {', '.join(peliculas) if peliculas else 'None'}")

        print("="*40)

def buscar_personaje():
    cadena = input("Ingrese el nombre del personaje a buscar: ")
    for personaje in Personaje.lista_personajes:
        if cadena.lower() in personaje.nombre.lower():
            print(f"Nombre: {personaje.nombre}")
            planeta_Origen = next((planeta.nombre for planeta in Planeta.lista_planetas if planeta.url == personaje.planeta_origen), "Unknown")
            print(f"Planeta de origen: {planeta_Origen}")

            peliculas = [f"{pelicula.titulo}, episode {pelicula.episodio}" for pelicula in Pelicula.lista_peliculas if personaje.url in pelicula.personajes]
            print(f"Episodes: {', '.join(peliculas) if peliculas else 'None'}")

            print(f"Género: {personaje.genero}")

            nombre_especie = next((especie.nombre for especie in Especie.lista_especies if personaje.url in especie.personajes), "Unknown")
            print(f"Species: {nombre_especie}")

            naves = [nave.nombre for nave in Nave.lista_naves if personaje.url in nave.pilotos]
            print(f"Naves: {', '.join(naves) if naves else 'None'}")

            vehiculos = [vehiculo.nombre for vehiculo in Vehiculo.lista_vehiculos if personaje.url in vehiculo.pilotos]
            print(f"Vehicles: {', '.join(vehiculos) if vehiculos else 'None'}")

            print("="*40)

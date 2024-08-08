from pelicula import Pelicula
from personaje import Personaje
from planeta import Planeta
from especie import Especie

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
        print(f"Planeta de origen: {especie.planeta_origen}")
        print(f"Lengua: {especie.lengua}")
        print(f"Personajes: {', '.join(especie.personajes)}")
        print(f"Episodios: {', '.join(especie.episodios)}")
        print("="*40)

def listar_planetas():
    for planeta in Planeta.lista_planetas:
        print(f"Nombre: {planeta.nombre}")
        print(f"Período de órbita: {planeta.periodo_orbita}")
        print(f"Período de rotación: {planeta.periodo_rotacion}")
        print(f"Cantidad de habitantes: {planeta.habitantes}")
        print(f"Clima: {planeta.clima}")
        print(f"Episodios: {', '.join(planeta.peliculas)}")
        print(f"Personajes: {', '.join(planeta.residentes)}")
        print("="*40)

def buscar_personaje():
    cadena = input("Ingrese el nombre del personaje a buscar: ")
    for personaje in Personaje.lista_personajes:
        if cadena.lower() in personaje.nombre.lower():
            print(f"Nombre: {personaje.nombre}")
            print(f"Planeta de origen: {personaje.planeta_origen}")
            print(f"Episodios: {', '.join(personaje.episodios)}")
            print(f"Género: {personaje.genero}")
            print(f"Especie: {personaje.especie}")
            print(f"Naves: {', '.join(personaje.naves)}")
            print(f"Vehículos: {', '.join(personaje.vehiculos)}")
            print("="*40)

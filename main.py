from pelicula import cargar_peliculas, Pelicula
from personaje import cargar_personajes, Personaje, cargar_personajes_desde_csv
from planeta import cargar_planetas, Planeta, cargar_planetas_desde_csv
from nave import cargar_naves, Nave, cargar_naves_desde_csv
from arma import Arma, cargar_armas_desde_csv
from vehiculo import cargar_vehiculos, Vehiculo
from especie import cargar_especies, Especie
from estadisticas import grafico_personajes_por_planeta, grafico_caracteristicas_naves, estadisticas_naves
from listados import listar_peliculas, listar_especies, listar_planetas, buscar_personaje
from misiones import *
import json

def menu_principal():
    while True:
        print("\nBienvenido a tu mundo de Star Wars!")
        print("\nQue la fuerza te acompañe!")
        print("Seleccione qué desea realizar:")
        print("1. Ver informacion de star wars")
        print("2. Ver estadísticas galácticas")
        print("3. Gestionar misiones intergalácticas")
        print("4. Salir de la aplicacion ")

        seleccion = input("-----> ")

        if seleccion == "1":
            menu_listados()
        elif seleccion == "2":
            menu_estadisticas()
        elif seleccion == "3":
            menu_misiones()
        elif seleccion == "4":
            print("Hasta pronto.")
            break
        else:
            print("ERROR - Seleccion invalida, por favor intente de nuevo")
        
def menu_listados():
    cargar_peliculas()
    print('Películas cargadas del api')
    cargar_personajes()
    print('Personajes cargados del api')
    cargar_planetas()
    print('Planetas cargados del api')
    cargar_naves()
    print('Naves cargadas del api')
    cargar_vehiculos()
    print('Vehículos cargados del api')
    cargar_especies()
    print('Especies cargadas del api')


    while True:
        print("\nSeleccione que desea hacer:")
        print("1. Ver el listado de Películas")
        print("2. Ver el listado de Especies")
        print("3. Ver el listado de Planetas")
        print("4. Buscar un personaje por su nombre")
        print("5. Volver al menú principal")

        seleccion = input("-----> ")

        if seleccion == "1":
            listar_peliculas()
        elif seleccion == "2":
            listar_especies()
        elif seleccion == "3":
            listar_planetas()
        elif seleccion == "4":
            buscar_personaje()
        elif seleccion == "5":
            break
        else:
            print("ERROR - Seleccion invalida, por favor intente de nuevo")

def menu_estadisticas():
    cargar_armas_desde_csv()
    cargar_naves_desde_csv()
    cargar_planetas_desde_csv()
    cargar_personajes_desde_csv()

    while True:
        print("\nSeleccione una opción del submenú de Estadísticas:")
        print("1. Gráfico de cantidad de personajes por planeta")
        print("2. Gráficos de características de naves")
        print("3. Estadísticas sobre naves")
        print("4. Volver al menú principal")

        seleccion = input("-----> ")

        if seleccion == "1":
            grafico_personajes_por_planeta()
        elif seleccion == "2":
            grafico_caracteristicas_naves()
        elif seleccion == "3":
            estadisticas_naves()
        elif seleccion == "4":
            break
        else:
            print("ERROR - Seleccion invalida, por favor intente de nuevo")

def menu_misiones():
    cargar_armas_desde_csv()
    cargar_naves_desde_csv()
    cargar_planetas_desde_csv()
    cargar_personajes_desde_csv()
    while True:
        print("\nSeleccione una opción del menú de misiones:")
        print("1. Construir una nueva misión")
        print("2. Modificar una misión existente")
        print("3. Ver misiones en el sistema")
        print("4. Guardar misiones del sistema en txt")
        print("5. Cargar misiones de txt")
        print("6. Regresar")
        
        seleccion = input("-----> ")

        if seleccion == "1":
            crear_nueva_mision()
        elif seleccion == "2":
            modificar_mision_existente()
        elif seleccion == "3":
            ver_detalles_mision()
        elif seleccion == "4":
            guardar_misiones_en_archivo()
        elif seleccion == "5":
            cargar_misiones_desde_archivo()
        elif seleccion == "6":
            break
        else:
            print("ERROR - Seleccion invalida, por favor intente de nuevo")

print('success')
menu_principal()
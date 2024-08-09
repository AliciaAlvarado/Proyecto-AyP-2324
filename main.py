from pelicula import cargar_peliculas, Pelicula
from personaje import cargar_personajes, Personaje
from planeta import cargar_planetas, Planeta
from nave import cargar_naves, Nave
from vehiculo import cargar_vehiculos, Vehiculo
from especie import cargar_especies, Especie
from listados import listar_peliculas, listar_especies, listar_planetas, buscar_personaje
from estadisticas import grafico_personajes_por_planeta, grafico_caracteristicas_naves, estadisticas_naves

def menu_principal():
    while True:
        print("\nBienvenido a tu a el mundo de Star Wars!")
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


cargar_peliculas()
print('Películas cargadas')
cargar_personajes()
print('Personajes cargados')
cargar_planetas()
print('Planetas cargados')
cargar_naves()
print('Naves cargadas')
cargar_vehiculos()
print('Vehículos cargados')
cargar_especies()
print('Especies cargadas')


print('success')
menu_principal()
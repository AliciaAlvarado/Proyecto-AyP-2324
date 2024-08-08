from pelicula import cargar_peliculas, Pelicula
from personaje import cargar_personajes, Personaje
from planeta import cargar_planetas, Planeta
from nave import cargar_naves, Nave
from vehiculo import cargar_vehiculos, Vehiculo
from especie import cargar_especies, Especie

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
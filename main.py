from claseSistAdopcion import Sistem_Adopcion
from clasePerro import Perro
from claseUserAdoptante import User_Adoptante


def main():

    sistem = Sistem_Adopcion()

    print("     ---------- Bienvenidos a ADOPDOG ---------- ")
    print("\n * Donde una nueva historia comienza con un ladrido *\n\n\nEn este sitio vas a encontrar perros que buscan un hogar.\nSon cariñosos,  únicos y están esperando una familia como la tuya.\nAdoptar es fácil y cambia vidas, la de ellos... y la tuya también.")
    while True:

        print("\n\nSeleccione la opcion deseada:\n\n.1 Cargar perro\n.2 Eliminiar perro\n.3 Registro de usuarios\n.4 Postular un perro\n.5 Confirmar una adopción\n.6 Preferencia de perros\n.7 Listado de perros\n.8 Salir")

    
        try:

            opcion = int(input("Ingrese 1/2/3/4/5/6/7/8:"))
            if opcion < 1 or opcion > 8:
                print("Por favor, ingrese un número del 1 al 8.")
                continue # para que vuelva a pedir la opción
        except ValueError:
            print("Entrada inválida. Ingrese un número valido del 1 al 8.")
            continue
    
        if opcion == 1:
            sistem.cargar_perro()
            
        elif opcion == 2:
            sistem.eliminar_perro()
        
        elif opcion == 3:
            sistem.registrar_user()
        
        elif opcion == 4:
            pass
        elif opcion == 5:
            sistem.confirmar_adop()
    
        elif opcion == 6:
            print("Filtrar perros por:\n\n1. Raza:\n2.Edad:\n3. Tamaño:")
            filtro = input("Ingrese 1/2/3:")
            if filtro == "1":
                valor = input("Ingrese la raza: ")
                result = sistem.preferencia_perro("raza", valor)
            elif filtro == "2":
                valor = input("Ingrese la edad (cachorro/joven/adulto): ")
                result = sistem.preferencia_perro("edad", valor)
            elif filtro == "3":
                valor = input("Ingrese el tamaño (pequeño/mediano/grande): ")
                result = sistem.preferencia_perro("tamaño", valor)
            else:
                print("Opción invalida")
                continue
            if not result:
                print("No hay perros con esas preferencias")
            else:
                print("Perros con sus preferncias")
                i = 1
                for perro in result:
                    print(f"{i}. ID: {perro.id}\nNombre: {perro.nombre}\nRaza: {perro.raza}\nEdad: {perro.edad}\nTamaño: {perro.tamano}\nPeso: {perro.peso}\nSalud: {perro.salud}\nVacunado: {perro.vacunado}\nEstado de adopción: {perro.estado_de_adopcion}\nTemperamento: {perro.temperamento}")
                    i = i + 1
            
        
        elif opcion == 7:
            sistem.listado_perro()
        
        elif opcion == 8:
            print("Gracias por visitarnos. Los esperamos nuevamente!!!")
            break
        



       




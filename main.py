from claseSistAdopcion import Sistem_Adopcion
from clasePerro import Perro
from claseUserAdoptante import User_Adoptante


def main():

    sistem = Sistem_Adopcion()

    print("     ---------- Bienvenidos a ADOPDOG ---------- ")
    print("\n * Donde una nueva historia comienza con un ladrido *\n\n\nEn este sitio vas a encontrar perros que buscan un hogar.\nSon cariñosos,  únicos y están esperando una familia como la tuya.\nAdoptar es fácil y cambia vidas, la de ellos... y la tuya también.")
    
    
    while True:

        print("\n\nSeleccione la opcion deseada:\n\n1. Cargar o eliminar perro\n2. Registro de usuarios\n3. Postular un perro\n4. Confirmar una adopción\n5. Preferencia de perros\n6. Listado de perros\n7. Salir")

    
        try:

            opcion = int(input("Ingrese 1/2/3/4/5/6/7:"))
            if opcion < 1 or opcion > 7:
                print("Por favor, ingrese un número del 1 al 7.")
                continue # para que vuelva a pedir la opción
        except ValueError:
            print("Entrada inválida. Ingrese un número valido del 1 al 7.")
            continue
    
        if opcion == 1:
            # Cargar un perro
            print("Para cargar un perro ingese c o e para eliminar un perro")
            eleccion = input("c/e").lower()
            if eleccion == "c":
                
                print("Ingrese los datos del perro:\n")
                nombre = input("Nombre:")
                raza = input("Raza:")
                edad = input("Edad(cachorro/joven/adulto):")
                tamano = input("Tamaño(pequeño/mediano/grande):")
                peso = input("Peso:")
                salud = input("Salud:")
                vacunado = input("Vacunado? (s/n):").lower()
                temperamento = input("Temperamento:")
                vacunado = True if vacunado == "s" else False
                
                new_perro = Perro(nombre, raza, edad, tamano, peso, salud, vacunado, temperamento)
                sistem.cargar_perro(new_perro)

                print("Se cargo correctamente", flush = True)

                # Eliminar un perro
            elif eleccion == "e":
                try:
                    id_perro = int(input("Ingrese el ID del perro a eliminar: "))
                    sistem.eliminar_perro(id_perro)
                except ValueError:
                    print("ID inválido.")

            else:
                print("Error. Ingrese c para cargar o e para eliminar", flush = True)
        
        elif opcion == 2:
            # Registrar usuario
            
            print("Ingrese nombre, dni y email para su registro:\n")
            nombre = input("Nombre:")
            dni = input("DNI:")
            email = input("Email:")

            print("\nPreferencias del perro:\n")
            raza = input("Raza preferida: ")
            edad = input("Edad preferida (cachorro/joven/adulto): ").lower()
            tamano = input("Tamaño preferido (pequeño/mediano/grande): ")

            preferencia = {"raza": raza, "edad": edad, "tamaño": tamano}
            new_usuario = User_Adoptante(nombre, dni, email, preferencia)
            sistem.registrar_user(new_usuario)
            
            print("Usuario registrado correctamente.", flush = True)
        
        elif opcion == 3:
            pass
        elif opcion == 4:
            # Confirmar una adopción
            try: 
                id_perro = int(input("Ingrese el ID del perro a adoptar"))
                sistem.confirmar_adop(id_perro)
            except ValueError:
                print("ID inválido", flush = True)
    
        elif opcion == 5:
            # Filtrar perros
            print("Filtrar perros por:\n\n1.Raza:\n2.Edad:\n3.Tamaño:")
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
                print("Opción invalida", flush = True)
                continue
            if not result:
                print("No hay perros con esas preferencias", flush = True)
            else:
                print("Perros con sus preferencias", flush = True)
                i = 1
                for perro in result:
                    print(f"{i}. ID: {perro.id}\nNombre: {perro.nombre}\nRaza: {perro.raza}\nEdad: {perro.edad}\nTamaño: {perro.tamano}\nPeso: {perro.peso}\nSalud: {perro.salud}\nVacunado: {perro.vacunado}\nEstado de adopción: {perro.estado_de_adopcion}\nTemperamento: {perro.temperamento}")
                    i = i + 1
            
        
        elif opcion == 6:
            # Listado de perros
            sistem.listado_perro()
        
        elif opcion == 7:
            print("Gracias por visitarnos. Los esperamos nuevamente!!!", flush = True)
            break
        



if __name__ == "__main__":
    main()




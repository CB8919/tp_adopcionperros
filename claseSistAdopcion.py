from claseUserAdoptante import User_Adoptante
from clasePerro import Perro

class Sistem_Adopcion():
    def __init__(self):
        self.list_usuario = []
        self.list_perro = []
        self.id_contador = 1
        

        # Método para agregar un nuevo perro a la lista de adopción
    def cargar_perro(self):
        

        print("----- Bienvenido -----\n\nIngrese los datos del perro")

        nombre = input("Nombre:")
        raza = input("Raza:")
        edad = int(input("Edad:"))
        tamano = input("Tamaño:")
        peso = float(input("Peso:"))
        estado_salud = input("Estado de salud:")
        vacunado = input("¿Vacunado? SI/NO:").upper()
        temperamento = input("Temperamento:")
        
        perro = Perro(id = self.id_contador, nombre = nombre, raza = raza, edad = edad, tamano = tamano, peso = peso, estado_salud = estado_salud, vacunado = vacunado, estado = "Disponible", temperamento = temperamento)

        self.list_perro.append(perro)
        self.id_contador = self.id_contador + 1
        
        print("Se registro el perro correctamente.")
        return perro
        

        # Método para eliminar un perro de la lista o ponerlo como adoptado
    def eliminar_perro(self):

        print("Ingrese el perro que desea eliminar\n")
        
        nombre = input("Nombre:")
        raza = input("Raza:")
        edad = int(input("Edad:"))
        tamano = input("Tamaño:")
        peso = float(input("Peso:"))
        estado_salud = input("Estado de salud:")
        vacunado = input("¿Vacunado? SI/NO:").upper()
        temperamento = input("Temperamento:")
        
        for perro in self.list_perro:
            if perro.nombre == nombre and perro.raza == raza and perro.edad == edad and perro.tamano == tamano and perro.peso == peso and perro.estado_salud == estado_salud and perro.vacunado.upper() == vacunado.upper() and perro.temperamento == temperamento:

                self.list_perro.remove(perro)
                print("Se elimino el perro")
                break
        else:
            print("No se encontro el perro con esos datos")

        return self.list_perro
        # Método para registrar un usuario en una base de datos
    def registrar_user(self):

        print("----- Bienvenido -----\n\nIngrese sus datos personales") #nombre, dni, email, preferencias

        nombre = input("Nombre:")
        dni = int(input("DNI(sin puntos):"))
        email = input("Email:")

        print("\nIngrese sus preferencias(raza, edad, tamaño)")
        raza = input("Raza:")
        edad = input("Edad (cachorro/joven/adulto):")
        tamano = input("Tamaño(pequño/mediano/grande)")

        preferencias = {
            "raza": raza,
            "edad": edad,
            "tamaño": tamano,
        }
        

        nuevo_usuario = User_Adoptante(nombre, dni, email, preferencias) 
        self.list_usuario.append(nuevo_usuario)
        print("Se registro el usuario correctamente")
        nuevo_usuario.mostrar_user()

        return nuevo_usuario

        # Método para cambiar el estado de un perro a adoptado
    def confirmar_adop(self):
        
        pass

        # Método para filtra preferncias del usuario a la hora de adoptar
    def preferncia_perro(self):
        filtrado = []
        print("----- Filtrado por raza, edad o tamaño -----")
        opcion = input("Ingrese la preferencia (raza, edad, tamaño): ").lower()
        valor = input("Ingrese el valor a buscar: ").lower()

        for perro in self.list_perro:
            if opcion == "raza" and perro.raza.lower() == valor:
                filtrado.append(perro)
            elif opcion == "edad" and perro.edad.lower() == valor:
                filtrado.append(perro)
            elif opcion == "tamaño" and perro.tamano.lower() == valor:
                filtrado.append(perro)

        return filtrado
                
        # Método que retorna o muestra una lista de perros disponibles con sus estados
    def listado_perro(self):
        disponible = []
        for perro in self.list_perro:
            if perro.estado == "Disponible":
                disponible.append(perro)
        return disponible
            
    

#r = Sistem_Adopcion()
#nuevo_perro = r.cargar_perro()
#print(nuevo_perro.mostrar_info())
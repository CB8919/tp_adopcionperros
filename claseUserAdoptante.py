class User_Adoptante(object):
    def __init__(self, nombre, dni, email, preferencias, histo_adop):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias # Raza, edad, tamaño
        self.histo_adop = histo_adop

    def mostrar_user(self):
        print(f"Nombre: {self.nombre}\nDNI: {self.dni}\nEmail: {self.email}\nPreferncias: {self.preferencias}\nHistorial de adopción: {self.historial()}")

        # Método para registrar a un usuario 
    def registro_user(self):
        print("---- REGISTRO DE USUARIO ----")
        
        print("Ingrese nombre, dni, email y preferncias.\nFavor de respetar el orden al ingresar los datos solicitados)")
        self.nombre = input("Nombre: ")
        self.dni = input("DNI: ")
        self.email = input("Email: ")

        print("Ingresar preferencias:")
        raza = input("Raza preferida: ")
        tamano = input("Tamaño preferido (grande, mediano, pequeño): ")
        edad = input("Edad preferida (cachorro, joven, adulto): ")

        self.preferencias = {
            "raza": raza,
            "tamaño": tamano,
            "edad": edad
        }
               
        
        print("\n----- Datos del usuario -----\n\n")
        print(f"Nombre: {self.nombre}\nDNI: {self.dni}\nEmail: {self.email}\nPreferncias: {self.preferencias}\nHistorial de adopción: {self.historial()}")

        # Método para modificar, actualizar o borrar los datos del usuario
    def modificar_datos(self):
        respuesta = "SI"
        while respuesta == "SI":
            print("Que dato desea modificar?")
            print("\nSeleccione:")  
            print("Nombre: 1\nDNI: 2\nEmail: 3\nPreferencias: 4")
            opcion = int(input("Opción:"))
        
        
            if opcion == 1:
                self.nombre = input("Nuevo Nombre: ")
            elif opcion == 2:
                self.dni = input("Nuevo DNI: ")
            elif opcion == 3:
                self.email = input("Nuevo email: ")
            elif opcion == 4:
                raza = input("Nueva raza: ")
                tamano = input("Nuevo tamaño: ")
                edad = input("Nueva edad:")

                self.preferencias = {
                    "raza": raza,
                    "tamaño": tamano,
                    "edad": edad
                }
            else:
                print("Porfavor ingrese 1, 2, 3 o 4 de lo contrario no podra modicar ningún dato")
    
            print("Quiere modificar otro dato?")
            respuesta = input("SI/NO").upper()

        # Método para mostrar su historial de adopción si lo tiene, o simplemente mostrar todos los datos del usuario
    def historial(self):
        if self.histo_adop != []:
            return "No hay adopciones realizadas"
        else:
            return "Historial de adopciones: "



#nuevo_usuario = User_Adoptante("", "", "", "", "")
#nuevo_usuario.registro_user()

#nuevo_usuario = User_Adoptante("Carlos", "32564789", "c@gmail.com", {"Labrador", "grande", "cachorro"}, ["Plaga"])
#nuevo_usuario.modificar_datos()
#nuevo_usuario.mostrar_user()
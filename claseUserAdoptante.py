class User_Adoptante(object):
    def __init__(self, nombre, dni, email, preferencias, histo_adop):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias # Raza, edad, tamaño
        self.histo_adop = histo_adop
        

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
        self.histo_adop = []

        usuario = User_Adoptante(self.nombre, self.dni, self.email, self.preferencias, self.histo_adop)

        return usuario

        # Método para modificar, actualizar o borrar los datos del usuario
    def modificar_datos(self):
        pass

        # Método para mostrar su historial de adopción si lo tiene, o simplemente mostrar todos los datos del usuario
    def historial(self):
        pass
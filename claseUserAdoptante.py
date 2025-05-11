class User_Adoptante(object):
    def __init__(self, nombre, dni, email, preferencias, histo_adop):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias # Raza, edad, tamaño
        self.histo_adop = histo_adop
        pass

        # Método para registrar a un usuario 
    def registro_user(self):
        pass

        # Método para modificar, actualizar o borrar los datos del usuario
    def modificar_datos(self):
        pass

        # Método para mostrar su historial de adopción si lo tiene, o simplemente mostrar todos los datos del usuario
    def historial(self):
        pass
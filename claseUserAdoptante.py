class User_Adoptante():

    def __init__(self, nombre, dni, email, preferencia):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencia = preferencia # {Raza, edad(cachorro/joven/adulto), tamaño}
        self.histo_adop = []
        
        # Método para registrar a un usuario
    def registrarse(self):
        return f"Usuario registrado: {self.nombre}\nDNI: {self.dni}\nEmail: {self.email}\nPreferencias: {self.preferencia}\nHistorial de adopción: {self.historial()}"
    
        # Método para modificar datos
    def modificar_datos(self, nuevo_nombre = None, nuevo_email = None, nueva_preferencia = None): #None para omitir si algún dato no se quiere modificar
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevo_email:
            self.email = nuevo_email
        if nueva_preferencia:    
            self.preferencia = nueva_preferencia


        return f"Datos modificados:\nNombre: {self.nombre}\nDNI: {self.dni}\nEmail: {self.email}\nPreferencias: {self.preferencia}"
        # Método para borrar los datos
    def borrar_datos(self):
        self.nombre = ""
        self.dni = ""
        self.email = ""
        self.preferencia = {}
        self.histo_adop = []

        
        return f"Los datos fueron borrados correctamente"
        

        # Método para mostrar su historial de adopción si lo tiene, o simplemente mostrar todos los datos del usuario
    def historial(self):
        if self.histo_adop == []:
            return "No hay adopciones realizadas"
        else:
            historial = ""
            for perro in self.histo_adop:
                historial += f"{perro.nombre} ID: {perro.id}\n"

            return f"Historial de adopciones: {historial} "
        
    def mostrar_user(self):
        print(f"Nombre: {self.nombre}\nDNI: {self.dni}\nEmail: {self.email}\nPreferencias: {self.preferencia}\nHistorial de adopción: {self.historial()}")



#nuevo_usuario = User_Adoptante("", "", "", "", "")
#nuevo_usuario.registro_user()

#nuevo_usuario = User_Adoptante("Carlos", "32564789", "c@gmail.com", {"Labrador", "grande", "cachorro"}, ["Plaga"])
#nuevo_usuario.modificar_datos()



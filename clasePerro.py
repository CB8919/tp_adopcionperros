class Perro(object):
    def __init__(self, id, nombre, raza, edad, tamano, peso, estado_salud, vacunado, estado, temperamento):
        self.id = int(id)
        self.nombre = nombre
        self.raza = raza
        self.edad = edad # cachorro, joven, adulto
        self.tamano = tamano  # Grande, mediano,pequeño
        self.peso = float(peso)
        self.estado_salud = estado_salud
        self.vacunado = vacunado # True o False
        self.estado = estado # Disponible, reservado, adoptado
        self.temperamento = temperamento
        

        # Método para cambiar el estado del perro a disponible, reservado o adoptado
    def cambiar_estado(self, nuevo_estado):
        #if nuevo_estado == "disponible" or nuevo_estado == "reservado" or nuevo_estado == "adoptado":
        if nuevo_estado in ["disponible", "reservado", "adoptado"]:
            self.estado = nuevo_estado
            return f"Nuevo estado: {self.estado}"
        else:
            return("Estado no valido")

        # Métedo para mostrar la info del perro
    def mostrar_info(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nRaza: {self.raza}\nEdad: {self.edad}\nTamaño: {self.tamano}\nPeso: {self.peso}kg\nEstado de saludo: {self.estado_salud}\nVacunado: {self.vacunado}\nEstado: {self.estado}\nTemperamento: {self.temperamento}"


perro = Perro(1, "Rex", "Pastor Alemán", "cachorro", "Grande", 30.5, "Bueno", True, "Disponible", "Amigable")


#print(perro.mostrar_info())
#perro.cambiar_estado("adoptado")
#print("\nInformación actualizada:")
#print(perro.mostrar_info())


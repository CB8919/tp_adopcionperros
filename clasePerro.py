class Perro():
    contador = 1 # Para aumentar el id del perro con cada perro nuevo que ingresa

    def __init__(self, nombre, raza, edad, tamano, peso, salud, vacunado, temperamento): #id_perro
        self.id = Perro.contador
        Perro.contador = Perro.contador + 1
        self.nombre = nombre
        self.raza = raza
        self.edad = edad # cachorro, joven, adulto
        self.tamano = tamano  # Grande, mediano,pequeño
        self.peso = float(peso)
        self.salud = salud
        self.vacunado = vacunado # True o False
        self.estado_de_adopcion = "disponible" # disponible, reservado, adoptado
        self.temperamento = temperamento
        

        # Método para cambiar el estado del perro a disponible, reservado o adoptado
    def cambiar_estado(self, nuevo_estado):
        #if nuevo_estado == "disponible" or nuevo_estado == "reservado" or nuevo_estado == "adoptado":
        if nuevo_estado in ["disponible", "reservado", "adoptado"]:
            self.estado_de_adopcion = nuevo_estado
            return f"Nuevo estado: {self.estado_de_adopcion}"
        else:
            return("Estado no valido")

        # Métedo para mostrar la info del perro
    def mostrar_info(self):
        return (f"ID: {self.id}\nNombre: {self.nombre}\nRaza: {self.raza}\nEdad: {self.edad}\nTamaño: {self.tamano}\nPeso: {self.peso}kg\nSalud: {self.salud}\nVacunado: {self.vacunado}\nEstado: {self.estado_de_adopcion}\nTemperamento: {self.temperamento}")








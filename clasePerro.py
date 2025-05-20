class Perro():
    id_contador = 1 # Para aumentar el id del perro con cada perro nuevo que ingresa

    def __init__(self, nombre, raza, edad, tamano, peso, salud, vacunado, temperamento): #id_perro
        self.id = Perro.id_contador
        Perro.id_contador = Perro.id_contador + 1
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


perro1 = Perro(nombre="Max", raza="Labrador", edad="adulto", tamano="grande", peso=30, salud="buena", vacunado=True, temperamento="calmado")
perro2 = Perro(nombre="Luna", raza="Beagle", edad="joven", tamano="mediano", peso=15, salud="excelente", vacunado=False, temperamento="activo")
perro3 = Perro(nombre="Coco", raza="Bulldog", edad="cachorro", tamano="pequeño", peso=8, salud="regular", vacunado=True, temperamento="tranquilo")
print(perro1.mostrar_info())
print(perro2.mostrar_info())
print(perro3.mostrar_info())




from clasePerro import Perro
from claseUserAdoptante import User_Adoptante

class Sistem_Adopcion():
    def __init__(self):
        self.list_usuario = []
        self.list_perro = []
        self.list_perro_adoptados = []

        # Método para agregar un nuevo perro a la lista de adopción
    def cargar_perro(self, perro):
        self.list_perro.append(perro)
        
        return self.list_perro
        
        # Método para eliminar un perro de la lista o ponerlo como adoptado
    def eliminar_perro(self, id_perro):
        for perro in self.list_perro:
            if perro.id == id_perro:
                self.list_perro.remove(perro)
                print(f"Se elimino el perro ID:{id_perro}")
                return True
            
        print(f"No se encontro ese ID: {id_perro}")
        return False 
        
        
        # Método para registrar un usuario en una base de datos
    def registrar_user(self, usuario):
        self.list_usuario.append(usuario)

        return self.list_usuario


        # Método para cambiar el estado de un perro a adoptado
    def confirmar_adop(self, id_perro):
        for perro in self.list_perro:
            if perro.id == id_perro:
                self.list_perro.remove(perro)
                perro.cambiar_estado("adoptado")
                self.list_perro_adoptados.append(perro)
                print(f"El perro ID: {id_perro} fue adoptado con exito.")
                return True
        print(f"No se encontro ese ID: {id_perro}")
        return False
                

        # Método para filtra preferncias del usuario a la hora de adoptar
    def preferencia_perro(self, opcion, valor):
        filtrado = []

        for perro in self.list_perro:
            if perro.estado_de_adopcion != "disponible":
                continue
            if opcion == "raza" and perro.raza == valor:
                filtrado.append(perro)
            elif opcion == "edad" and perro.edad == valor:
                filtrado.append(perro)
            elif opcion == "tamaño" and perro.tamano == valor:
                filtrado.append(perro)

        return filtrado
                
        # Método que retorna o muestra una lista de perros disponibles con sus estados
    def listado_perro(self):
        print("Listado de perros:\n")
        i = 1
        for perro in self.list_perro:
            i = i + 1
            print(f"{i}. ID: {perro.id}\nNombre: {perro.nombre}\nRaza: {perro.raza}\nEdad: {perro.edad}\nTamaño: {perro.tamano}\nPeso: {perro.peso}\nSalud: {perro.salud}\nVacunado: {perro.vacunado}\nEstado de adopción: {perro.estado_de_adopcion}\nTemperamento: {perro.temperamento}")    
        

        #disponible = []
        #for perro in self.list_perro:
        #    if perro.estado_de_adopcion == "disponible"
        #        disponible.append(perro)
        #return disponible  
    

#r = Sistem_Adopcion()
#nuevo_perro = r.cargar_perro()
#print(nuevo_perro.mostrar_info())



# Esto haría que sí se considere usado:
p = Perro("Luna", "Labrador", "joven", "mediano", 20, "saludable", True, "tranquila")

p1 = Perro("Firulais", "Labrador", "joven", "mediano", 20, "saludable", True, "tranquilo")

user1 = User_Adoptante("Carla", "12345678", "carla@gmail.com", {"raza": "Labrador"})

user1.histo_adop.append(p1)

user1.mostrar_user()

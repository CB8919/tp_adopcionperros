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
        if not self.list_perro:
            print("No hay perros registrados hasta el momento")
            return
        print("Listado de perros:\n")
        i = 1
        for perro in self.list_perro:
            print(f"{i}. ID: {perro.id}\nNombre: {perro.nombre}\nRaza: {perro.raza}\nEdad: {perro.edad}\nTamaño: {perro.tamano}\nPeso: {perro.peso}\nSalud: {perro.salud}\nVacunado: {perro.vacunado}\nEstado de adopción: {perro.estado_de_adopcion}\nTemperamento: {perro.temperamento}")
            i = i + 1    
        

        #disponible = []
        #for perro in self.list_perro:
        #    if perro.estado_de_adopcion == "disponible"
        #        disponible.append(perro)
        #return disponible  
    

#r = Sistem_Adopcion()
#nuevo_perro = r.cargar_perro()
#print(nuevo_perro.mostrar_info())


s = Sistem_Adopcion()
perro1 = Perro(nombre="Max", raza="Labrador", edad="adulto", tamano="grande", peso=30, salud="buena", vacunado=True, temperamento="calmado")
perro2 = Perro(nombre="Luna", raza="Beagle", edad="joven", tamano="mediano", peso=15, salud="excelente", vacunado=False, temperamento="activo")
perro3 = Perro(nombre="Coco", raza="Bulldog", edad="cachorro", tamano="pequeño", peso=8, salud="regular", vacunado=True, temperamento="tranquilo")

s.cargar_perro(perro1)
s.cargar_perro(perro2)
s.cargar_perro(perro3)
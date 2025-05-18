from clasePerro import Perro

class Sistem_Adopcion():
    def __init__(self):
        self.list_usuario = []
        self.list_perro = []
        

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
    def confirmar_adop(self):
        
        pass

        # Método para filtra preferncias del usuario a la hora de adoptar
    def preferencia_perro(self, opcion, valor):
        filtrado = []

        for perro in self.list_perro:
            if opcion == "raza" and perro.raza == valor:
                filtrado.append(perro)
            elif opcion == "edad" and perro.edad == valor:
                filtrado.append(perro)
            elif opcion == "tamaño" and perro.tamano == valor:
                filtrado.append(perro)

        return filtrado
                
        # Método que retorna o muestra una lista de perros disponibles con sus estados
    def listado_perro(self):
        disponible = []
        for perro in self.list_perro:
            if perro.estado_de_adopcion == "Disponible":
                disponible.append(perro)
        return disponible
            
    

#r = Sistem_Adopcion()
#nuevo_perro = r.cargar_perro()
#print(nuevo_perro.mostrar_info())




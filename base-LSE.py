# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada 
# ===========================================

# Clase Nodo
class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

#clase lista
class ListaSE:
    def __init__(self):
        self.cabeza = None
  
    def vacio(self):
        if self.cabeza is None:
            print("Está vacia")
        else:
            print("Lista no vacia")

    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    # contar el numero de elementos
    def contar(self):
        contador = 0
        actual = self.cabeza

        while actual:
            contador += 1
            actual = actual.siguiente

        return contador

    # buscar un elemento
    def buscar(self, data):
        actual = self.cabeza

        while actual:
            if actual.data == data:
                return True
            actual = actual.siguiente

        return False

    # eliminar el ultimo elemento
    def eliminarUltimo(self):

        if self.cabeza is None:
            return

        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        actual = self.cabeza

        while actual.siguiente.siguiente:
            actual = actual.siguiente
        actual.siguiente = None
	# eliminar el primer elemento   
    def eliminarPrimero(self):
        if self.cabeza is None:
            return
        self.cabeza = self.cabeza.siguiente

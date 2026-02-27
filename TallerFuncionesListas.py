# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada 
# ===========================================

class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None


class ListaSE:
    def __init__(self):
        self.cabeza = None
  
    # Verifica si la lista no contiene elementos
    def vacio(self):
        if self.cabeza is None:
            print("Está vacía")
        else:
            print("Lista no vacía")

    # Inserta un nuevo nodo al inicio de la lista
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    # Inserta un nuevo nodo al final de la lista
    def agregarFinal(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    # Inserta un nuevo valor después de la primera aparición de X
    def insertarDespues(self, x, data):
        actual = self.cabeza
        while actual:
            if actual.data == x:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return True
            actual = actual.siguiente
        return False

    # Inserta un nuevo valor antes de la primera aparición de X
    def insertarAntes(self, x, data):
        if self.cabeza is None:
            return False

        # Si X es la cabeza
        if self.cabeza.data == x:
            self.agregarInicio(data)
            return True

        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.data == x:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return True
            actual = actual.siguiente
        return False

    # Elimina el primer nodo de la lista
    def eliminarPrimero(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return
        self.cabeza = self.cabeza.siguiente

    # Elimina el último nodo de la lista
    def eliminarUltimo(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return

        # Si solo hay un nodo
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        actual = self.cabeza
        while actual.siguiente.siguiente:
            actual = actual.siguiente
        actual.siguiente = None

    # Busca un elemento por su valor (retorna Verdadero o Falso)
    def buscar(self, x):
        actual = self.cabeza
        while actual:
            if actual.data == x:
                return True
            actual = actual.siguiente
        return False

    # Cuenta cuántos elementos tiene la lista
    def contar(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    # Muestra los elementos de la lista
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.data, end=" -> ")
            actual = actual.siguiente
        print("None")
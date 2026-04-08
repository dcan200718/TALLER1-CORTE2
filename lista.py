class lista:
    def __init__(self):
        self.head = None

    def insertarCabeza(self, data):
        nuevoNodo = nuevoNodo(data)
        nuevoNodo.next = self.head
        self.head = nuevoNodo

    def insertarFinal(self, data):
        nuevoNodo = nuevoNodo(data)

        if self.head is None:
            self.head = nuevoNodo
            return

        actual = self.head
        while actual.next is not None:
            actual = actual.next

        actual.next = nuevoNodo

        def display(self):
          actual = self.head
        while actual is not None:
            print(actual.data, end=" -> ")
            actual = actual.next
        print("None")

        def buscarNodo(self,objetivo):
         actual = self.head

        while actual is not None:
         if actual.data == int(objetivo):
            return True
        actual = actual.next

        return False
    
    def borrarPrimerNodo(self):
           if self.head is not None:
              self.head = self.head.next  

    def eliminar_primero(self):
        if self.cabeza is None:
            print("La lista está vacía. No hay nodo que eliminar.")
            return
        eliminado = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        print(f"Nodo con valor '{eliminado}' eliminado del inicio.")

    def eliminar_por_valor(self, dato):
        
        if self.cabeza is None:
            print("La lista está vacía. No hay nodo que eliminar.")
            return
 
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            print(f"Nodo con valor '{dato}' eliminado.")
            return
 
        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual is not None:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente
                print(f"Nodo con valor '{dato}' eliminado.")
                return
            anterior = actual
            actual = actual.siguiente
 
        print(f"El valor '{dato}' no fue encontrado en la lista.")

    def tamano(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def invertir(self):
        anterior = None
        actual = self.head

        while actual is not None:
            siguiente = actual.next
            actual.next = anterior
            anterior = actual
            actual = siguiente

        self.head = anterior

    def ordenar(self):
        if self.head is None:
            return

        cambiado = True

        while cambiado:
            cambiado = False
            actual = self.head

            while actual.next is not None:
                if actual.data > actual.next.data:
                    temp = actual.data
                    actual.data = actual.next.data
                    actual.next.data = temp
                    cambiado = True
                actual = actual.next
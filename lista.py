class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Lista:
    def __init__(self):
        self.head = None

    def insertarCabeza(self, data):
        nuevoNodo = Node(data)
        nuevoNodo.next = self.head
        self.head = nuevoNodo

    def insertarFinal(self, data):
        nuevoNodo = Node(data)

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

    def buscarNodo(self, objetivo):
        actual = self.head
        while actual is not None:
            if actual.data == objetivo:
                return True
            actual = actual.next
        return False

    def borrarPrimerNodo(self):
        if self.head is not None:
            self.head = self.head.next

    def eliminar_por_valor(self, dato):
        if self.head is None:
            return

        if self.head.data == dato:
            self.head = self.head.next
            return

        anterior = self.head
        actual = self.head.next

        while actual is not None:
            if actual.data == dato:
                anterior.next = actual.next
                return
            anterior = actual
            actual = actual.next

    def tamano(self):
        contador = 0
        actual = self.head
        while actual is not None:
            contador += 1
            actual = actual.next
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
                    actual.data, actual.next.data = actual.next.data, actual.data
                    cambiado = True
                actual = actual.next
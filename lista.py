class lista:
    def __init__(self):
        self.head = None





















































































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
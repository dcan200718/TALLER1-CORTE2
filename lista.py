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
         if actual.data == objetivo:
            return True
        actual = actual.next

        return False
    
    def borrarPrimerNodo(self):
           if self.head is not None:
              self.head = self.head.next    
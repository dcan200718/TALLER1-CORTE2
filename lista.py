class lista:
    def __init__(self):
        self.head = None

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
 
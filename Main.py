
from lista import lista

def menu():
    print("\n--- MENÚ LISTA ENLAZADA ---")
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Mostrar lista")
    print("4. Buscar elemento")
    print("5. Eliminar primer elemento")
    print("6. Eliminar por valor")
    print("7. Tamaño de la lista")
    print("8. Invertir lista")
    print("9. Ordenar lista")
    print("0. Salir")
    return input("Seleccione una opción: ")

def main():
    mi_lista = lista()
    
    while True:
        opcion = menu()
        
        if opcion == "1":
            dato = input("Ingrese el valor a insertar al inicio: ")
            mi_lista.insertarCabeza(dato)
        
        elif opcion == "2":
            dato = input("Ingrese el valor a insertar al final: ")
            mi_lista.insertarFinal(dato)
            
        elif opcion == "3":
            print("Contenido de la lista:")
            mi_lista.display()
            
        elif opcion == "4":
            objetivo = input("Ingrese el valor a buscar: ")
            # Tu método buscarNodo retorna True o False
            encontrado = mi_lista.buscarNodo(objetivo)
            if encontrado:
                print(f"El elemento {objetivo} existe en la lista.")
            else:
                print("Elemento no encontrado.")
                
        elif opcion == "5":
            mi_lista.borrarPrimerNodo()
            print("Primer nodo eliminado.")
            
        elif opcion == "6":
            valor = input("Ingrese el valor a eliminar: ")
            # Nota: Asegúrate de implementar eliminarPorValor en lista.py
            print("Función en desarrollo...") 
            
        elif opcion == "7":
            # Nota: Necesitas implementar el método de tamaño
            print("Calculando tamaño...")
            
        elif opcion == "8":
            # Nota: Necesitas implementar el método de inversión
            print("Invirtiendo lista...")
            
        elif opcion == "9":
            # Nota: Aquí iría tu Bubble Sort de enlaces
            print("Ordenando lista...")
            
        elif opcion == "0":
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
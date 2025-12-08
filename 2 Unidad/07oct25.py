from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()
        else:
            return None
    
    def frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            return None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamaño(self):
        return len(self.items)
    
    def mostrar(self):
        print("La cola es:", list(self.items))
    
    @staticmethod
    def menu():
        cola = Cola()  # Crear instancia de la cola
        
        while True:
            print("\n" + "="*30)
            print("MENÚ DE LA COLA")
            print("="*30)
            print("1. Encolar")
            print("2. Desencolar")
            print("3. Ver frente")
            print("4. ¿Está vacía?")
            print("5. Tamaño de la cola")
            print("6. Mostrar cola")
            print("7. Salir")
            
            opcion = input("\nSelecciona una opción (1-7): ")
            
            if opcion == "1":
                elemento = input("Ingresa el elemento a agregar: ")
                cola.encolar(elemento)
                print(f"Elemento '{elemento}' agregado a la cola")
            
            elif opcion == "2":
                elemento = cola.desencolar()
                if elemento is not None:
                    print(f"Elemento eliminado: '{elemento}'")
                else:
                    print("La cola está vacía, no hay elementos para eliminar")
            
            elif opcion == "3":
                frente = cola.frente()
                if frente is not None:
                    print(f"El frente de la cola es: '{frente}'")
                else:
                    print("La cola está vacía")
            
            elif opcion == "4":
                if cola.esta_vacia():
                    print("La cola SÍ está vacía")
                else:
                    print("La cola NO está vacía")
            
            elif opcion == "5":
                print(f"El tamaño de la cola es: {cola.tamaño()}")
            
            elif opcion == "6":
                cola.mostrar()
            
            elif opcion == "7":
                print("Saliendo del programa...")
                break
            
            else:
                print("Opción inválida. Por favor, selecciona una opción del 1 al 7")

# Bloque principal para probar la clase
if __name__ == "__main__":
    Cola.menu()
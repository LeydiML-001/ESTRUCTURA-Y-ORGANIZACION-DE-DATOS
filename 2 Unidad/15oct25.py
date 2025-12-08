from collections import deque

class Cola:
    def __init__(self):
        self.items = deque() 

    def encolar(self, item): 
        self.items.append(item)  # Corregido: "intems" -> "items", "intems" -> "item"

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()  # Corregido: "intems" -> "items"
        else:
            return None

    def frente(self):
        if not self.esta_vacia():
            return self.items[0]  # Corregido: "intems" -> "items"
        else:
            return None

    def esta_vacia(self):
        return len(self.items) == 0  # Corregido: "intems" -> "items"

    def tamaño(self):
        return len(self.items)  # Corregido: "intems" -> "items"

    def mostrar(self):
        print("Cola:", list(self.items))  # Corregido: "intems" -> "items"


def menu():
    cola = Cola()
    
    while True:
        print("--- MENÚ ---")
        print("1. Encolar")
        print("2. Desencolar")
        print("3. Ver frente")
        print("4. Mostrar cola")
        print("5. Verificar si está vacía")
        print("6. Tamaño de la cola")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            elemento = input("Ingresa el elemento a encolar: ")
            cola.encolar(elemento)
            print(f"Elemento '{elemento}' encolado.")

        elif opcion == "2":
            elemento = cola.desencolar()
            if elemento is not None:
                print("Elemento desencolado:", elemento)
            else:
                print("La cola está vacía.")

        elif opcion == "3":
            frente = cola.frente()
            if frente is not None:
                print(f"Frente de la cola: {frente}")
            else:
                print("La cola está vacía.")

        elif opcion == "4":
            cola.mostrar()

        elif opcion == "5":
            print("¿Cola vacía?", "Sí" if cola.esta_vacia() else "No")

        elif opcion == "6":
            print("Tamaño de la cola:", cola.tamaño())

        elif opcion == "7":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()

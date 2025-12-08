from collections import deque

class Cola:
    def __init__(self):  #se agrega otro gion bajo al def __init__(self):  
        self.items = deque()   #se agrega .itemsal self por que no esta definido

    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
           return self.items.popleft() # se elimina print (self.items.popleft()) y se agrega return self.items.popleft()
        else:
            return None
  
    def frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            return None
        
    def esta_vacia(self):
        return len(self.items) ==0
    
    def tamaño(self):
        return len(self.items)
    
    def mostrar (self):
        print ("La cola es: ",list(self.items))

def menu():
    cola = Cola()

    while True:
        print("Menu de mi cola")
        print("1. Encolar")
        print("2. Desencolar")
        print("3. Ver frente")
        print("4. ¿Esta vacio?")
        print("5. Tamaño de la cola")
        print("6. Mostrar")
        print("7. Salir")

        opcion = input ("Selecciona lo que quieras hacer:")
        if opcion=="1":
            elemento=input("Agrega nuevo elemento numerico")#se elimina int y el parentesis
            cola.encolar(elemento) #se agrega .encolar de cola.encolar
            print(f"Elemento '{elemento}' encolado.") #se cambia el dato ("Elemento agregado", elemento) por el dato (f"Elemento '{elemento}' encolado.") para visualizar datos

        elif opcion=="2":
            elemento=cola.desencolar()
            if elemento is not None:
                print ("Elemento eliminado es:", elemento)
            else:
                print ("La cola esta vacia")
            
        elif opcion=="3":
            frente=cola.frente()
            if frente is  None:  
                print(f"Frente de la cola: {frente}") #se cambia el dato ("La frente de la cola es", frente) por(f"Frente de la cola: {frente}")
            else:
                print("La cola esta vacia")
        
        elif opcion=="4":
            print ("La cola esta vacia?:","Si" if cola.esta_vacia() else "No")

        elif opcion=="5":
            print ("El tamaño de la cola es:",cola.tamaño())

        elif opcion=="6":
            cola.mostrar()

        elif opcion=="7":
            print ("Saliste del programa")
            break # se agrega break debajo del print
        else:
            print ("Dato invalido")

if __name__ == "__main__":  # se Corrige el _main_ por el __main__
    menu()
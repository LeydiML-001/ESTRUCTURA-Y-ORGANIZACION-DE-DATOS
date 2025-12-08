class ColaEstatica:
    def __init__(self,tamaño_maximo):
        self.tamaño_maximo=tamaño_maximo
        self.cola=[]

    def esta_vacia(self):
        return len(self.cola)==0

    def esta_lleno(self):
        return len(self.cola)==self.tamaño_maximo

    def enqueue(self,elemento):
        if self.esta_lleno():
         print("Error: la cola esta llena")
        else:
            self.cola.append(elemento)

    def dequeue(self):
        if self.esta_vacia():
         print("Cola vacia,no se puede eliminar")
        else:
          return self.cola.pop(0)
 
    def peek(self):
        if self.esta_vacia():
          return None
        return self.cola[0]

    def size(self):
       return len(self.cola)

    def clear(self):
       self.cola.clear()

    def ver_informacion(self):
      return self.cola




cola= ColaEstatica(4)
cola.enqueue("A")
cola.enqueue("B")
cola.enqueue("C")
cola.enqueue("D")

def menu_ColaEstatica(input):

 while True:
          try:
              tamaño=int(input("ingresa el tamaño maximo de la cola:"))
              if tamaño <=0:
                  print("el tamaño debe ser mayor a cero")
                  continue
              break
          except ValueError:
              print("por favor ingresa un numero valido")
              
          print("menu")  
          print("1. encolar")
          print("2. desencolar")
          print("3. ver frente")
          print("4. esta vacio?:")
          print("5. esta lleno?:")
          print("6. tamaño de la cola")
          print("7. mostrar")
          print("8. salir")

          opcion=input("selecciona lo que quieras hacer:")
          if opcion=="1":
            elemento=input("agrega un nuevo elemento")
            if cola.encolar(elemento):
             print("elemento agregado",elemento)
          
          elif opcion =="2":
            elemento=cola.desencolar()
            if elemento is not None:
                print("el elemento eliminado es:",elemento)
            else:
                print("la cola esta vacia:")
          
          elif opcion =="3":
             frente=cola.frente()
             if frente is not None:
                 print("el frente de la cola es:",elemento)
             else:
                 print("la cola esta vacia:",elemento)
          
          elif opcion=="4":
             if cola.vacia(): 
                 print("la cola esta vacia?:",elemento)     
         
          elif opcion=="5":
             if cola.esta_lleno(): 
              print("la cola esta llena?:")
          
          elif opcion=="6":
                 print("el tamaño es:",cola.tamaño())
         
          elif opcion=="7":
                 cola.mostrar()
         
          elif opcion=="7":
                 print("saliste del programa")
                 break
          else:
              print("dato invalido")
          if __name__ == "__main__":
              menu_ColaEstatica


print("menu")
print("La cola despues de agregar las 3 letras es:",cola.ver_informacion())
print("La letra en la cima de la cola es:",cola.peek())
print("Su capacidad de elementos en la cola es:",cola.size())

#cola dinamica
from collections import deque

class Cola:
    def __init__(self):
        self.items=deque()

    def encolar(self,item):
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
        return len (self.items)==0
    
    def tamaño(self):
        return len(self.items)

    def mostrar(self):
        print("la cola es:",list(self.items))     

    def menu():
     cola = Cola
while True:
          print("menu de la cola")  
          print("1. encolar")
          print("2. desencolar")
          print("3. ver frente")
          print("4. esta vacio?:")
          print("5. tamaño de la cola")
          print("6. mostrar")
          print("7. salir")

          opcion=input("selecciona lo que quieras hacer:")
          if opcion=="1":
            elementos=input("agrega un nuevo elemento")
            Cola.encolar(elementos)
            print("elemento agregado",elementos)
          elif opcion =="2":
            elementos=Cola.desencolar()
            if elementos is not None:
                print("el elemento eliminado es:",elementos)
            else:
                print("la cola esta vacia:")
          elif opcion =="3":
             frente=Cola.frente()
             if frente is not None:
                 print("el frente de la cola es:")
             else:
                 print("la cola esta vacia:")
          elif opcion=="4":
                 print("la cola esta vacia?:")
          elif opcion=="5":
                 print("el tamaño es:",Cola.tamaño(int))
          elif opcion=="6":
                 Cola.mostrar()
          elif opcion=="7":
                 print("saliste del programa")
                 break
          else:
              print("dato invalido")
          if __name__ == "__main__":

           cola=Cola()
cola.encolar("A")
cola.encolar("B")
cola.encolar("C")
cola.encolar("D")
cola.encolar("E")
Cola.mostrar()
print("el frente es:",cola.frente())
print("el dato eliminado es:",cola.desencolar())
Cola.mostrar()
print("la cola esta vacia?:",cola.esta_vacia())
print("el tamaño es:",cola.tamaño())
Cola.mostrar()
print("la cola se muestra:",cola.mostrar())
print("el dato agregado es:",cola.encolar())

#cola estatico
class ColaEstatica:
    def __init__(self,tamaño_maximo):
        self.tamaño_maximo=tamaño_maximo
        self.cola=[]

#identifica si no esta vacia
    def esta_vacia(self):
        return len(self.cola)==0

    def esta_lleno(self):
        return len(self.cola)==self.tamaño_maximo

#agregar datos
    def enqueue(self,elemento):
        if self.esta_lleno():
         print("Error: la cola esta llena")
        else:
            self.cola.append(elemento)
#eliminar datos
    def dequeue(self):
        if self.esta_vacia():
         print("La cola esta vacia, no puedes eliminar")
        else:
          return self.cola.pop(0)
#saber cual es el dato esta en la cima
    def peek(self):
        if self.esta_vacia():
          return None
        return self.cola[0]
#devolver datos de manera ordenada
    def size(self):
       return len(self.cola)
#borrar todo
    def clear(self):
       self.cola.clear()

    def ver_todos(self):
      return self.cola
#provar datos de forma sencilla
cola= ColaEstatica(3)
#agregar elemntos
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)
print("la cola despues de agregar 3 elementos es:",cola.ver_todos())
#dato en la cima
print("el dato en la cima de la cola es:",cola.peek())

#tamaño
print("el tamaño de la cola es:",cola.size())

#eliminar todo
cola.clear()
print("la cola despues de eliminar es:",cola.ver_todos())







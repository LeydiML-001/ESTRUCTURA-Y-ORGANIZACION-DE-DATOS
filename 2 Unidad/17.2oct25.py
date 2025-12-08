#definimos clase pila y definimos variables
class Pila:
    def __init__(self, capacidad=5):
        self.capacidad = capacidad
        self.elementos = []
    
    def push(self, elemento):# agregamos sel.elementos a elementos
        if len(self.elementos) < self.capacidad:
            self.elementos.append(elemento)
            print(f"Elemento agregado: {elemento}")
        else:
            print("La pila está llena")
    
    def pop(self):
        if not self.esta_vacia():
            elemento = self.elementos.pop()
            print(f"Elemento eliminado: {elemento}")
            return elemento
        else:
            print("La pila está vacía")
            return None
    
    def peek(self):
        if not self.esta_vacia():
            print(f"Elemento en la cima: {self.elementos[-1]}")
            return self.elementos[-1]
        else:
            print("La pila está vacía")
            return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def mostrar(self):
        if self.elementos:
            print("Pila (cima - base):", list(reversed(self.elementos)))
        else:
            print("Pila vacía")

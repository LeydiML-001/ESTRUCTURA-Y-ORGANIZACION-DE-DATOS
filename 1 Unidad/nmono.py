# definimos clase y definicion funcion
class Nodo:
 def __init__(self,valor):
     self.valor=valor
     self.izquierda=None
     self.derecha=None
     
 #creamos nodos
raiz=Nodo ("A")
raiz.izquierda=Nodo("B")
raiz.derecha=Nodo("C")

#Mostramos valore
print("Raiz de inicio",raiz.valor)
print("Hijo izquierda",raiz.izquierda.valor)
print("Hijo derecho", raiz.derecha.valor)

# definimos clase y definicion funcion
class Nodo:
 def __init__(self,valor):
     self.valor=valor
     self.izquierda=None
     self.derecha=None
     
 #creamos nodos
raiz=Nodo ("A")
raiz.izquierda=Nodo("Café")
raiz.derecha=Nodo("Pan")

#Mostramos valore
print("Raiz de inicio",raiz.valor)
print("Hijo izquierda",raiz.izquierda.valor)
print("Hijo derecho", raiz.derecha.valor)
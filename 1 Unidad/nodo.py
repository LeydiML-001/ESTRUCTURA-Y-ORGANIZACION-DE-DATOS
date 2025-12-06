#Definimos clase y definimos valor
class nodo:
 def _init_(self,valor):
     self.valor = valor
     self.izquierda=None
     self.derecha=None
#Creamos nodos
     raiz= Nodo("A")
     raiz.izquierda= Nodo("B")
     raiz.derecha= Nodo("c")
     # Mostramos valores
     print("raiz de inicio",raiz.valor)
     print("hijo izquierdo",raiz.izquierdo.valor)
     print("hijo derecho",raiz.derecho.valor)




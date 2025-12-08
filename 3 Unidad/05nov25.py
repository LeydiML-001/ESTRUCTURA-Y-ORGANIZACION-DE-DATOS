#arbol binario de busqueda
class Nodo:
    def __init__(self,valor):
        self.valor=valor
        self.izquierda=None
        self.derecha=None

def insertar (nodo,valor):
    if nodo is None:
        return Nodo (valor)
    if valor<nodo.valor:
        nodo.izquierda=insertar(nodo.izquierda,valor)
    else:
        nodo.derecha=insertar(nodo.derecha,valor)
    return nodo    
#busqueda
def buscar (nodo, valor):
    if nodo is None:
        return False
    if nodo.valor== valor:
        return True
    elif valor< nodo.valor:
        return buscar(nodo.izquierda,valor)
    else:
        return buscar(nodo.derecha,valor)
#inorden
def inorden(nodo):
    if nodo:
        inorden(nodo.izquierda)
        print(nodo.valor,end="")
        inorden(nodo.derecha)
#pruebas
#raiz=None
#valores=[1,3,4,1,5,7,9,11,14,10]   
#for v in valores:
 #   raiz=insertar(raiz,v)
#print("arbol en orden")
#inorden(raiz)

#print("buscar",buscar(raiz,11))
#print("buscar",buscar(raiz,20))


raiz=None
print("arbol de busqueda")
valores=input("ingresa los valores separados por espacios")
valores=[int(v) for v in valores.split()]

for v in valores:
    raiz=insertar(raiz,v)

    print("el orden de mi arbol es:")
    inorden(raiz)
#busqueda
while True:
    opcion=input("¿desea buscar algun otro valor?(s/n)").lower()
    if opcion !="s":
        break
    valor_buscar=int(input("ingresa el valor a buscar que sea un numero"))
    encontrar=buscar(raiz,valor_buscar)
    if encontrar:
        print("el valor si esta en el arbol")
    else:
        print("el valor no esta en el arbol")    



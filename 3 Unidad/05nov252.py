class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Funciones de recorrido
def inorden(nodo):
    if nodo:
        inorden(nodo.izquierda)
        print(nodo.valor, end=" ")
        inorden(nodo.derecha)

def preorden(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        preorden(nodo.izquierda)
        preorden(nodo.derecha)

def posorden(nodo):
    if nodo:
        posorden(nodo.izquierda)
        posorden(nodo.derecha)
        print(nodo.valor, end=" ")

# Función para calcular altura
def altura(nodo):
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.izquierda), altura(nodo.derecha))

# Funciones para árbol binario de búsqueda (ABB)
def insertar_abb(nodo, valor):
    """Inserta un valor en un árbol binario de búsqueda"""
    if nodo is None:
        return Nodo(valor)
    if valor < nodo.valor:
        nodo.izquierda = insertar_abb(nodo.izquierda, valor)
    else:
        nodo.derecha = insertar_abb(nodo.derecha, valor)
    return nodo

def buscar_abb(nodo, valor):
    """Busca un valor en un árbol binario de búsqueda"""
    if nodo is None:
        return False
    if nodo.valor == valor:
        return True
    elif valor < nodo.valor:
        return buscar_abb(nodo.izquierda, valor)
    else:
        return buscar_abb(nodo.derecha, valor)

# Función para mostrar árbol predefinido
def mostrar_arbol_predefinido():
    raiz = Nodo(1)
    raiz.izquierda = Nodo(2)
    raiz.derecha = Nodo(3)
    raiz.izquierda.izquierda = Nodo(4)
    raiz.izquierda.derecha = Nodo(5)
    raiz.izquierda.izquierda.izquierda = Nodo(6)
    raiz.izquierda.izquierda.derecha = Nodo(7)
    raiz.izquierda.derecha.izquierda = Nodo(8)
    raiz.izquierda.derecha.derecha = Nodo(9)
    raiz.derecha.izquierda = Nodo(10)
    raiz.derecha.derecha = Nodo(11)
    raiz.derecha.izquierda.izquierda = Nodo(12)
    raiz.derecha.izquierda.derecha = Nodo(13)
    raiz.derecha.derecha.izquierda = Nodo(14)
    raiz.derecha.derecha.derecha = Nodo(15)
    
    return raiz

# Menú principal CORREGIDO
def menu():
    arbol_predefinido = None
    arbol_busqueda = None
    while True:
        print("\n" + "="*50)
        print("MENÚ ÁRBOLES BINARIOS")
        print("1. Mostrar árbol predefinido y sus recorridos")
        print("2. Calcular altura del árbol predefinido")
        print("3. Crear árbol binario de BÚSQUEDA (ABB)")
        print("4. Buscar valor en árbol binario de búsqueda (ABB)")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción (1-5): ")
        
        if opcion == "1":
            print("-- ÁRBOL PREDEFINIDO ---")
            arbol_predefinido = mostrar_arbol_predefinido()
            
            print("Recorrido Inorden:")
            inorden(arbol_predefinido)
            print()
            
            print("Recorrido Preorden:")
            preorden(arbol_predefinido)
            print()
            
            print("Recorrido Posorden:")
            posorden(arbol_predefinido)
            print()
            
        elif opcion == "2":
            if arbol_predefinido is None:
                arbol_predefinido = mostrar_arbol_predefinido()
            alt = altura(arbol_predefinido)
            print(f"La altura del árbol predefinido es: {alt}")
            
        elif opcion == "3":

            arbol_busqueda = None
            valores = []
            
            print("Ingresa números para construir el árbol de búsqueda.")
            print("Escribe 'fin' para terminar de agregar números.")
            
            if valores:  
                print("Recorrido Inorden (valores ordenados):")
                inorden(arbol_busqueda)
                print()
                
                print("Recorrido Preorden:")
                preorden(arbol_busqueda)
                print()
                
                print("Recorrido Posorden:")
                posorden(arbol_busqueda)
                print()
                
                alt = altura(arbol_busqueda)
                print(f"Altura del árbol de búsqueda: {alt}")
                
                # Mostrar estructura básica del árbol
                print("Estructura básica del árbol:")
                if arbol_busqueda:
                    print(f"Raíz: {arbol_busqueda.valor}")
                    if arbol_busqueda.izquierda:
                        print(f"Subárbol izquierdo de {arbol_busqueda.valor}: ", end="")
                        inorden(arbol_busqueda.izquierda)
                        print()
                    if arbol_busqueda.derecha:
                        print(f"Subárbol derecho de {arbol_busqueda.valor}: ", end="")
                        inorden(arbol_busqueda.derecha)
                        print()
                    else:
                        print("No se ingresaron valores. El árbol de búsqueda está vacío.")
                
        elif opcion == "4":
            if arbol_busqueda is None:
                print("Primero debes crear un árbol binario de búsqueda (opción 3)")
                continue
                
            print("--- BUSCAR EN ÁRBOL BINARIO DE BÚSQUEDA ---")
            print("Árbol actual en orden (inorden): ", end="")
            inorden(arbol_busqueda)
            print()
            
            valor_buscar = int(input("\nIngresa el valor a buscar: "))
            encontrado = buscar_abb(arbol_busqueda, valor_buscar)
                
            if encontrado:
                    print(f"El valor {valor_buscar} SÍ está en el árbol.")
            else:
                    print(f"El valor {valor_buscar} NO está en el árbol.")
                
        elif opcion == "5":
            print("Hasta luego!")
            break
            
        else:
            print("Opción inválida. Por favor selecciona una opción del 1 al 5.")
        
if __name__ == "__main__":
    menu()
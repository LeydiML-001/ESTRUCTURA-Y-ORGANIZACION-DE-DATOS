class Grafo:#nodos y grafos
    def __init__(self):
        self.grafo =  {}#las llaves son para crear un diccionario soin generar ninguna con3exion

    def agregar_vertice(self,vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = [] 
        else:
            print("el grafo ya existe.")

    def agregar_aristas(self,v1,v2):
        if v1 in self.grafo and v2 in self.grafo:
            self.grafo[v1].append(v2)
            self.grafo[v2].append(v1)
        else:
            print("el vertice no existe, o no hay")  

    def mostrar(self):
        for vertice in self.grafo:
            print(vertice,"->",self.grafo[vertice])    

if __name__ == "__main__":
    g=Grafo()

#crear menu este input a todo el programa de menu en la parte de anchura y profundidad 
    def bfs(self, inicio):
        visitados = set() 
        cola = [inicio]
        visitados.add(inicio)

        while cola:
            vertice = cola.pop(0)
            print(vertice, end=" ")
        
            for vecino in self.grafo[vertice]:
                if vecino not in visitados:
                    visitados.add(vecino) 
                    cola.append(vecino)

    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        
        visitados.add(inicio)
        print(inicio, end=" ")
        
        for vecino in self.grafo[inicio]:
            if vecino not in visitados:
                self.dfs(vecino, visitados)

    def menu():
        while True:
            print("--- MENÚ ---")
            print("1. Agrega aristas")
            print("2. Agrega vertices")
            print("3. Anchura")
            print("5. Profundidad")
            print("6. Mostrar grafo")
            print("7. salir")
        
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
             m=int(input("agrega el numero de aristas"))
            for i in range(m):
                print("aristas,#{i+1}:")
                v1=input("agrega la primera arista")
                v2=input("agrega la segunda arista")
                g.agregar_aristas(v1,v2)
           
            if opcion == "2":
             n=int(input("agrega el numero de vertices"))
            for i in range(n):
                vertice=int(input("ingresa el numero de vertices,#{i+1}:"))
                g.agregar_vertice(vertice)

            if opcion == "3":
             print("la anchura es")
             g.bfs()
                
            if opcion == "4":
             print("la profundidad es")
             g.dfs()

            if opcion == "5":
             print("mostrar grafo:")
             g.mostrar()
       
            if opcion == "7":
              print("Saliendo del programa.")
            break

if __name__ == "__main__":
    menu()
class Grafo:
    def __init__(self):
        self.grafo = {}  # diccionario para almacenar el grafo

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = [] 
        else:
            print("El vértice ya existe.")

    def agregar_arista(self, v1, v2):
        if v1 in self.grafo and v2 in self.grafo:
            self.grafo[v1].append(v2)
            self.grafo[v2].append(v1)
        else:
            print("Alguno de los vértices no existe.")

    def mostrar(self):
        for vertice in self.grafo:
            print(vertice, "->", self.grafo[vertice])

    def bfs(self, inicio):
        if inicio not in self.grafo:
            print("El vértice inicial no existe.")
            return
            
        visitados = set() 
        cola = [inicio]
        visitados.add(inicio)

        print("Recorrido BFS:", end=" ")
        while cola:
            vertice = cola.pop(0)
            print(vertice, end=" ")
        
            for vecino in self.grafo[vertice]:
                if vecino not in visitados:
                    visitados.add(vecino) 
                    cola.append(vecino)
        print()

    def dfs(self, inicio, visitados=None):
        if inicio not in self.grafo:
            print("El vértice inicial no existe.")
            return
            
        if visitados is None:
            visitados = set()
        
        visitados.add(inicio)
        print(inicio, end=" ")
        
        for vecino in self.grafo[inicio]:
            if vecino not in visitados:
                self.dfs(vecino, visitados)


def menu():
    g = Grafo()
    
    while True:
        print("\n--- MENÚ DEL GRAFO ---")
        print("1. Agregar vértices")
        print("2. Agregar aristas")
        print("3. Recorrido en Anchura (BFS)")
        print("4. Recorrido en Profundidad (DFS)")
        print("5. Mostrar grafo")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                n = int(input("¿Cuántos vértices quieres agregar? "))
                for i in range(n):
                    vertice = input(f"Ingresa el vértice #{i+1}: ")
                    g.agregar_vertice(vertice)
            except ValueError:
                print("Por favor ingresa un número válido.")
           
        elif opcion == "2":
            try:
                m = int(input("¿Cuántas aristas quieres agregar? "))
                for i in range(m):
                    print(f"Arista #{i+1}:")
                    v1 = input("Ingresa el primer vértice: ")
                    v2 = input("Ingresa el segundo vértice: ")
                    g.agregar_arista(v1, v2)
            except ValueError:
                print("Por favor ingresa un número válido.")

        elif opcion == "3":
            inicio = input("Ingresa el vértice inicial para BFS: ")
            g.bfs(inicio)
                
        elif opcion == "4":
            inicio = input("Ingresa el vértice inicial para DFS: ")
            print("Recorrido DFS:", end=" ")
            g.dfs(inicio)
            print()

        elif opcion == "5":
            print("Grafo completo:")
            g.mostrar()
       
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
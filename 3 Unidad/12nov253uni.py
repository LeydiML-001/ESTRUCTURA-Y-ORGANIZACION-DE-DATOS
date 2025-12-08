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

#recorridos por anchura y por profundidad

    def bfs(self,inicio): #bfs sirve para anchura
        visitados=set()
        cola=[inicio]
        visitados.add(inicio)

        while cola:#utilizamos pop para nomduplicar los datos de anchura
            vertice=cola.pop(0)# if vertice not in visitados:
            print(vertice,end=" ")
            for vec in self.grafo[vertice]:
                    if vertice not in visitados:
                        visitados.add(vec)
                    cola.append(vec)

    def dfs(self,inicio,visitados=None):
        if visitados is None:
            visitados=set()
            print(inicio, end=" ")
            visitados.append(inicio)
            for vec in self.grafo[inicio]:
                if vec not in visitados:
                    self.dfs(vec,visitados)                


#pruebas Y crear grafo
g=Grafo()

#agregar vertices
g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")


#agregar aristas
g.agregar_aristas("A","B")
g.agregar_aristas("A","C")
g.agregar_aristas("A","D")


#mandar a traer la funcion mostrar para imprimir
print("el grafo es:")
g.mostrar()

#anchura
print("recorrido anchura bfs desde el A")
g.bfs("A")

#OPORTUNIDAD
print("recorrido dfs profundidad desde A")
g.dfs("A")




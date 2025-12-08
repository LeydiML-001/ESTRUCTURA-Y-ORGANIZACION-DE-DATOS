class Grafo:  # nodos y grafos
    def __init__(self):
        self.grafo = {}  # las llaves son para crear un diccionario sin generar ninguna conexión

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
        else:
            print("el vertice ya existe.")

    def agregar_aristas(self, v1, v2):
        if v1 in self.grafo and v2 in self.grafo:
            self.grafo[v1].append(v2)
            self.grafo[v2].append(v1)
        else:
            print("el vertice no existe")

    def mostrar(self):
        for vertice in self.grafo:
            print(vertice, "->", self.grafo[vertice])


if __name__ == "__main__":
    g = Grafo()

    n = int(input("agrega el numero de vertices: "))
    for i in range(n):
        vertice = input("ingresa el vertice #{}: ".format(i+1))
        g.agregar_vertice(vertice)

    m = int(input("agrega el numero de aristas: "))
    for i in range(m):
        print("arista #{}:".format(i+1))
        v1 = input("agrega el primer vertice: ")
        v2 = input("agrega el segundo vertice: ")
        g.agregar_aristas(v1, v2)

    print("\nGrafo resultante:")
    g.mostrar()
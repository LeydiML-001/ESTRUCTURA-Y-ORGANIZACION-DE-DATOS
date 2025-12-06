grafo={
"A":["B","C"],
"B":["A","C"],
"C":["A"],
"D":["B"]
}
for nodo in grafo:
    print(f"{nodo}el nodo establecido es: {grafo[nodo]}")

grafo={
"A":["matematicas","Contabilidad"],
"B":["modulo","submodulo"],
"C":["clase"],
"D":["docente"]
}
for nodo in grafo:
    print(f"{nodo}el nodo establecido es: {grafo[nodo]}")



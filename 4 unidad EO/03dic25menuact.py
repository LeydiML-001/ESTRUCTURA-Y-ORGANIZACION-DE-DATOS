#1.- BUSQUEDA DE LISTAS
def listain():
    n=[1,2,3,4]
    print(n)
    n1=int(input("Ingresa el numero que quieres buscar "))
    print(n1 in n)
listain()

#index
#DEF
def index():
    a=[2,4,6,8,9]
    print(a)
    a2=int(input("Ingresa el numero que quieres buscar "))
    print(a.index(a2))
index()

#bucles
#DEF
def bucle():
    num1=[1,2,3,4,5,6,7,8,9]
    print(num1)
    n3=int(input("Ingresa el numero que quieres buscar "))
    for n3 in num1:
        if n3==input:
            print("Numero encontrado")
bucle()
#Busqueda con comprensión
#DEF
def busqueda():
    lista0=[2,4,6,8,9]
    print(lista0)
    encontrar2=int(input("Ingresa el numero que quieras saber la posicion "))
    posicion=[i for i, x in enumerate(lista0) if x>encontrar2]
    print("estas son las pocisiones que tiene la lista: ", posicion)
busqueda()

#2.- Busquedas de cadenas "String"
#.find()
#DEF
def find ():
    i= "python es el mejor"
    print("La oracion es:", i)
    buscar1=input("Ingresa la palabra que quieras encontrar conforme a la oracion: ")
    print(i.find(buscar1))
find()

#.index
#DEF
def index1():
    m="hola mundo"
    print("La oracion es:", m)
    buscar2=input("Ingresa la palabra que quieres buscar en la oración: ")
    print(m.index(buscar2))
index1()

#.startwith
#DEF
def startwith():
    m3="programar es mi pasion"
    buscar3=input("Ingresa las primeras letras de la oracion: ")
    print(m3.startswith(buscar3))

#.endwith
#INPUT
#DEF
def endwith():
    m4="programar es mi pasion"
    print(m4)
    buscar4=input("Ingresa las ultimas letras de la oracion: ")
    print(m4.endswith(buscar4))

#3.- BUSQUEDA POR DICCIONARIOS
#INPUT
#DEF
def diccionario ():
    d= {"a":1,"b":2,"c":3,"d":4,"e":5}
    print(d)
    encontrar=input("Ingresa la letras para saber que valor tiene entre comillas")
    print(d.get(encontrar))
diccionario()

#BUSQUEDA POR VALORES
#DEF
def busqueda1():
    d1= {"x":10,"y":20}
    print(d1)
    encontrar1=input("Ingresa la letra para imprimir los valores que tienen las claves")
    buscar5=[k for k, v in d1.items() if v == encontrar1]
    print(buscar5)
busqueda1()

#4.- BUSQUEDA AVANZADA
#busqueda binaria(bisect)
#DEF
import bisect
def bs():
    lista1=[1,2,3,4,5,6,7]
    print(lista1)
    bis=int(input("Ingresa un numero para encontrar su posicion(bisect): "))
    pos=bisect.bisect_left(lista1, bis) #indica la posicion del numero
    print(pos)
bs()

#Grafos y arboles
#DEF
grafo={
    "A":["B","C"],
    "B":["D"],
    "C":[],
    "D":[]
}
def dfs(nodo):
    print(nodo)
    for vecino in grafo[nodo]:
        dfs(vecino)
dfs("A")
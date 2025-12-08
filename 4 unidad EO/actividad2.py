def listain():
    n=[1,2,3,4]
    print(n)
    n1=int(input("Ingresa el numero que quieres buscar "))
    print(n1 in n)

def index():
    a=[2,4,6,8,9]
    print(a)
    a2=int(input("Ingresa el numero que quieres buscar "))
    print(a.index(a2))

def bucle():
    num1=[1,2,3,4,5,6,7,8,9]
    print(num1)
    n3=int(input("Ingresa el numero que quieres buscar "))
    for n3 in num1:
        if n3==input:
            print("Numero encontrado")

def compresion():
    lista0=[2,4,6,8,9]
    print(lista0)
    encontrar2=int(input("Ingresa el numero que quieras saber la posicion "))
    posicion=[i for i, x in enumerate(lista0) if x>encontrar2]
    print("estas son las pocisiones que tiene la lista: ", posicion)

def find ():
    i= "python es el mejor"
    print("La oracion es:", i)
    buscar1=input("Ingresa la palabra que quieras encontrar conforme a la oracion: ")
    print(i.find(buscar1))

def index1():
    m="hola mundo"
    print("La oracion es:", m)
    buscar2=input("Ingresa la palabra que quieres buscar en la oración: ")
    print(m.index(buscar2))

def startwith():
    m3="programar es mi pasion"
    print(m3)
    buscar3=input("Ingresa las primeras letras de la oracion: ")
    print(m3.startswith(buscar3))

def endwith():
    m4="programar es mi pasion"
    print(m4)
    buscar4=input("Ingresa las ultimas letras de la oracion: ")
    print(m4.endswith(buscar4))

def diccionario ():
    d= {"a":1,"b":2,"c":3,"d":4,"e":5}
    print(d)
    encontrar=input("Ingresa la letras para saber que valor tiene entre comillas")
    print(d.get(encontrar))

def busqueda1():
    d1= {"x":10,"y":20}
    print(d1)
    encontrar1=input("Ingresa la letra para imprimir los valores que tienen las claves")
    buscar5=[k for k, v in d1.items() if v == encontrar1]
    print(buscar5)

import bisect
def bs():
    lista1=[1,2,3,4,5,6,7]
    print(lista1)
    bis=int(input("Ingresa un numero para encontrar su posicion(bisect): "))
    pos=bisect.bisect_left(lista1, bis) 
    print(pos)

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
 

def menu():
    while True:
        print("---Menu de mi ordeamiento---")
        print("1. Busqueda de listas")
        print("2. Busquedas de cadenas")
        print("3. Busqueda por diccionarios")
        print("4. Buqueda avanzada")
        print("5. Salir")
        opcion=input("Selecciona una opcion(1-5): ")

        if opcion=="1":
             while True:
                print("---Menu de Busqueda de listas---")
                print("1. In")
                print("2. Index")
                print("3. Bucles")
                print("4. Con comprensión")
                print("5. Salir")

                sub=input("Selecciona una opcion(1-5): ")

                if sub=="1":
                    listain()

                elif sub=="2":
                    index()

                elif sub=="3":
                    bucle()

                elif sub=="4":
                    compresion()

                elif sub=="5":
                 print("Saliste del programa")
                 break

        elif opcion=="2":
            
             while True:
                print("---Menu de Busquedas de cadenas---")
                print("1. Find")
                print("2. Index")
                print("3. Startwith")
                print("4. Endwith")
                print("5. Salir")

                sub=input("Selecciona una opcion(1-5): ")

                if sub=="1":
                    find()

                elif sub=="2":
                    index1()

                elif sub=="3":
                    startwith()

                elif sub=="4":
                    endwith()

                elif sub=="5":
                 print("Saliste del programa")
                 break

        elif opcion=="3":
            while True:
                print("---Menu de Busqueda por diccionarios---")
                print("1. Busqueda de diccionario")
                print("2. Busqueda de valores")
                print("3. Salir")

                sub=input("Selecciona una opcion(1-5): ")

                if sub=="1":
                    diccionario()

                elif sub=="2":
                    busqueda1()
                
                elif sub=="3":
                 print("Saliste del programa")
                 break

        elif opcion=="4":
            while True:
                print("---Menu de Buqueda avanzada---")
                print("1. Busqueda de bs")
                print("2. Busqueda de dfs")
                print("3. Salir")

                sub=input("Selecciona una opcion(1-5): ")

                if sub=="1":
                    bs()

                elif sub=="2":
                    dfs("A")  

                elif sub=="3":
                 print("Saliste del programa")
                 break

        elif opcion=="5":
            print("Saliste del programa")
            break       
if __name__ == "__main__":
 menu()

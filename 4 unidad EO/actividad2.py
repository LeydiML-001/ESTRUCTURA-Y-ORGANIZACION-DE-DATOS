#metodos de busqueda(busqueda de listas)
#in
def nu():
    num=[1,2,3,4]
    print(num)
    y=input("ingresa el numero que quieres buscar:")
    print(y)
nu()

#index
def r():
    li=[2,4,6,9]
    print(li)
    li=int(input("ingre el numero que quieras buscar:"))
print(r)
r()

#bucles
def bucles():
    buc=[1,2,3,4,5,6]
    print(buc)
    buc=input("ingres el numero que quieras buscar:")
    print(bucles)
bucles()

#busqueda con compresion
def compresion():
    lista3=[2,4,6,8,9,5]
    print(lista3)
    posicion=input("ingresa el numero que quieras buscar:")
    print(posicion in lista3)
compresion()

#busueda de cadenas(strings)
#.find() 
def find():
    s="python es el mejor"
    print(s)
    busqueda=input("ingresa el numero que quieras buscar:")
    print(s.find(busqueda))
find()

#.index
def index():
    o="hola mundo"
    print(o)
    letras=input("ingresa el numero que quieras buscar:")
    print(o.index(letras))
index()

#statswith
def starswith():
    m="programacion"
    print(m)
    palabras=input("ingresa el numero que quieras buscar:")
    print(m.startswith(palabras))

#endswith
def endswith():
    u="caracteres"
    print(u)
    d1=input("ingresa el numero que quieras buscar:")
    print(u.endswith(d1))
endswith()

#busqueda por diccionarios
def diccionarios():
    f={"g":1, "h":2}
    print(f)
    d2=input("ingresa el numero que quieras buscar:")
    print(f.get(d2))
diccionarios()

#busqueda por valores
def valores():
    j={"b":12, "c":14}
    print(j)
    d3=input("ingresa el numero que quieras buscar:")
    print(d3 in j)
valores()

#busqueda por archivos
def archivos():
    archivos="arboles.txt"
    print(archivos)
    archivos=input("ingresa el numero que quieras buscar:")
    print("encontrado",archivos.strip())
archivos()

#BUSQUEDA AVANZADA
def busqueda_avanzada():
    metodo=[1,2,4,6]
    print(metodo)
    ps=input("ingresa el numero que quieras buscar:")
    print(ps)
busqueda_avanzada()
 
def menu():
    while True:
        print("--- MENÚ DE ORDENAMIENTO ---")
        print("1. Busqueda de listas")
        print("2. Busqueda de cadenas")
        print("3. busqueda de valores")
        print("4. Busqueda de archivos")
        print("5. Método de busqueda organizada")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            while True:
                y=input("ingresa el numero que quieres buscar:")
                print(y in nu)

          
if __name__ == "__main__":
    menu()

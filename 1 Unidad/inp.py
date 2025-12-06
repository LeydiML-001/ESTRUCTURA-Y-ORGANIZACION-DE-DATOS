input
entrada=input("Agrega algo:")
print(entrada)
entrada=int(input("Agrega un numero:"))
numero=input("Agrega datos separados por una coma:")
entrada=numero.split(",")
print(entrada)

lista=[]
n1=input("Ingresa algo:")
n2=input("Ingresa otro dato:")
n3=input("Ingresa otro:")
lista=[n1,n2,n3]
print(lista)

pila=[]
elem1=int(input("ingresa un valor:"))
pila.append(elem1)
elem2=int(input("ingresa un valor:"))
pila.append(elem2)
print(pila)

despilado=pila.pop()
print(despilado)


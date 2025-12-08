#metodos de busqueda(busqueda de listas)
#in
num=[1,2,3,4,5,6,7,8,9]
print("dos" in num)

num1=["tele", "ojo"]
print("datos" in num1)

#index
lista1=[2,4,6,8,9]
print(lista1.index(2))

lista2=["ojo","tele","celular"]
print(lista2.index("ojo"))

lista3=["ojo",1,"tele",2]
print(lista3.index("tele"))

#bucles
nums=[1,2,3,4,5,6]
for n in nums:
    if n==2:
        print("numero encontrado")
    else:
        print("numero no en la lista")  
        break   

#realizar cadena de texto

#busqueda con compresion
lista0=[2,4,6,8,9,5]
posicion=[i for i, x in enumerate(lista0)if x==4]#x>0 o x==2 para imprimir la posicion de la lista
print("oyeeeeee esto es la posicion del numero que tu buscas:",posicion)

letras=["sol","verso","arco"]
posicion=[i for i, x in enumerate(letras)if x > 0 ]#x>0 o x==2 para imprimir la posicion de la lista
print("oyeeeeee esto es la posicion de la letra que tu buscas:",posicion)
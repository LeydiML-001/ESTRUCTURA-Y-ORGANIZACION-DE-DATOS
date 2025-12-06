# Accedemos a la posicion o numero
lista = [10, 20, 30, 40, 50]
print(lista[2])

# Se agregan datos
lista.append(60)
print(lista)

# eliminacion de un dato en especifico
lista.remove(10)
print(lista)

# para ingresar un valor en consola
lista1 = int(input("ingresa un numero:"))
lista.append(lista1)
lista2 = int(input("ingresa un numero:"))
lista.append(lista2)
lista3 = int(input("ingresa un numero:"))
lista.append(lista3)
lista4 = int(input("ingresa un numero:"))
lista.append(lista4)
print(lista)

lista.remove(60)
print("lista final:", lista)

# No llevan comillas ya que se trata de una condicion
lista = [True, False]
print(lista)

# Caracteres y letras siempre llevan comillas
lista = [20, "*", 30, "Jesus", False, 12.55]
print(lista)

# Imprimir la consola vacia 
lista = []  # Nueva lista vacía

lista1 = int(input("ingresa un numero:"))
lista.append(lista1)

lista2 = float(input("ingresa un numero decimal:"))  # float
lista.append(lista2)

lista3 = input("ingresa un caracter:")  # input, no varchar
lista.append(lista3)

entrada_bool = input("ingresa True o False: ")
if entrada_bool.lower() == "true":
    lista4 = True
elif entrada_bool.lower() == "false":
    lista4 = False
else:
    lista4 = bool(entrada_bool)  # Cualquier otra entrada
lista.append(lista4)

lista5 = input("ingresa una palabra:")  # input para string
lista.append(lista5)  # append(lista5), no append(lista4)

print(lista)
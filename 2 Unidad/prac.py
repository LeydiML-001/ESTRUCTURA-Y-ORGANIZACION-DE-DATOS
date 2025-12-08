#Lista vacia
lista=[]
nombre=input("Ingresa un nombre:")
lista.append(nombre)
edad=int(input("Ingresa un edad:"))
lista.append(edad)
genero=(input("Ingresa un genero:"))
lista.append(genero)
nacimiento=int(input("Ingresa un fecha de nacimiento:"))
lista.append(nacimiento)
hobbie=input("Ingresa un hobbie:")
lista.append(hobbie)
print(lista)
#Eliminar lista
lista.remove(hobbie)
print(lista)
# Buscar elementos
existe=edad in lista
print("el numero 19 existe en mi lista",existe)
# Insertar multiples elementos
lista.extend(["donde naci es playa vicente","mi carrera es tics","tener una profesion relacionada con la seguridad"])
print("despues de agregar lugar de nacimiento, carrera y proximo futuro la lista es:",lista)
# Agregar 2 cosas que más nos guste
gustos=input("Ingresa dos cosas que mas te guste:")
lista.append(gustos)

# Longitud de lista
print("L longitud es:",len(lista))

# Lista para strings 
lista_strings = [nombre, hobbie, "donde naci es playa vicente", "mi carrera es tics", "tener una profesion relacionada con la seguridad"]

# Lista para números 
lista_numeros = [edad, nacimiento]

# Ordenar cada lista por separado
lista_strings.sort()
lista_numeros.sort()

print("Strings ordenados:", lista_strings)
print("Numeros ordenados:", lista_numeros)

lista.clear()
print("mi lista despues de limpiar es:",lista)
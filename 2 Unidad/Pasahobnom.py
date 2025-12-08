lista=[]
lista.append("Luisa")
lista.append("Leydi")
lista.append("Moreno")
lista.append("Lopez")
print("Mi Nombre Completo es:",lista)

# Insertar multiples elementos
lista.extend(["tengo 19 años"])
print("despues de agregar mi edad a la lista es:",lista)

lista.extend(["me gusta salir a caminar por las tardes y jugar con mis mascotas"])
print("despues de agregar mi pasatiempo a la lista es:",lista)

lista.extend(["Escuchar musica"])
print("despues de agregar mi hobie a la lista es:",lista)

# Longitud de lista
print("L longitud es:",len(lista))

# Ordenar mi lista
lista.sort()
print("mi lista ordenada es:",lista)

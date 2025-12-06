lista = [1, 2, 3, "pedro", "juan", 10]
print(lista)

print("El dato en posición 2 es:", lista[2])  # Esto imprimiría 3

lista.append(11)
lista.append("luis")
print("Lista después de agregar elementos:", lista)

lista.remove("juan")
print("Lista después de eliminar 'juan':", lista)
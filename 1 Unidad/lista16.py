lista=[1,"Casco",2,"Ropa",3,"Pans",4,"Gorra",4,"Morral",5,"Bolso",6,"Peine",7,"Zapato",8]                
print("la primera posicion es:",lista[0])
lista.insert(0,18)
print("el nuevo elemento:",lista)
lista.remove("Casco")
print("lista final:",lista)

from collections import deque
cola=deque()
cola.append("Leydi")
cola.append("Lopez")
cola.append("Rivero")
cola.append(12)
cola.append(9)
cola.append(24)
cola.append("Ciclismo")
cola.append("caminar")
print("La cola es",list(cola))

elemento = cola.popleft()
print("Elemento eliminado:", elemento)
print("La cola después de eliminar:", list(cola))

pila = []
pila.append("j")
pila.append("k")
pila.append("l")
pila.append("m")
pila.append("n")
pila.append("ñ") 
pila.append("o")
pila.append("p")
print("La pila es:", pila)
elemento = pila.pop()
print("Elemento eliminado:", elemento)
print("La pila después de eliminar:",pila)


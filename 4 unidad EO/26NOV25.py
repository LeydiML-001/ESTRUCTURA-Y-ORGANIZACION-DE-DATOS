#ordenamiento, metodo burbuja este metodo ayuda a ordenar a datos cortos una amtriz o una lista con 5 datos en particular metodo burbuja
#def burbuja(lista):
def burbuja(lista):
    for x in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[i]> lista[i+1]:
                lista[i],lista[i+1]=lista[i+1],lista[i]
                return lista
                
#no esta permitido utilizar x como variable por que marca error de sintessis y no va a imprikmir nadaa e estara vacio en consola
#seleccion
def seleccion(lista1):
    for i in range(len(lista1)):
        menor = i
        for j in range(i+1, len(lista1)):
            if lista1[j] < lista1[menor]:
                menor = j
        lista1[i], lista1[menor] = lista1[menor], lista1[i]
    return lista1
                
#insercion va a mover todos los numeros hacia aras hasta que este ordenado
def insercion(lista2):
    for i in range(1, len(lista2)):
        valor = lista2[i]
        j = i-1
        while j >= 0 and lista2[j] > valor:
            lista2[j+1] = lista2[j]
            j -= 1
        lista2[j+1] = valor
    return lista2

        
#mezcla valores entre si
def mezcla(lista3):
    if len(lista3) <= 1:
        return lista3
    medio=len(lista3)//2
    izquierda=lista3 (lista3[:medio])
    derecha=lista3 (lista3[medio:])
    resultado=[]
    while izquierda and derecha:
        if izquierda[0] < derecha[0]:
            resultado.append(izquierda.pop(0))
    else:
            resultado.append(derecha.pop)

    return resultado + izquierda + derecha


#metodo rapido
def rapido(lista4):
    if len(lista4) <=1:
        return lista4
    pivote=lista4[0]
    menores=[x for x in lista4[1:]if x < pivote]
    mayores=[x for x in lista4[1:]if x >= pivote]
    return rapido(menores)+[pivote] + rapido(mayores)

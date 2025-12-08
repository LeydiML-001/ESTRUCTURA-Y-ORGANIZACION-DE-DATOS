# Método Burbuja - ordena intercambiando elementos adyacentes
def burbuja(lista):
    lista_ordenada = lista.copy()
    n = len(lista_ordenada)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_ordenada[j] > lista_ordenada[j+1]:
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
    return lista_ordenada

# Método Selección - busca el menor y lo coloca al inicio
def seleccion(lista):
    lista_ordenada = lista.copy()
    n = len(lista_ordenada)
    for i in range(n):
        menor = i
        for j in range(i+1, n):
            if lista_ordenada[j] < lista_ordenada[menor]:
                menor = j
        lista_ordenada[i], lista_ordenada[menor] = lista_ordenada[menor], lista_ordenada[i]
    return lista_ordenada

# Método Inserción - mueve elementos hacia atrás hasta encontrar su posición
def insercion(lista):
    lista_ordenada = lista.copy()
    for i in range(1, len(lista_ordenada)):
        valor = lista_ordenada[i]
        j = i - 1
        while j >= 0 and lista_ordenada[j] > valor:
            lista_ordenada[j+1] = lista_ordenada[j]
            j -= 1
        lista_ordenada[j+1] = valor
    return lista_ordenada

# Método Mezcla (Merge Sort) - divide y vencerás
def mezcla(lista):
    if len(lista) <= 1:
        return lista.copy()
    
    # Dividir la lista en dos mitades
    medio = len(lista) // 2
    izquierda = mezcla(lista[:medio])
    derecha = mezcla(lista[medio:])
    
    # Combinar las dos mitades ordenadas
    return mezclar(izquierda, derecha)

def mezclar(izquierda, derecha):
    resultado = []
    i = 0 
    j = 0 
    
    # Comparar elementos de ambas listas
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Agregar los elementos restantes de izquierda (si los hay)
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1
    
    # Agregar los elementos restantes de derecha (si los hay)
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1
    
    return resultado

# Método Rápido 
def rapido(lista):
    if len(lista) <= 1:
        return lista.copy()
    
    pivote = lista[0]
    menores = []
    iguales = []
    mayores = []
    
    # Separar elementos según el pivote
    for elemento in lista:
        if elemento < pivote:
            menores.append(elemento)
        elif elemento == pivote:
            iguales.append(elemento)
        else:
            mayores.append(elemento)
    
    return rapido(menores) + iguales + rapido(mayores)

def convertir_a_numeros(entrada):
    numeros = []
    if not entrada.strip():  
        return numeros
    
    partes = entrada.split()
    for parte in partes:
        es_numero = True
        puntos = 0  
        for caracter in parte:
            if caracter == '.':
                puntos += 1
                if puntos > 1:  
                    es_numero = False
                    break
            elif not caracter.isdigit() and caracter != '-':  
                es_numero = False
                break
        
        if es_numero:
            if '.' in parte:
                numeros.append(float(parte))
            else:
                numeros.append(int(parte))
        
    return numeros

def menu():
    while True:
        print("MENÚ DE MÉTODOS DE ORDENAMIENTO")
        print("1. Método Burbuja")
        print("2. Método Selección")
        print("3. Método Inserción")
        print("4. Método Mezcla (Merge Sort)")
        print("5. Método Rápido (Quick Sort)")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            entrada = input("Ingresa números separados por espacios: ")
            numeros = convertir_a_numeros(entrada)
            if numeros:
                print(f"Lista original: {numeros}")
                resultado = burbuja(numeros)
                print(f"Lista ordenada con Burbuja: {resultado}")
            else:
                print("Error: No se ingresaron números válidos")
                
        elif opcion == "2":
            entrada = input("Ingresa números separados por espacios: ")
            numeros = convertir_a_numeros(entrada)
            if numeros:
                print(f"Lista original: {numeros}")
                resultado = seleccion(numeros)
                print(f"Lista ordenada con Selección: {resultado}")
            else:
                print("Error: No se ingresaron números válidos")
                
        elif opcion == "3":
            entrada = input("Ingresa números separados por espacios: ")
            numeros = convertir_a_numeros(entrada)
            if numeros:
                print(f"Lista original: {numeros}")
                resultado = insercion(numeros)
                print(f"Lista ordenada con Inserción: {resultado}")
            else:
                print("Error: No se ingresaron números válidos")
                
        elif opcion == "4":
            entrada = input("Ingresa números separados por espacios: ")
            numeros = convertir_a_numeros(entrada)
            if numeros:
                print(f"Lista original: {numeros}")
                resultado = mezcla(numeros)
                print(f"Lista ordenada con Mezcla: {resultado}")
            else:
                print("Error: No se ingresaron números válidos")
                
        elif opcion == "5":
            entrada = input("Ingresa números separados por espacios: ")
            numeros = convertir_a_numeros(entrada)
            if numeros:
                print(f"Lista original: {numeros}")
                resultado = rapido(numeros)
                print(f"Lista ordenada con Rápido: {resultado}")
            else:
                print("Error: No se ingresaron números válidos")
                
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
     menu()
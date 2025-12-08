# elaboración al cuadrado de cualquier número
def potencia_cuadrado(base):
    return base ** 2

# elaboración al cubo de cualquier número
def potencia_cubo(base):
    return base ** 3

# realizar un conteo hacia atrás y al final diga ¡go!
def cuenta_regresiva(numero):
    if numero <= 0:
        print("¡go!")  # Cambiado de "¡Despegue!" a "¡go!"
        return
    print(numero)
    cuenta_regresiva(numero - 1)

# factorial de número flotante usando la función gamma
def factorial(n):
    import math
    # Para números enteros
    if n == int(n) and n >= 0:
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    # Para números decimales usando la función gamma
    else:
        return math.gamma(n + 1)

# ejemplo de palíndromo
def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return palindromo(palabra[1:-1])

# 4 números y sacar promedio (porcentaje)
def promedio():
    numeros = []
    for i in range(4):
        numero = float(input(f"Ingresa el número {i+1}: "))
        numeros.append(numero)
    
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return promedio

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Potencia al cuadrado")
        print("2. Potencia al cubo")
        print("3. Cuenta Regresiva")
        print("4. Factorial")   
        print("5. Palíndromo")
        print("6. Promedio")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            base = int(input("Ingresa la base: "))
            print(f"Resultado: {potencia_cuadrado(base)}")

        elif opcion == "2":
            base = int(input("Ingresa la base: "))
            print(f"Resultado: {potencia_cubo(base)}")

        elif opcion == "3":
            n = int(input("Ingresa un número para cuenta regresiva: "))
            cuenta_regresiva(n)
        
        elif opcion == "4":
            n = float(input("Ingresa un número (puede ser decimal): ")) 
            print(f"Factorial: {factorial(n)}")

        elif opcion == "5":
            palabra = input("Ingresa una palabra: ")
            resultado = palindromo(palabra)
            if resultado:
                print(f"'{palabra}' es un palíndromo")
            else:
                print(f"'{palabra}' no es un palíndromo")

        elif opcion == "6":
            resultado = promedio()
            print(f"El promedio es: {resultado}")

        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
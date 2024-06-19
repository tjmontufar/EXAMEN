# Ejercicio 4: Escribir un programa que pida al usuario un numero entero y muestre por pantalla si
# es par o impar.

numero = 0
while True:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    numero = int(input("Ingrese un numero entero: "))

    if numero == -1:
        break
    
    if numero % 2 == 0:
        print("El numero ",numero," es par.")
    else:
        print("El numero ",numero," es impar.")
    
    input("Presione Enter para continuar...")
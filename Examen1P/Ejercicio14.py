# Ejercicio 14: Escribir un programa que pida al usuario un numero entero positivo y muestre por
# pantalla la cuenta atras desde ese numero hasta cero.

while True:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    entero = int(input("Ingrese un numero entero positivo: "))

    if entero == -1:
        break

    if entero <= 0:
        print("El numero ingresado debe ser mayor que 0, intentelo de nuevo...")
        input("Presione Enter para continuar...")
    else:
        while entero != -1:
            print(entero)
            entero -= 1
        input("Presione Enter para continuar...")
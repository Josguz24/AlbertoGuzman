import math  # Importamos la biblioteca math para realizar operaciones matemáticas, como la raíz cuadrada

opcion = 0  # Tipo: int. Inicializamos la variable que controla el ciclo while

# Ciclo que se ejecuta hasta que la opción sea igual a 7 (salir)
while opcion < 7:
    # Menú de operaciones
    print("Bienvenido a la Calculadora\n"
        "Selecciona la operación que deseas realizar:\n"
        "1) Suma\n"
        "2) Resta\n"
        "3) Multiplicación\n"
        "4) División\n"
        "5) Elevar al exponente\n"
        "6) Raíz cuadrada\n"
        "7) Salir")

    # Solicitamos al usuario que elija una operación
    opcion = int(input("\nIntroduce el número de la operación (1-7): "))  # Convertimos la opción a entero

    # Validamos que la opción esté dentro del rango permitido
    if opcion < 1 or opcion > 7:
        print("\nOpción no válida. Por favor, elige un número entre 1 y 7.")
    else:
        # Si la operación no es raíz cuadrada (opción 6), pedimos dos números
        if 0 < opcion <= 4:
            num1 = float(input("Introduce el primer número: "))  # Convertimos el input a número decimal (float)
            num2 = float(input("Introduce el segundo número: "))  # Segundo número
        
        # Para la opción 5 (elevar al exponente), también pedimos dos números
        if opcion == 5:
            num1 = float(input("Introduce el primer número: "))  # Base
            num2 = float(input("Introduce el valor del exponente: "))  # Exponente

        # Si la opción es raíz cuadrada (opción 6), solo necesitamos un número
        if opcion == 6:
            num = float(input("Introduce el número: "))  # Solo un número para la raíz cuadrada
        
        # Realizamos la operación elegida según la opción
        if opcion == 1:  # Suma
            resultado = num1 + num2
            print(f"\nEl resultado de la suma {num1} + {num2} es: {resultado}")
        elif opcion == 2:  # Resta
            resultado = num1 - num2
            print(f"\nEl resultado de la resta {num1} - {num2} es: {resultado}")
        elif opcion == 3:  # Multiplicación
            resultado = num1 * num2
            print(f"\nEl resultado de la multiplicación {num1} * {num2} es: {resultado}")
        elif opcion == 4:  # División
            if num2 == 0:  # Validamos que no se divida por cero
                print("\nError: No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print(f"\nEl resultado de la división {num1} / {num2} es: {resultado}")
        elif opcion == 5:  # Elevar al exponente
            resultado = num1 ** num2  # Elevar num1 a num2
            print(f"\nEl resultado de {num1} elevado a {num2} es: {resultado}")
        elif opcion == 6:  # Raíz cuadrada
            if num < 0:  # Validamos que el número no sea negativo
                print("\nError: No se puede calcular la raíz cuadrada de un número negativo.")
            else:
                resultado = math.sqrt(num)  # Usamos la función sqrt() de math
                print(f"\nEl resultado de la raíz cuadrada de {num} es: {resultado}")
        elif opcion == 7:  # Salir
            print("Nos vemos pronto")

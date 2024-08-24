#Temas a utilizar Variables,Strings,Concatenar,Suma, resta, multiplicación y división,El condicional IF y operadores de comparación
#El condicional IF ELSE,while

salir = 'B'  # Variable para controlar el ciclo

# Solicitar nombre y edad
nombre, edad = str(input("Cual es tu nombre? ")), int(input("que edad tienes: "))
print(f'Bienvenido a mi codigo {nombre} ')

# Preguntar si quiere realizar una operación matemática
pregunta = input("Quieres que realice una operación matematica?\n Escribe 'S' para sí o 'N' para no \n")

# Inicia el ciclo
while salir != 'a':
    if pregunta == 's': 
        # Seleccionar la operación
        Operación = int(input("\nSelecciona el numero de la operación a realizar \n1)suma \n2)resta \n3)multiplicacion \n4)division\n "))
        
        # Realizar la operación seleccionada
        if Operación == 1:
            Num1, Num2 = int(input("Digita el primer numero")), int(input("Digita el segundo numero: "))
            Res = Num1 + Num2
        elif Operación == 2:
            Num1, Num2 = int(input("Digita el primer numero")), int(input("Digita el segundo numero: "))
            Res = Num1 - Num2
        elif Operación == 3:
            Num1, Num2 = int(input("Digita el primer numero")), int(input("Digita el segundo numero: "))
            Res = Num1 * Num2
        elif Operación == 4:
            Num1, Num2 = int(input("Digita el primer numero")), int(input("Digita el segundo numero: "))
            Res = Num1 / Num2
        
    # Preguntar si quiere salir
    salir = input(f'{nombre} el resultado de tu operación es: {Res}\n\n Si quieres salir presiona la letra A, de lo contrario presiona cualquier otra tecla: ')

# Despedida
print('NOS VEMOS PRONTO')



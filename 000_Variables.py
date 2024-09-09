#Temas a utilizar Variables,Strings,Concatenar,Suma, resta, multiplicación y división,El condicional IF y operadores de comparación
#El condicional IF ELSE,while
salir = 'B'  # Tipo: String. Controla el ciclo while

# Solicitar nombre y edad
nombre = str(input("Cual es tu nombre? "))  # Tipo: String. Convierte el input a texto
edad = int(input("que edad tienes: "))  # Tipo: int. Convierte el input a número entero

print(f'Bienvenido a mi codigo {nombre} ')  # Tipo: String. Imprime un mensaje con el nombre del usuario

# Preguntar si quiere realizar una operación matemática
pregunta = input("Quieres que realice una operación matematica?\n Escribe 'S' para sí o 'N' para no \n")  
# Tipo: String. Recibe la respuesta del usuario

operacion_realizada = False  # Tipo: bool. Inicialmente en False, cambia a True cuando se realice una operación

# Inicia el ciclo while
while salir != 'a':  # El ciclo sigue hasta que salir sea igual a 'a'
    if pregunta == 's':  # Si el usuario responde 's', se hace la operación
        Operación = int(input("\nSelecciona la operación:\n1)suma \n2)resta \n3)multiplicacion \n4)division\n "))
        # Tipo: int. Elige la operación según la opción seleccionada

        if Operación == 1:  # Suma
            Num1 = float(input("Digita el primer numero: "))  # Tipo: float. Convierte el input a decimal
            Num2 = float(input("Digita el segundo numero: "))  # Tipo: float
            Res = Num1 + Num2  # Tipo: float. Realiza la suma
            operacion_realizada = True  # Cambia a True, indicando que se realizó una operación
        elif Operación == 2:  # Resta
            Num1 = float(input("Digita el primer numero: "))
            Num2 = float(input("Digita el segundo numero: "))
            Res = Num1 - Num2  # Tipo: float. Realiza la resta
            operacion_realizada = True
        elif Operación == 3:  # Multiplicación
            Num1 = float(input("Digita el primer numero: "))
            Num2 = float(input("Digita el segundo numero: "))
            Res = Num1 * Num2  # Tipo: float. Realiza la multiplicación
            operacion_realizada = True
        elif Operación == 4:  # División
            Num1 = float(input("Digita el primer numero: "))
            Num2 = float(input("Digita el segundo numero: "))
            Res = Num1 / Num2  # Tipo: float. Realiza la división
            operacion_realizada = True
        
    # Pregunta si quiere salir
    if operacion_realizada:  # Verifica si se realizó una operación antes de mostrar el resultado
        salir = input(f'{nombre} el resultado es: {round(Res,2)}\nPresiona A para salir, o cualquier otra tecla para continuar: ')
    else:
        salir = input(f'No se realizó ninguna operación, {nombre}.\nPresiona A para salir, o cualquier otra tecla para continuar: ')
    
# Despedida
print('NOS VEMOS PRONTO')  # Imprime un mensaje final de despedida

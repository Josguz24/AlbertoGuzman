# Contraseña correcta
password_correcta = "python123"

# Inicializamos la variable de contraseña ingresada
password_ingresada = ""

# Usamos un ciclo while para pedir la contraseña hasta que sea correcta
while True:  # Ciclo infinito hasta que se cumpla la condición de salida
    password_ingresada = input("Por favor, ingresa la contraseña: ")

    # Usamos un condicional if para verificar si la contraseña es correcta
    if password_ingresada == password_correcta:
        print("¡Contraseña correcta! Acceso permitido.")
        break  # Si la contraseña es correcta, salimos del bucle
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")

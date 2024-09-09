# Funciones UPPER(), LOWER(), TITLE().

bienvenida = 'Hola, como te llamas?'  # Tipo: String. Cadena de texto para dar la bienvenida al usuario

# Usamos el método title() para capitalizar la primera letra de cada palabra en la cadena de bienvenida
nombre = input(bienvenida.title())  # Tipo: String. Convierte la cadena de bienvenida a Title Case y captura el nombre

# Pedimos al usuario que escriba un mensaje
mensaje = input(f"bienvenido {nombre.upper()}, escribe un mensaje:\n")  
# Tipo: String. Muestra el nombre en mayúsculas (upper()) y captura el mensaje del usuario

# Solicitamos al usuario que elija una opción para modificar su mensaje
opc = int(input("¿Qué deseas hacer con el mensaje?\n1) La primera letra de cada palabra en mayúscula\n2) Todo en mayúsculas\n3) Todo en minúsculas\n"))  
# Tipo: int. Captura la opción elegida y la convierte a número entero

if opc == 1:
    # usamos title() para capitalizar la primera letra de cada palabra
    print("Este es tu mensaje:\n", mensaje.title())  
    # Tipo: String. Convierte el mensaje a Title Case (primera letra de cada palabra en mayúsculas)
elif opc == 2:
    # usamos upper() para convertir todo el texto a mayúsculas
    print("Este es tu mensaje:\n", mensaje.upper())  
    # Tipo: String. Convierte el mensaje a mayúsculas
elif opc == 3:
    # usamos lower() para convertir todo el texto a minúsculas
    print("Este es tu mensaje:\n", mensaje.lower())  
    # Tipo: String. Convierte el mensaje a minúsculas


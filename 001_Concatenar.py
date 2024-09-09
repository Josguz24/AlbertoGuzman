import datetime  # Importa el módulo datetime para trabajar con fechas y horas

# Ingrese su nombre
nombre = input("Ingresa tu nombre: ")  # Tipo: String. Captura el nombre del usuario

# Ingrese su apellido
apellido = input("Ingresa tu apellido: ")  # Tipo: String. Captura el apellido del usuario

# Concatenar nombre y apellido
nombre_completo = nombre + " " + apellido  # Tipo: String. Concatenación de nombre y apellido con un espacio

# Obtener la hora actual
hora_actual = datetime.datetime.now().hour  # Tipo: int. Obtiene la hora actual como un entero (de 0 a 23)

print(hora_actual)  # Muestra la hora actual en formato de 24 horas

# Condicional para determinar el saludo según la hora
if hora_actual < 12:  # Si la hora es menor a 12 (antes del mediodía)
    saludo = "¡Buenos días, " + nombre_completo.title() + "!"  # Tipo: String. Capitaliza el nombre completo
elif 12 <= hora_actual < 18:  # Si la hora está entre 12 y 18 (después del mediodía hasta la tarde)
    saludo = "¡Buenas tardes, " + nombre_completo.title() + "!"
else:  # Si la hora es mayor o igual a 18 (por la noche)
    saludo = "¡Buenas noches, " + nombre_completo.title() + "!"

print(saludo)  # Muestra el saludo personalizado con el nombre completo del usuario




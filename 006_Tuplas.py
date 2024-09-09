# Definimos tres empleados como tuplas, cada una contiene nombre, edad y cargo
empleado1 = ("Juan Pérez", 30, "Desarrollador")  # Tipo: tupla (nombre, edad, cargo)
empleado2 = ("Ana Gómez", 25, "Diseñadora")  # Tipo: tupla
empleado3 = ("Carlos Rodríguez", 35, "Gerente de proyecto")  # Tipo: tupla

# Creamos una lista que contiene todas las tuplas de empleados
empleados = [empleado1, empleado2, empleado3]  # Tipo: lista de tuplas

# Iteramos sobre la lista de empleados
for empleado in empleados:
    nombre, edad, cargo = empleado  # Desempaquetamos la tupla en nombre, edad, y cargo
    print(f"Nombre: {nombre}, Edad: {edad}, Cargo: {cargo}")  # Mostramos los datos de cada empleado

# Calculamos la suma de las edades de todos los empleados usando comprensión de listas
total_edad = sum(empleado[1] for empleado in empleados)  # Tipo: int. Suma las edades de todos los empleados
edad_promedio = total_edad / len(empleados)  # Tipo: float. Calcula la edad promedio dividiendo la suma por la cantidad de empleados
print(f"Edad promedio de los empleados: {edad_promedio:.2f}")  # Imprime la edad promedio con dos decimales

# Accedemos al nombre del segundo empleado en la lista (índice 1)
nombre_segundo_empleado = empleados[1][0]  # Tipo: String. Obtiene el nombre del segundo empleado
print(f"El nombre del segundo empleado es: {nombre_segundo_empleado}")  # Muestra el nombre del segundo empleado

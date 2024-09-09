from datetime import datetime

# Obtener la fecha y hora actual
fecha_actual = datetime.now()

# Mostrar la fecha actual en varios formatos
print("Fecha y hora actual:", fecha_actual)

# Formatear la fecha actual
formato_fecha = fecha_actual.strftime("%d/%m/%Y")
formato_hora = fecha_actual.strftime("%H:%M:%S")

print("Fecha actual formateada:", formato_fecha)
print("Hora actual formateada:", formato_hora)

# Obtener solo el año, mes y día
print(f"Año: {fecha_actual.year}, Mes: {fecha_actual.month}, Día: {fecha_actual.day}")

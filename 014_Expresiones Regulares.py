import re

texto = "El coche rojo va más rápido que el coche azul."

# Usando search() para buscar la primera coincidencia
coincidencia = re.search("coche", texto)
if coincidencia:
    print(f"Se encontró 'coche' en la posición: {coincidencia.start()}")

# Usando findall() para encontrar todas las coincidencias de una palabra
todas_coincidencias = re.findall("coche", texto)
print(f"Se encontraron {len(todas_coincidencias)} coincidencias de 'coche'.")

# Usando split() para dividir el texto por espacios
partes = re.split(r"\s", texto)
print(f"El texto dividido por espacios: {partes}")

# Usando sub() para reemplazar palabras
nuevo_texto = re.sub("coche", "vehículo", texto)
print(f"Texto modificado: {nuevo_texto}")

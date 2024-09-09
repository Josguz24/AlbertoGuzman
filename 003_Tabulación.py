# Definimos la lista de lenguajes de programación
# Definimos la lista de lenguajes de programación
lenguajes = (
    "- Python.\n"
    "- JavaScript.\n"
    "- Java.\n"
    "- PHP.\n"
    "- TypeScript.\n"
    "- SQL.\n"
    "- COBOL.\n"
    "- Rust.\n"
    "- Go.\n"
)  
# Tipo: String. Cadena larga que contiene la lista de lenguajes de programación, con cada lenguaje en una nueva línea

print("Lenguajes de programación disponibles:")
print(lenguajes)  # Muestra la lista de lenguajes en pantalla

# Biblioteca de descripciones (diccionario)
descripciones = {
    "Python": "Un lenguaje poderoso y fácil de aprender, ideal para scripting y data science.",
    "JavaScript": "El lenguaje del front-end web, usado para darle vida a las páginas web.",
    "Java": "Un lenguaje robusto y multiplataforma, muy utilizado en aplicaciones empresariales.",
    "PHP": "El veterano de la web, fundamental para el desarrollo de sitios dinámicos.",
    "TypeScript": "Una versión mejorada de JavaScript, con tipado estático para mayor seguridad.",
    "SQL": "El lenguaje estándar para gestionar bases de datos relacionales.",
    "COBOL": "Un clásico de la programación empresarial, aún en uso en muchos bancos y gobiernos.",
    "Rust": "Conocido por su seguridad de memoria, ideal para sistemas donde la seguridad es clave.",
    "Go": "Creado por Google, combina simplicidad y eficiencia, perfecto para sistemas distribuidos."
}  
# Tipo: diccionario. Contiene las descripciones de cada lenguaje de programación, donde la clave es el nombre del lenguaje y el valor es la descripción.

# Pedir nombre del programa al usuario y darle formato adecuado
opc = input("Ingresa el nombre del programa del que quieres más detalles:\n")  
# Tipo: String. Captura el nombre del lenguaje de programación que el usuario desea más información
opc = opc.title()  # Convierte el texto ingresado a Title Case para asegurar que coincida con las claves del diccionario

# Verificar si el lenguaje existe en el diccionario
if opc in descripciones:  
    # Si el lenguaje existe en el diccionario, se imprime su descripción
    print(f"\nHas elegido {opc}")
    print(f"\tDescripción:\n\t\t{descripciones[opc]}\n\n")  
    # Tipo: String. Imprime el nombre del lenguaje y la descripción correspondiente
else:
    # Si el lenguaje no se encuentra, se informa al usuario
    print(f"\nEl lenguaje {opc} no está en nuestra lista de lenguajes.")

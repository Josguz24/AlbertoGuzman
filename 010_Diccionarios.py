personas = {
    "Juan": 30,
    "Ana": 25,
    "Luis": 40,
    "María": 22
}

print("Lista de personas y sus edades:")
for nombre, edad in personas.items():
    print(f"{nombre} tiene {edad} años.")

# Usamos el método get() para obtener la edad de una persona
persona_buscada = input("Ingresa el nombre de la persona para buscar su edad: ")
edad_persona = personas.get(persona_buscada, "No se encontró a la persona")
print(f"La edad de {persona_buscada} es: {edad_persona}")

# Usamos el método pop() para eliminar una persona
persona_a_eliminar = input("Ingresa el nombre de la persona que deseas eliminar: ")
edad_eliminada = personas.pop(persona_a_eliminar, "No se encontró a la persona")
print(f"Se ha eliminado a {persona_a_eliminar}, quien tenía {edad_eliminada} años.")
print(f"El diccionario actualizado es: {personas}")

# Usamos update() para agregar una nueva persona al diccionario
nueva_persona = input("Ingresa el nombre de la nueva persona: ")
edad_nueva_persona = int(input(f"Ingresa la edad de {nueva_persona}: "))
personas.update({nueva_persona: edad_nueva_persona})
print(f"Se ha agregado a {nueva_persona} con {edad_nueva_persona} años. El diccionario ahora es: {personas}")

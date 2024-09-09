# Pedimos al usuario que ingrese su edad
edad = int(input("Por favor, ingresa tu edad: "))

# Verificamos si la edad es válida
if edad < 0:
    print("Edad no válida. Por favor ingresa una edad correcta.")
else:
    # Clasificamos según el rango de edad
    if edad < 13:
        print("Eres un niño.")
        print("Tienes derecho a entrar gratis al parque de diversiones." if edad < 5 else "Debes pagar entrada infantil para el parque de diversiones.")

    elif 13 <= edad < 18:
        print("Eres un adolescente.")
        permiso_padres = input("¿Tienes permiso de tus padres para salir? (s/n): ").lower()
        print("Puedes salir con permiso de tus padres." if permiso_padres == 's' else "No puedes salir sin permiso de tus padres.")

    elif 18 <= edad < 65:
        print("Eres un adulto.")
        entrada_parque = input("¿Tienes algún descuento especial (estudiante/trabajador)? (s/n): ").lower()
        print("Puedes obtener un descuento en la entrada del parque." if entrada_parque == 's' else "Debes pagar la entrada regular para el parque de diversiones.")

    else:
        print("Eres un adulto mayor.")
        print("Tienes derecho a un descuento especial en todas las entradas y servicios.")

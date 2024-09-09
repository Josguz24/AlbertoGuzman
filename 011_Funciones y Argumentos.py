# Variable global
mensaje_global = "Hola desde la variable global"

# Función que usa *args (argumentos arbitrarios)
def suma_numeros(*args):
    return sum(args)

# Función que usa **kwargs (diccionarios arbitrarios)
def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Función con variables locales, globales y función anidada
def funcion_externa():
    mensaje_local = "Hola desde la variable local"

    def funcion_interna():
        # Usamos la variable global y local
        print(mensaje_global)
        print(mensaje_local)

    funcion_interna()

# Función lambda para multiplicar dos números
multiplicar = lambda x, y: x * y

# Llamadas de prueba
print(f"Suma de los números: {suma_numeros(1, 2, 3, 4)}")
mostrar_informacion(nombre="Ana", edad=25, ciudad="Madrid")
funcion_externa()
print(f"Resultado de multiplicación: {multiplicar(5, 6)}")

# Ejemplo de manejo de excepciones
def dividir_numeros(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except TypeError:
        print("Error: Los valores deben ser números.")
    else:
        print(f"El resultado de {a} dividido entre {b} es: {resultado}")
    finally:
        print("Fin del cálculo.")

# Pruebas de la función
dividir_numeros(10, 2)
dividir_numeros(10, 0)
dividir_numeros(10, "cinco")

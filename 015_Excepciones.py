# Ejemplo de manejo de excepciones
def dividir_numeros(a, b):
    try:
        resultado = a / b
        #EN CASO DE PRESENTAR UN ERROR EJECUTAR CUALQUIERA DE LOS EXCEPT
    except ZeroDivisionError:
         #SI SE DIVIDE ENTRE 0
        print("Error: No se puede dividir entre cero.")
    except TypeError:
        #SI SE DIVIDE ENTRE LETRAS U OTRO
        print("Error: Los valores deben ser números.")
    else:
        #MOSTRAR EL RESULTADO
        print(f"El resultado de {a} dividido entre {b} es: {resultado}")
    finally:
        # SE IMPRIME SI O SI
        print("Fin del cálculo.")

# Pruebas de la función
dividir_numeros(10, 2)
dividir_numeros(10, 0)
dividir_numeros(10, "cinco")

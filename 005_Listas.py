colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]  # Lista inicial de colores
newlist = ['uno', 'dos']  # Otra lista inicial para manipulaciones

# Menú principal
opc = int(input("MENU\n"
                "Selecciona el número de tu opción preferida\n"
                "1) Buscar un color\n"
                "2) Agregar/Eliminar elemento en nueva lista\n"))

# Opción 1: Operaciones con la lista 'colores'
if opc == 1:
    bucle = 1  # Controla el ciclo de repetición de la sección
    while bucle == 1:
        # Submenú para diferentes opciones con la lista de colores
        elegir = int(input('Seleccione una opción\n'
                           '1) Buscar por Color\n'
                           '2) Buscar por Posición\n'
                           '3) Eliminar con REMOVE\n'
                           '4) Eliminar con POP\n'
                           '5) Ordenar colores con SORT\n'
                           '6) Mostrar cantidad de colores con LEN\n'))

        if elegir == 1:  # Buscar un color por su nombre
            buscar = input('Ingrese el nombre del color\n')
            if buscar in colores:  # Verificamos si el color está en la lista
                print(f'El color está en la posición {colores.index(buscar)}')
            else:
                print('El color no existe en la lista')

        elif elegir == 2:  # Buscar un color por su posición en la lista
            buscar = int(input('Ingrese el número de la posición\n'))
            if -len(colores) <= buscar < len(colores):  # Verificamos si la posición está en rango
                print(f'En la posición {buscar} se encuentra el color {colores[buscar]}')
            else:
                print('Fuera de rango')

        elif elegir == 3:  # Eliminar un color por su nombre con REMOVE
            buscar = input('Selecciona el color a eliminar\n')
            if buscar in colores:  # Solo lo eliminamos si el color está en la lista
                colores.remove(buscar)
                print(f'El color {buscar} ha sido eliminado. La lista se ve así: {colores}')
            else:
                print('El color no existe en la lista')

        elif elegir == 4:  # Eliminar un color por su posición con POP
            buscar = int(input('Ingrese la posición a eliminar con POP\n'))
            if -len(colores) <= buscar < len(colores):  # Verificamos si la posición está en rango
                eliminado = colores.pop(buscar)  # Eliminamos y guardamos el color eliminado
                print(f'El color {eliminado} ha sido eliminado con pop(). La lista se ve así: {colores}')
            else:
                print('Fuera de rango')

        elif elegir == 5:  # Ordenar la lista de colores
            colores.sort()
            print(f'La lista de colores ha sido ordenada: {colores}')

        elif elegir == 6:  # Mostrar la cantidad de colores en la lista
            print(f'La lista tiene {len(colores)} colores.')

        else:
            print('Opción no válida')

        bucle = int(input(f'Ingresa el número 1 para continuar o 0 para salir: '))  # Controla si se repite el ciclo

# Opción 2: Operaciones con la lista 'newlist'
elif opc == 2:
    bucle = 1  # Controla el ciclo de repetición de la sección
    while bucle == 1:
        # Submenú para diferentes operaciones con la lista newlist
        opc = int(input("Qué desea hacer:\n"
                        "1) Agregar número con APPEND\n"
                        "2) Agregar palabra con APPEND\n"
                        "3) Insertar elemento con INSERT\n"
                        "4) Borrar elemento con DEL\n"
                        "5) Ordenar lista con SORT\n"
                        "6) Mostrar cantidad de elementos con LEN\n"))
        
        if opc == 1:  # Agregar un número a la lista con APPEND
            numero = int(input('Ingrese el número a agregar: \n'))
            newlist.append(numero)  # Añadimos el número al final de la lista
            print(f'Número añadido. La lista se ve así: {newlist}')

        elif opc == 2:  # Agregar una palabra a la lista con APPEND
            palabra = input('Ingrese la palabra a agregar \n')
            newlist.append(palabra)  # Añadimos la palabra al final de la lista
            print(f'Palabra añadida. La lista se ve así: {newlist}')

        elif opc == 3:  # Insertar un elemento en una posición específica con INSERT
            posicion = int(input('Ingrese la posición donde quiere insertar: \n'))
            elemento = input('Ingrese el elemento a insertar: \n')
            if 0 <= posicion <= len(newlist):  # Verificamos que la posición esté en rango
                newlist.insert(posicion, elemento)
                print(f'Elemento "{elemento}" insertado en la posición {posicion}. La lista se ve así: {newlist}')
            else:
                print('Posición fuera de rango')

        elif opc == 4:  # Eliminar un elemento por posición con DEL
            eliminar = int(input('Ingrese posición a eliminar con DEL\n'))
            if 0 <= eliminar < len(newlist):  # Verificamos que la posición esté en rango
                del newlist[eliminar]  # Eliminamos el elemento de la lista
                print(f'Elemento eliminado. La lista se ve así: {newlist}')
            else:
                print('Posición fuera de rango')

        elif opc == 5:  # Ordenar la lista con SORT
            newlist.sort()  # Ordenamos la lista
            print(f'La lista ha sido ordenada: {newlist}')

        elif opc == 6:  # Mostrar la cantidad de elementos en la lista con LEN
            print(f'La lista tiene {len(newlist)} elementos.')

        else:
            print('Opción no válida')

        bucle = int(input(f'Ingresa el número 1 para continuar o 0 para salir: '))  # Controla si se repite el ciclo

# Definición de clase básica
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Clase que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)  # Llamamos a __init__ de Persona
        self.puesto = puesto

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Puesto: {self.puesto}")

# Clase vacía usando pass
class TemporalEmpleado(Empleado):
    pass

# Crear instancias de Persona y Empleado
persona1 = Persona("Carlos", 45)
empleado1 = Empleado("Ana", 30, "Desarrolladora")

# Llamadas de prueba
persona1.mostrar_informacion()
empleado1.mostrar_informacion()

# Eliminar un objeto
del empleado1

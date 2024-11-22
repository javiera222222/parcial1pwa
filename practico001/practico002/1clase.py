# 1.- Clase Persona:
# Crear una clase llamada `Persona` que tenga los atributos
# `nombre` y `edad`. Además, debe tener un método `saludar` que
# imprima un saludo incluyendo el nombre de la persona.

class Persona(object):
    def __init__(self,nombre,edad):
        self.nombre =nombre
        self.edad =edad
    def saludar(self):
            print(f"Hola, mi nombre es  {self.nombre} y tengo {self.edad} años")



    
    


# Prueba la clase
persona1 = Persona("Juan", 25)
persona1.saludar()
# Salida:
# Hola, mi nombre es Juan y tengo 25 a os.
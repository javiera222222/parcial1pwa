# 1.- Decorador Simple para Mostrar Mensajes:
# Crear un decorador con el nombre “decorador_mensaje” que
# imprima un mensaje antes y después de la ejecución de la función
# decorada.
# Crear una función con el nombre “funcion_principal” que
# imprima en pantalla el texto: “Esta es la función principal”.
# Decorar esta funcion con el decorador y luego ejecutarla.

def decorador_mensaje(funcion_principal):
    def wrapper():
        print("Inicio de la funcion")
        funcion_principal()
        print("Fin de la funcion")
    return wrapper

@decorador_mensaje
def funcion_principal():
    print("Esta es la funcion principal") 
 

# Prueba la funcion decorada
funcion_principal()
# Salida
# Inicio de la funcion.
# Esta es la funcion principal.
# Fin de la funcion.
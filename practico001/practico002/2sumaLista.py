# 2.- Sumatoria de Lista:
# Crear un script de python que contenga una función con el
# nombre “sumar_lista”, reciba como único parámetros una lista de
# números y retorne la sumatoria de todos los números de la lista.


def sumar_lista(lista):
    suma =0
    for numero in lista:
        suma= suma+numero
    return suma    

# Prueba la funcion
print(sumar_lista([3, 1, 4, 1, 5, 9, 2, 6, 5])) # Salida: 36
print(sumar_lista([5, 9])) # Salida: 14

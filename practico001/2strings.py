# 2.- Strings:
#  Crear un script de python que contenga una variable mi_nombre 
# y asignarle tu nombre como string. Luego mostrar el tipo de datos 
# de la variable.
#  Intentar acceder a la primera y última letra de mi_nombre 
# utilizando índices y mostrándolos en pantalla.
#  Utilizar la función len() para calcular la longitud de 
# mi_nombre y mostrarlo.
#  Imprimir en pantalla el contenido de la variable mi_nombre, 
# todo en mayusculas y todo en minúsculas

mi_nombre="javiera"
print(type(mi_nombre))
print(mi_nombre[0])
print(mi_nombre[6])
print(len(mi_nombre))
nombre_upper=mi_nombre.upper()
print(nombre_upper)
nombre_lower=mi_nombre.lower()
print(nombre_lower)
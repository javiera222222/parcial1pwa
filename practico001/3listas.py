#  3.- Listas:
#  Crear un script con una lista mi_lista que contenga tres tipos
#  diferentes de datos.
#  Agregar un nuevo elemento al final de la lista con el método 
# append().
#  Cambiar el valor del primer elemento de la lista.
#  Eliminar el último elemento de la lista con el método pop().
#  Mostrar en pantalla el contenido de la lista.

mi_lista=[1,"hola",True]
mi_lista.append("chau")
mi_lista[0]=2
mi_lista.pop(3)
print(mi_lista)
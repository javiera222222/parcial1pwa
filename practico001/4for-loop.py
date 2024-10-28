#  4.- For loops:
#  a. Escribir un programa que muestre los números del 1 al 10
#  utilizando un bucle for.
#  b. Escribir un programa que muestre la suma de los números del
#  1 al 100
numeros=[1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(numero, "\n")

suma=0
for i in range(1,101):
   
    suma=suma+i
print(suma)
#  3.- If-elif-else statements:
#  Escribir un programa que le solicite al usuario ingresar una
#  calificación del 0 al 100, la asigne a una variable y muestre la
#  calificación alfabética correspondiente (A, B, C, D, F) según el
#  numero ingresado. Correspondiendo cada letra con valores de 20 en
#  20. Es decir: 0 a 19 = A, de 20 a 39 = B, etc

calificacion=int(input("escribi una calificacion del 0 al 100"))
if calificacion<=20:
    letra="A"
    print(letra)
elif calificacion>20 and calificacion<=40:
    letra="B"
    print(letra)
elif calificacion>40 and calificacion<=60:
    letra="C"
    print(letra)
elif calificacion>60 and calificacion<=80:
    letra="D"
    print(letra)
elif calificacion>80 and calificacion<=100:
    letra="F"
    print(letra)
elif calificacion<0 or calificacion>100:
    print("valor no aceptado")
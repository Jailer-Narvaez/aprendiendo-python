#python tiene 3 tipos de datos numéricos
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#verificando el tipo de dato
print(type(x))
print(type(y))
print(type(z))

#los numeros flotantes tambien se pueden declarar con e en potencias de 10
x = 10e4
print(x)

#conversion de tipos
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convirtiendo a float
a = float(x)

#convirtiendo a entero
b = int(y)

#convirtiendo a complejo:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#NO SE PUEDEN CONVERTIR NUMEROS COMPLEJOS A OTROS TIPOS DE NUMEROS


#numeros aleatorios
import random

x = random.randrange(1,10)

print(x)
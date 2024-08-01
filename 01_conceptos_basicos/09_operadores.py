#los operadores se usan para realizar operaciones sobre variables o valores puros
print(10 + 5)

#operadores aritmeticos
print(1 + 1) #suma
print(1 - 1) #resta
print(1 * 1) #multiplicacion
print(1 / 1) #division
print(1 % 1) #modulo
print(1 // 1) #división sin decimales
print(1 ** 2) #exponenciación

#operadores de asignación

x = 5
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x //= 3
print(x)
x **= 3
print(x)


#operadores de igualdad
x = 10
y = 20

print(x == y) #igual
print(x != y) #distinto
print(x > y) #mayor que
print(x < y) #menor que
print(x >= y) #mayor o igual
print(x <= y) #menor o igual

#operadores logicos
x < 5 and  x < 10
x < 5 or x < 4
not(x < 5 and x < 10)

#operadores de identidad
x is y
x is not y

#operadores de pertenencia
x in y
x not in y

#operadores bit a bit
x & y
x | y
x ^ y
~x
x << 2
x >> 2

#precedencia de los operadores
print((6 + 3) - (6 + 3)) #los parentesis se operan primero
print(100 + 5 * 3) #la multiplicacion se opera primero que la suma
print(5 + 4 - 7 + 3) #las sumas y restas tienen la misma precedencia, en este caso el código se opera de izquierda a derecha


#variables de python
x = 5
y = "Hola mundo"

print(y * x)

x = "Nuevo valor"
print(x)


#Conversión (se puede declarar el tipo de la variable con conversión)
x = str(3) #variable de tipo string
y = int(5) #variable de tipo entero
z = float(2.3) #variable de coma flotante

#Se pueden concocer los tipos de variables con la función type
print(type(x))
print(type(y))
print(type(z))


#nombres de variables (pueden seguir cualquiera de las siguientes reglas)
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#nombres de variables de varias palabras
#Carmel case
myVariableName = "John"

#Pascal Case
MyVariableName = "John"

#snake case
my_variable_name = "John"


#asignación de multiples valores en una sola linea
x, y, z = "Mundo", "Naranja", 3

print(x)
print(y)
print(z)

#un valor para multiples variables
x = y = z = "Naranja"
print(x)
print(y)
print(z)

#descomprimir una lista
numeros = [1,2,3]
x, y, z = numeros
print(x)
print(y)
print(z)

#variables de salida multiples
print(x, y, z)

#variables globales
x = "Global"

def mi_funcion():
    print(x) #Las variables declaradas dentro de la función son locales y solo se pueden operar dentro y obetener al llamar la función

mi_funcion()

print("La variable permanece como esta fuera de la función, por eso es: ", x)

#cambiando el valor de la variable global desde un ambito local
def variable_local_global():
    global x
    x = 16

variable_local_global()

print("Cambiando el valor de la variable global desde la función, ahora vale: ", x)
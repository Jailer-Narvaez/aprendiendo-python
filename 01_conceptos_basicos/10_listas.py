#las listas se utilizan para almacenar varios valores en una sola variable
mi_lista = ["banana", "manzana", "pera"]
print(mi_lista)

#los elementos de una lista estan ordenados, son modificables y permiten valores duplicados
mi_lista = ["banana", "manzana", "pera", "banana"]
#los elementos de una lista estan ordenados por indices [0,1,2,3,4] iniciando su ordenamiento desde el número 0, cada indice representa una posición en la lista
print(mi_lista[1])
#al estar ordenados los elementos de la lista este orden no se puede cambiar

#longitud de la lista
print(len(mi_lista))

#tipos de datos
list1 = ["abc", 34, True, 40, "male"]
#una lista puede contener diferentes tipos de datos

#el constructor list
mi_lista = list(("banana", "manzana", "pera"))

print(mi_lista)

#consultando un elemento de la lista
print(mi_lista[0])

#indexación negativa (acceder a la lista de derecha a izquierda)
print(mi_lista[-2])

#accediendo a un rango de indices
print(mi_lista[1:4])

#si omitimos el valor inicial se iniciara desde el primer indice
print(mi_lista[:4])

#si omitimos el valor final se iniciara en el indice indicado y accedera hasta el final
print(mi_lista[2:])

#rango con indices negativos
print(mi_lista[-4:-1])

#busqueda dentro de una lista
if "manzana" in mi_lista:
    print("Valor encontrado")
else: 
    print("Valor no encontrado")

#cambiar elementos de una lista
mi_lista[1] = "piña"

print(mi_lista)

#cambiar un rango de valores en la lista
mi_lista[2:3] = "valor 1", "valor 2"

print(mi_lista)

#insertar elementos de la lista
mi_lista.insert(2,"sandia") #inserta el valor como tercer elemento

print(mi_lista) #insertar elementos aumenta la longitud de la lista

#eliminar elementos especifico de la lista
mi_lista.remove("sandia")
print(mi_lista)

#eliminando un indice de la lista
mi_lista.pop(1)
print(mi_lista)

#la palabra clave del
del mi_lista[0]
print(mi_lista)

#eliminando toda la lista
del mi_lista
#print(mi_lista) (error)

#limpiando la lista
mi_lista = ["banana", "manzana", "pera"]
mi_lista.clear()

print(mi_lista)


#recorrer lista con un bucle
mi_lista = ["banana", "manzana", "pera"]

for i in mi_lista:
    print(i)

#recorriendo los indices de la lista
for i in range(len(mi_lista)):
    print(i)

#recorriendo la lista con un while
i = 0
while i< len(mi_lista):
    print(mi_lista[i])
    i += 1

#recorriendo la lista con un blucle corto
[print(i) for i in mi_lista] #solo funciona con los corchetes

#creando listas a partir de otras listas
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#en una sola linea de código
newlist = [x for x in fruits if "a" in x] #la lista se crea a partir de condiciones verdaderas
print(newlist)

newlist = [x for x in fruits if x not in "banana"]
print(newlist)


newlist = [i for i in fruits] #sin condicionales
print(newlist)

numeros = [i for i in range(10)]
print(numeros)

numeros = [i for i in range(10) if i < 5]
print(numeros)

#manipulando los elementos antes de finalizar la iteración
fruits = [i.upper() for i in fruits]
print(fruits)

#cambiando todos los elementos de la lista con un valor
fruits = ["Hola" for i in fruits]
print(fruits)

fruits = [x if x != "Hola" else "Banana" for x in fruits]
print(fruits)

#ordenamiento de listas alfanumericamente
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#en orden descendente
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

#personalizar la función
def mi_funcion(n):
    return abs(n-23)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = mi_funcion) #ordena poniendo en primer lugar el valor pasado en la función
print(thislist)

#ordenamiento sin tener en cuenta mayusculas
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


#ordenamiento inverso
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#copiar listas
thislist = ["apple", "banana", "cherry"]
my_list = thislist.copy()
print(my_list)


#tambien se puede copiar con el meto list
thislist = ["apple", "banana", "cherry"]
my_list = list(thislist)
print(my_list)


#se puede hacer una copia de la lista segmentando
thislist = ["apple", "banana", "cherry"]
my_list = thislist[0:2]
print(my_list)

#uniendo listas
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


#uniendo listas con inserción de datos
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#uniendo listas con un método existente
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)






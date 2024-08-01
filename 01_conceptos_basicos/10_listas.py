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



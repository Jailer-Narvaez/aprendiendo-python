#expresiones verdaderas o falsas
print(10>9)
print(10<9)

#expresiones verdaderas o falsas en el if
a = 200
b = 33


if b>a:
    #se ejecuta si la condición es verdadera
    print("La condición es verdaderas")
else:
    #se ejecuta si la condición es falsa
    print("La condición es falsa")

#evaluar valores y variables
print(bool("Hola"))
print(bool(15))
print(bool(0))

#CUALQUIER VALOR VACIO O 0 RESULTA FALSO, CUALQUIER VALOR POR SI SOLO ES TRUE

#expresiones falsas
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


#las funciones pueden devolver un valor booleano
def mi_funcion():
    return False

print(mi_funcion())


#se puede ejecutar código a partir del valor booleano reportado por una función

if mi_funcion():
    print("La función retorno verdadero")
else:
    print("La función retorno falso")


#python tiene funciones integradas que retornan valores booleanos verdaderos o falsos
x = 200

print(isinstance(x,int)) #pregunta si la variable contiene un valor entero


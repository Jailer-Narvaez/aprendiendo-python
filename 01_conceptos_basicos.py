#Hola mundo
print("Hola mundo")

#tipos de datos
print(type("Hello"))
print(type(32))
print(type(32.1))
print(type(True))
print(type(False))

#operadores aritmeticos
print(1+1) #suma
print(2-1) #resta
print(1*2) #multiplicacion
print(16/8) #division
print(16//8) #division sin decimales
print(16%4) #resto

#operadores de comparacion
print("h" == "h") #igualdad
print(1>2) #mayor que
print(2<3) #menor que
print(1>=1) #mayor o igual que
print(1<=1) #menor o igual que
print(2!=2) #diferente de 
print(not False) #negacion

#variables
numero1 = 1
print(numero1)
texto = "Hola mundo"
print("Hola mundo solitario")
nombre = "Jailer"
saludo = "Hola " + nombre
print(saludo)

#funciones
def saludar():
    print("Hola, bienvenido")

saludar()

#funcion con argumentos
def suma(num1, num2):
    print("El resultado de la suma es: ",num1 + num2)

suma(1,3)

#funcion con argumentos por defecto
def resta(num1 = 16, num2 = 15):
    print("El resultado de la resta es: ", num1 - num2)

resta() #si no se asigna un argumento la función toma los valores por defecto asignados

#funcion que retorna un valor
def testeando():
    return "Testeo exitoso"

print(testeando())

#funciones con variables locales
def multiplicacion():
    num1 = 1
    num2 = 3
    return num1 * num2

print(multiplicacion())

#funciones con variables globales
numero2 = 4
numero3 = 16

def division():
    global numero2 
    global numero3

    return numero3 // numero2

print(division())


#estructuras de datos
#Condicionales if

condicion = "HOLA"

if(condicion == True):
    print("La variable es verdadera")
elif(condicion == False):
    print("La variable es falsa")
else:
    print("La variable no es verdadera ni falsa")


#sentencia for
lista = ["Tomate", "Cebolla", "Banana", "Leche"]

for item in lista:
        print(item)


#bucle while
condicion = 0

while condicion <= 10:
    print(condicion)
    condicion += 1


import random

def nivel_facil():

    vidas = 9
    print("El numero aleatorio esta entre 1 y 10, tienes ", vidas, " oportunidades")
    numero_aleatorio = random.randint(1,10)

    while True:
               
        if(vidas == 0):
                print("No lograste adivinar el numero aleatorio")
                break
        else:
            respuesta = int(input("Ingresa un número "))
            if(numero_aleatorio == respuesta):
                print("Acertaste el número aleatorio")
                break
            elif(numero_aleatorio < respuesta):
                print("El numero aleatorio es menor que el ingresado")
                vidas -= 1
                print("Te quedan ", vidas," oportunidades")
            elif(numero_aleatorio > respuesta):
                print("El numero aleatorio es mayor que el numero ingresado")
                vidas -= 1
                print("Te quedan ", vidas," oportunidades")
            else:
                print("No ingresaste un número")

def nivel_medio():

    vidas = 6
    print("El numero aleatorio esta entre 1 y 10, tienes ", vidas, " oportunidades")
    numero_aleatorio = random.randint(1,10)

    while True:
               
        if(vidas == 0):
                print("No lograste adivinar el numero aleatorio")
                break
        else:
            respuesta = int(input("Ingresa un número "))
            if(numero_aleatorio == respuesta):
                print("Acertaste el número aleatorio")
                break
            elif(numero_aleatorio < respuesta):
                print("El numero aleatorio es menor que el ingresado")
                vidas -= 1
                print("Te quedan ", vidas," oportunidades")
            elif(numero_aleatorio > respuesta):
                print("El numero aleatorio es mayor que el numero ingresado")
                vidas -= 1
                print("Te quedan ", vidas," oportunidades")
            else:
                print("No ingresaste un número")

def nivel_dificil():

    vidas = 3
    print("El numero aleatorio esta entre 1 y 10, tienes ", vidas, " oportunidades")
    numero_aleatorio = random.randint(1,10)

    while True:
               
        if(vidas == 0):
                print("No lograste adivinar el numero aleatorio")
                break
        else:
            respuesta = int(input("Ingresa un número "))
            if(numero_aleatorio == respuesta):
                print("Acertaste el número aleatorio")
                break
            elif(numero_aleatorio < respuesta):
                print("El numero aleatorio es menor que el ingresado")
                vidas -= 1
                print("Te quedan ", vidas," oportunidades")
            elif(numero_aleatorio > respuesta):
                print("El numero aleatorio es mayor que el numero ingresado")
                vidas -= 1
                print("Te quedan ", vidas," oportunidades")
            else:
                print("No ingresaste un número")
    


def juego():
    print("Bienvenido, tienes varias oportunidades para encontrar un número aleatorio")
    inicio = input("¿Quieres jugar? ").lower()

    if(inicio == "si"):
        print("¡Empecemos!")
        respuesta = int(input("1. Facil, 2. Medio, 3. Dificil "))

        if(respuesta == 1):
            nivel_facil()
        elif(respuesta == 2):
            nivel_medio()
        elif(respuesta == 3):
            nivel_dificil()
    else:
        print("¡Regresa cuando quieras!")


juego()
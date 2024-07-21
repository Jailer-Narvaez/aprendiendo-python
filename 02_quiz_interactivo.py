#Un programa que hace 3 preguntas sobre computación

print("Bienvenido al quiz de informatica interactivo")


def juego():
        print("¡Empecemos!")
        puntaje = 0
        total_preguntas = 3

        pregunta1 = input("¿que significan las siglas CPU? ").lower()

        if(pregunta1 == "central processing unit"):
            print("¡Correcto!")
            puntaje += 1
        else:
            print("¡Incorrecto!")

        pregunta2 = input("¿Que significan las siglas RAM? ")

        if(pregunta2 == "ramdom acces memory"):
            print("¡Correcto!")
            puntaje += 1
        else:
            print("¡Incorrecto!")

        pregunta3 = input("¿Que significan las siglas GPU? ")

        if(pregunta3 == "graphic processing unit"):
            print("¡Correcto!")
            puntaje += 1
        else:
            print("¡Incorrecto!")

        print("El total de preguntas realizadas fue: ",total_preguntas)
        print("Acertaste ", puntaje, " preguntas")
        porcentaje_de_acertadas = round(puntaje / total_preguntas * 100)
        print("El porcentaje de preguntas correctas fue: ", porcentaje_de_acertadas)

        if(porcentaje_de_acertadas >= 80):
            print("Quiz contestado con exito")
        else:
            print("Haz perdido, vuelve a intentarlo")



inicio = input("¿Quieres jugar? ").lower()

if(inicio == "si"):
    while True:
        juego()
        jugar_de_nuevo = input("¿Quieres intentarlo de nuevo? ").lower()

        if(jugar_de_nuevo == "no"):
            print("¡Gracias por jugar!¡")
            break
else:
    print("Buelve cuando quieras")
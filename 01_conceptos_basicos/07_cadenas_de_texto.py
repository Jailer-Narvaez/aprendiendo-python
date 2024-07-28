#las cadenas de texto se pueden ingresar con los dos tipos de comillas
print("Hola mundo")
print('Hola mundo')

#caracteres de escape
print("Hola 'Mundo'") #las comillas internas no deben ser iguales a las externas

#asignación de un string a una variable
a = "Hola"
print(a)

#cadena de texto de varias lineas
a = """
Esto es un string
    que se imprime 
        en varias lienas
            de código
"""

#EL RESULTADO SE IMPRIME TAL CUAL LO PONEMOS DENTRO DEL CÓDIGO
print(a)

a = "Hola mundo"

print(a[0]) #accediendo a la primera letra del string

#recorriendo un string
for x in "Mi lista":
    print(x)

#longitud de la cadena de caracteres
a = "Hola mundo"
print(len(a)) #Longitud de la cadena

#buscando una palabra clave dentro de la cadena

a = "Hola Mundo"
print("Mundo" in a) #arroja un valor de tipo bool

if "Mundo" in a:
    print("Si esta dentro de la cadena")


#comprobando que no este dentro de la cadena
print("Mundo" not in a) #resultado de tipo bool


if "Mundo" not in a:
    print("Si esta dentro de la cadena")

else: 
    print("La cadena si esta en el string")

#segmentando la cadena
a = "Hola mundo moderno"

print(a[5:10])

#segmentando desde el principio
print(a[:5])

#segmentando hasta el final
print(a[5:])


#indexación negativa
print(a[-5:-2]) #Inicia la indexación de derecha a izquierda


#modificando cadenas 

a = " hola Mundo Moderno "

print(a.upper()) #mayusculas

print(a.lower()) #minusculas

print(a.strip()) #quita espacios al principio o al final de la cadena

print(a.replace("M", "i")) #remplaza el valor indicado a la izquierda por el indicado a la derecha

print(a.split(" ")) #separa la cadena cuando encuentre el valor indicado, lo retorna en una lista

#concatenación de cadenas
a = "Hola "
b = "Mundo"

print(a+b) #los une

#formato de cadenas
edad = 24
texto = f"Mi nombre es Jailer y mi edad es: {edad}" #manera correcto de mezclar numeros con cadenas de texto
print(texto)

precio = 59.99
texto = f"El precio del producto seleccionado es: {precio:.2f}"
print(texto)

texto = f"El resultado de la multiplicación es: {1 * 5}"
print(texto)


#caracteres de escape
print("Hola mundo ultra \"moderno\"") #todo lo que esta ubicado luego de la barra invertida sera procesado en el print
#Ejercicio de contar la cantidad de palabras escritas por parte del usuario.

cadena = input("¿En qué estás pensando? ")
separador = " "
lista = cadena.split(separador) #split se usa para delimitar cada palabra y agregar a una lista.
conteo = len(lista)

print("Tu pensamiento está escrito en ",conteo," palabras.")
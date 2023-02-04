#El usuario va adivinar un número generado por la pc en un rango especifico 
#y se le indicará si es mayor, menor o igual al generado.

import random

def adivina_num(x):
    print("=========================")
    print("¡Bienvenido(a) al juego!")
    print("=========================")
    print("Debes adivinar el número generado por la pc.")

    num_aleatorio = random.randint(1,x) #Num aleatorio entre 1 y x

    prediccion = 0

    while prediccion != num_aleatorio:
        prediccion = int(input(f"Adivina el número entre 1 y {x}: "))

        if prediccion < num_aleatorio:
            print("El número es muy pequeño. Intenta de nuevo.")
        elif prediccion > num_aleatorio:
            print("El número es muy grande. Intenta de nuevo.")
    
    print(f"¡Felicitaciones! Adivinaste el número {num_aleatorio} correctamente.")


adivina_num(10)
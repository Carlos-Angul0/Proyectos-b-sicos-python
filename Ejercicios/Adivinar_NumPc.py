#El usuario va a seleccionar un número en un rango específico y la pc deberá adivinar. 
#El usuario le indicará si es mayor, menor o igual al generado.

import random

def adivina_num_pc(x):
    print("=========================")
    print("¡Bienvenido(a) al juego!")
    print("=========================")

    lim_inferior = 1
    lim_superior = x

    respuesta_usuario = ""

    if lim_inferior == lim_superior:
        print("No hay números suficientes en el rango")
    else:
        print(f"Selecciona un número entre 1 y {x} para que el PC intente adivinar.\n")
        
        while respuesta_usuario != "c":
            #Generar predicción
            try:
                if lim_inferior != lim_superior:
                    prediccion = random.randint(lim_inferior, lim_superior)
                else:
                    prediccion = lim_inferior #También puede ser lim_superior
            except: 
                print("¡Perdiste! No hay más números en el rango :(")
                break
            
            #Respuesta del usuario
            respuesta_usuario = input(f"Mi predicción es {prediccion}. Si es muy alta, digita (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C) --> ").lower()

            if respuesta_usuario == "a":
                lim_superior = prediccion - 1
            elif respuesta_usuario == "b":
                lim_inferior = prediccion + 1
            else:
                print(f"¡Yes! La computadora adivinó tu número {prediccion} correctamente.")


adivina_num_pc(3)
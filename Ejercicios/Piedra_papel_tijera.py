import random

def play ():
    user = int(input("Escoja la opción:\n 1 para Piedra, 2 para Papel o 3 para Tijera --> "))
    pc = random.choice([1,2,3])

    while (user<1 or user>3):
        print(f'{user} no se encuentra en las opciones, por favor digita una opción válida.')

        user = int(input("Escoja la opción:\n 1 para Piedra, 2 para Papel o 3 para Tijera --> "))
        pc = random.choice([1,2,3])


    print(f'Escogiste la opción {user} y la computadora la opción {pc}\n')

    if user == pc:
        return '¡Empate!'

    if gana_user(user, pc):
        return '¡Ganaste!'

    return '¡Perdiste!'


def gana_user(user,pc):
    if ((user == 1 and pc == 3)
        or (user == 2 and pc == 1)
            or (user == 3 and pc == 2)):
        return True
    else:
        return False


print(play())
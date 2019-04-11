import random

arr1 = [2, 5, 43, 6, 76, 100, 4, 43, 3,]

# print(arr1[-2])
# print(arr1[-3:-1])
# print(arr1[-2], arr1[-3])
# print(arr1[::-1])

# for i in range(len(arr1)):
#     if i % 2 == 0:
#         print(arr1[i])
#
# print('-'*10)
#
# for i in range(0, len(arr1), 2):
#     print(arr1[i])
#
# print('-'*10)
#
# for i, num in enumerate(arr1):
#      if i % 2 == 0:
#          print(num)
#
# #print(arr1[::2])
#
# #print(arr1[::-2])
#
# frase = 'Gloria al bravo pueblo que el yugo lanzo'
#
# #print(frase[::-1])
#
# words = frase.split()
#print(words[::-1])

#words[0] = words[0].lower()
#words[-1] = words[-1].capitalize()
# print(words)
#
# print(' '.join(words[::-1]).capitalize())
#
# letra = ''
# #letra = input('Escribe una letra: ')
#
# count = 0
#
# for letter in frase:
#     if letter == letra:
#         count = count + 1
#
# count = 0
# for word in words:
#     result = word.find(letra)
#     if result != -1:
#         count = count + 1

#print(count)

#print(frase.split(letra))

#print(len(frase.split(letra)) - 1)

#print(words[0].lower())

# if letra in frase:
#     print(letra + ' esta en la frase')

#homework
#bonus, cuantos intentos para que no gane siempre

def dificultad(nivel):

    if nivel == '0':
        print('Tendras 8 intentos para adivinar un numero entre 0 y 300')
        return 8, 300
    elif nivel == '1':
        print('Tendras 5 intentos para adivinar un numero entre 0 y 600')
        return 5, 600
    elif nivel == '2':
        print('Tendras 2 intentos para adivinar un numero entre 0 y 1000')
        return 2, 1000
    else:
        print('Input no valido')
        return 0


def isInt(string):
    """
    check whether the input can be transformed into an integer
    """
    try:
        int(string)
    except ValueError:
        return False

    return True


def adivinar():

    nivel = input('Escoja el nivel de dificultad, siendo 0 facil, 1 medio y 2 dificil: ')

    nivel_dif, max_num = dificultad(nivel)

    num_random = random.randint(0, max_num)

    count = 0

    while count < nivel_dif:
        num_usuario = (input('Ingrese un numero: '))
        if isInt(num_usuario):
            num_usuario = int(num_usuario)
        else:
            print('El input debe ser un numero')
            continue

        if num_usuario < 0 or num_usuario > max_num:
            print('Este numero no esta en el rango!')
            continue

        if num_usuario == num_random:
            print('Adivinaste!')
            break
        elif num_usuario < num_random:
            print('Intenta con numeros mas altos')
        else:
            print('Intenta con numeros mas bajos')

        count = count + 1

        if count == (nivel_dif - 1):
            print('Ultima oportunidad')

    print('El numero era: ' + str(num_random))
    print('')


adivinar()

adivinar()

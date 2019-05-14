"""
Ejercicios de la clase de Programacion Orientada a Objectos
"""
import random

#Abstraccion
class Celular:
    def __init__(self, m, mo, so, alm, r, p):
        self.marca = m
        self.modelo = mo
        self.so = so
        self.almacenamiento = alm
        self.ram = r
        self.pantalla = p

    def marca_modelo(self):
        print(self.marca + ' ' + self.modelo)

    def especificaciones(self):
        print('Sistema Operativo: ' + self.so)
        print('Alcacenamiento: ' + self.almacenamiento)
        print('RAM: ' + self.ram)
        print('Pantalla: ' + self.pantalla)

    def chatear(self, app):
        self.app = app
        print('Abriendo ' + self.app)

    def selfie(self):
        print('Tomar selfie')
        print('* flash *')
        print('(^_^)')


samsung = Celular('Samsung', 'Galaxy J7 Duo', 'Android 8.0', '32GB', '4GB', '5.5"')

samsung.marca_modelo()
samsung.especificaciones()

samsung.chatear('Whatsapp')
samsung.selfie()


#Encapsulamiento
class Banda:
    def __init__(self, n, g, i, a, h):
        self.nombre = n
        self.genero = g
        self.integrantes = i
        self.albums = a
        self.hits = h

    def agregar_albums(self, a):
        self.albums.extend(a)

    def agregar_integrantes(self, i):
        self.integrantes.extend(i)

    def agregar_hits(self, h):
        self.hits.extend(h)


# foo_f = Banda('Foo Fighters', 'Rock', ['Dave Grohl', 'Taylor Hawkins'], ['Concrete and Gold'],
#                 ['The Pretender', 'Everlong', 'Times like these'])
#
# print(foo_f.albums)
#
# foo_f.agregar_albums(['Wasting Light'])
#
# print(foo_f.albums)
#
# INTEGRANTES = ['Pat Smear', 'Nate Mendel', 'Chris Shiflett', 'Rami Jaffee']
#
# foo_f.agregar_integrantes(INTEGRANTES)
#
# print(foo_f.integrantes)


#Principio de Ocultacion
class Cancion:
    def __init__(self, nombre, artista):
        self.__nombre = nombre
        self.__artista = artista

    #getter
    def nombre(self):
        return self.__nombre

    def artista(self):
        return self.__artista

    #setter
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_artista(self, artista):
        self.__artista = artista


# alive = Cancion('Alive', 'Empire of the Sun')
#
# print(alive.nombre())
# print(alive.artista())
#
# alive.set_nombre('Come Alive')
# print(alive.nombre())
# alive.set_artista('Foo Fighters')
# print(alive.artista())


#Polimorfismo
class Mascota(object):
    def __init__(self, nombre):
        self.__nombre = nombre

    def nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def comer(self):
        return 'nom nom nom'

    def dormir(self):
        return 'ZzZzZz'

    def evacuar(self):
        return ''


class Perro(Mascota):
        def __init__(self, nombre):
            super().__init__(nombre)

        def evacuar(self):
            return '*Afuera de la casa*'


class Gato(Mascota):
        def __init__(self, nombre):
            super().__init__(nombre)

        def evacuar(self):
            return '*En la caja de arena*'


class Hamster(Mascota):
        def __init__(self, nombre):
            super().__init__(nombre)

        def evacuar(self):
            return '*En todo el periodico de la cajita*'


class Pez(Mascota):
        def __init__(self, nombre):
            super().__init__(nombre)

        def comer(self):
            return 'glup glup glup'

        def evacuar(self):
            return '???'


# ramon = Perro('Ramon')
# print(ramon.nombre())
# print(ramon.comer())
# print(ramon.dormir())
# print(ramon.evacuar())

#print('')

# blanca = Gato('Blanca')
# print(blanca.nombre())
# print(blanca.comer())
# print(blanca.dormir())
# print(blanca.evacuar())

#print('')

# roberto = Hamster('Roberto')
# print(roberto.nombre())
# print(roberto.comer())
# print(roberto.dormir())
# print(roberto.evacuar())

#print('')

# maria = Pez('Maria')
# print(maria.nombre())
# print(maria.comer())
# print(maria.dormir())
# print(maria.evacuar())


#Herencia
class Persona(object):
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def nombre(self):
        return self.__nombre

    def edad(self):
        return self.__edad

    def ver_dementores(self):
        return 'No puede ver dementores'

    def hacer_hechizo(self, hechizo):
        return 'No puede hacer ' + hechizo


class Mago(Persona):
        def __init__(self, nombre, edad):
            super().__init__(nombre, edad)

        def ver_dementores(self):
            return 'Puede ver dementores'

        def hacer_hechizo(self, hechizo):
            return  r'\(o.o)--- ' + hechizo + '!!! ***'


class Muggle(Persona):
        def __init__(self, nombre, edad):
            super().__init__(nombre, edad)

class Squib(Persona):
        def __init__(self, nombre, edad):
            super().__init__(nombre, edad)

        def ver_dementores(self):
            return 'Puede ver dementores'


# harry = Mago('Harry Potter', 15)
# print(harry.nombre())
# print(harry.ver_dementores())
# print(harry.hacer_hechizo('Expecto Patronum'))
#
# petunia = Muggle('Petunia Dursley', 40)
# print(petunia.nombre())
# print(petunia.ver_dementores())
# print(petunia.hacer_hechizo('Expecto Patronum'))
#
# filch = Squib('Argus Filch', 58)
# print(filch.nombre())
# print(filch.ver_dementores())
# print(filch.hacer_hechizo('Lumos'))

#Recoleccion de Basura
def recoleccion_basura():
    print('Python usa un conteo de referencia simple como recolector de basura.')
    print('Esto quiere decir que al no haber mas referencias a un objeto')
    print('-el numero de referencias es 0-, el objeto puede ser recolectado como basura.')
    print('Para acceder al recolector de basura se usa el modulo gc.')
    print('Este permite desactivar la recoleccion, ajustar la frecuencia de recoleccion')
    print('y colocar diferentes opciones de debugging.')


#recoleccion_basura()


#Modelar partido de tenis


class Jugador():
    def __init__(self, nombre, raquetas):
        self.__nombre = nombre
        self.__raquetas = raquetas

    def nombre(self):
        return self.__nombre

    def raquetas(self):
        return self.__raquetas

    def set_raquetas(self, raquetas):
        self.__raquetas = raquetas

jose = Jugador('Jose', 1)
ramon = Jugador('Ramon', 1)
nata = Jugador('Nata', 3)
#print(isinstance(jose, Jugador))
#print(jose.nombre())

class Cancha():
    def __init__(self, nombre, material, dimensiones='23,77m x 8,23m'):
        self.__nombre = nombre
        self.__material = material
        self.__dimensiones = dimensiones

    def nombre(self):
        return self.__nombre

    def material(self):
        return self.__material

    def dimensiones(self):
        return self.__dimensiones


wimbledon = Cancha('Wimbledon', 'cesped')


def jugar(num1, num2, top):
    """
    Inputs:
    - num1 = Puntaje (numero entero) con que empieza el contador del jugador #1
    - num2 = Puntaje (numero entero) con que empieza el contador del jugador #2
    - top = Puntaje maximo que puden tener
    Outputs:
    - puntaje_jug1 = Puntaje final del jugador #1  (numero entero)
    - puntaje_jug2 = Puntaje final del jugador #2  (numero entero)
    - diff = Diferencia absoluta entre el puntaje del jugador 1 y del 2
    """

    puntaje_jug1 = random.randint(num1, top)
    puntaje_jug2 = random.randint(num2, top)

    diff = abs(puntaje_jug1 - puntaje_jug2)

    return puntaje_jug1, puntaje_jug2, diff


def ganador(resultado, jugador1, jugador2):
    """
    Inputs:
    - resultado = Tupla que contiene el puntaje del jugador #1, el del jugador #2
                    y la diferencia absoluta entre los dos puntajes
    - jugador1 = Nombre del jugador #1
    - jugador2 = Nombre del jugador #2
    Output:
    - Imprime el nombre del jugador ganador
    """

    if resultado[0] > resultado[1]:
        print('Gano ' + jugador1)
    else:
        print('Gano ' + jugador2)


def sonidos_tenis(tipo):
    """
    Input:
    - tipo = Tipo de encuentro de tenis, puede ser juego, set o partido
    Output:
    Imprime sonidos onomatopeyicos de tenis, de acuerdo al tipo de encuentro
    imprime una mayor o menor cantidad de sonidos
    """

    if tipo == 'juego':
        min = 1
        max = 5
    elif tipo == 'set':
        min = 4
        max = 7
    else:
        min = 5
        max = 9

    for i in range(random.randint(min, max)):
        print('pafff')
        print('    paff')
        print('')
        print('pa')
        print('  pafff')
        print('guapash')
    print('')


def check_jugadores(jugador1, jugador2):

    if isinstance(jugador1, Jugador) and isinstance(jugador2, Jugador):
        return True
    else:
        return False


def check_cancha(cancha):

    if isinstance(cancha, Cancha):
        return True
    else:
        return False


def tenis(tipo, jugador1, jugador2, cancha, dif_min=2, pts1=0, pts2=0):
    """
    Inputs:
    - tipo = tipo de encuentro de tenis, puede ser juego, set o partido
    - jugador1 = nombre del jugador #1
    - jugador2 = nombre del jugador #2
    - dif_min = diferencia minima entre los puntajes de los jugadores para
                ganar un encuentro. El default es 2.
    - pts1 = puntaje (numero entero) con que empieza el contador del jugador #1,
            el default es 0
    - pts2 = puntaje (numero entero) con que empieza el contador del jugador #2,
            el default es 0
    Outputs:
    Retorna el resultado del encuentro, en forma de tupla. El resultado nunca queda en
    empate y siempre existe una diferencia de dif_min entre los puntajes
    """

    if tipo == 'juego':
        pts_min = 5
    elif tipo == 'set' or tipo == 'partido':
        pts_min = 6
    else:
        return print('Input no valido, puedes jugar un juego, set o partido de tenis')

    jugadores_validos = check_jugadores(jugador1, jugador2)
    cancha_valida = check_cancha(cancha)

    if not jugadores_validos or not cancha_valida:
        return print('Parece que tus jugadores o la cancha no son validos')


    print('Que empiece el ' + tipo)

    sonidos_tenis(tipo)

    resultado = jugar(pts1, pts2, pts_min)
    jug1, jug2, dif  = resultado[0], resultado[1], resultado[2]
    max_val = max(jug1, jug2)

    while dif < dif_min or max_val < pts_min:
        resultado = jugar(jug1 , jug2, max_val+2)
        jug1, jug2, dif  = resultado[0], resultado[1], resultado[2]
        max_val = max(jug1, jug2)


    print('Fin del ' + tipo)

    ganador(resultado, jugador1.nombre(), jugador2.nombre())

    print('El marcador fue:')
    print(str(resultado[0]) + '-' + str(resultado[1]))

    #return resultado[0], resultado[1]



#tenis('set', jose, ramon, wimbledon)
#tenis('partido', nata, ramon, wimbledon)

#Modelar juego de basquet, objetos y relaciones, no codigo

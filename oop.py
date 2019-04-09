"""
Ejercicios de la clase de Programacion Orientada a Objectos
Prof. Juan
"""


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


# samsung = Celular('Samsung', 'Galaxy J7 Duo', 'Android 8.0', '32GB', '4GB', '5.5"')

#samsung.marca_modelo()
#samsung.especificaciones()

#samsung.chatear('Whatsapp')
#samsung.selfie()


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

# print(foo_f.albums)
#
# foo_f.agregar_album(['Wasting Light'])
#
# print(foo_f.albums)
#
# INTEGRANTES = ['Pat Smear', 'Nate Mendel', 'Chris Shiflett', 'Rami Jaffee']
#
# foo_f.agregar_integrante(INTEGRANTES)
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


recoleccion_basura()


#Modelar partido de tenis

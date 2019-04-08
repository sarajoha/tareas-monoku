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


samsung = Celular('Samsung', 'Galaxy J7 Duo', 'Android 8.0', '32GB', '4GB', '5.5"')

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


foo_f = Banda('Foo Fighters', 'Rock', ['Dave Grohl', 'Taylor Hawkins'], ['Concrete and Gold'],
                ['The Pretender', 'Everlong', 'Times like these'])

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
    def nuevo_nombre(self, nombre):
        self.__nombre = nombre

    def nuevo_artista(self, artista):
        self.__artista = artista


# alive = Cancion('Alive', 'Empire of the Sun')
#
# print(alive.nombre())
# print(alive.artista())
#
# alive.nuevo_nombre('Come Alive')
# print(alive.nombre())
# alive.nuevo_artista('Foo Fighters')
# print(alive.artista())


#Polimorfismo
class
#ponerle hijos a la clase
#hacer un metodo que puedan usar todos los hijos de la clase

#class genero musical, hijos merengue, salsa, bachata,
#todas las clases hijas tienen el metodo bailar, pero este es distinto para cada una
#ej, bachata paso paso cadera izq y derecha

#ejemplo 2
#animal clase padre, clases hijas gato, perro, hamster, pez
#metodo Polimorfismo comer = 'nom nom nom'
#necesidades fisiologicas, pis y pupu
#dormir = ZzZzZz



#Herencia



#Recoleccion de Basura



#Modelar partido de tenis

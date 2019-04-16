#import models

class Cliente(models.Model):
    saldo = FloatField()
    limiteCredito =
    descuento =
    #manytomany con Direccion
    #one to many con pedido PedidoCabecera


class Direccion(models.Model):
    numero = IntegerField()
    calle = CharField()
    comuna = CharField()
    ciudad = charField()


class PedidoCabecera(models.Model):
    fecha = DateField()
    #one to many con PedidoCuerpo


class PedidoCuerpo(models.Model):
    cantidad = IntegerField()


class Fabrica(models.Model):
    nombre = CharField()
    tlfContacto = IntegerField()
    #one to many articulos

class Articulo(models.Model):
    descripcion = CharField()

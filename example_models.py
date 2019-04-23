'''
Tarea de modelos de Django
'''
#import models
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=25)
    saldo = models.DecimalField()
    limite_credito = models.PositiveIntegerField(validators=[MaxValueValidator(3000000)])
    descuento = models.DecimalField()

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    numero = models.IntegerField()
    calle = models.CharField(max_length=30)
    comuna = models.CharField(max_length=20)
    ciudad = models.charField(max_length=20)
    cliente = models.ManyToManyField(Cliente)

    def __str__(self):
        return f'Calle {self.calle}, numero {self.numero}, {self.comuna}, {self.ciudad}'


class Fabrica(models.Model):
    nombre = models.CharField(max_length=50)
    tlf_contacto = models.PositiveIntegerField(max_length=10, validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField()
    fabrica = models.ForeignKey(Fabrica, on_delete=models.PROTECT))

    def __str__(self):
        return self.nombre


class PedidoCuerpo(models.Model):
    cantidad = models.PositiveIntegerField()
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.articulo}, {self.cantidad}'


class PedidoCabecera(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    pedido_cuerpo = models.ManyToManyField(PedidoCuerpo)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT))

    def __str__(self):
        return f'{self.cliente}, pedido: {self.pedido_cuerpo}, {self.fecha}'

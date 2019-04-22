#import models


class Cliente(models.Model):
    saldo = models.FloatField()
    limite_credito = models.PositiveIntegerField(validators=[MaxValueValidator(3000000)])
    descuento = models.FloatField()
    #direccion = models.ManyToManyField(Direccion)

class Direccion(models.Model):
    numero = models.IntegerField()
    calle = models.CharField(max_length=30)
    comuna = models.CharField(max_length=20)
    ciudad = models.charField(max_length=20)
    #cliente = models.ManyToManyField(Cliente)


class Fabrica(models.Model):
    nombre = models.CharField(max_length=50)
    tlf_contacto = models.PositiveIntegerField(max_length=10, validators=[MinLengthValidator(10)]) #minimo cifra de x numeros


class Articulo(models.Model):
    descripcion = CharField()
    fabrica = models.ForeignKey(Fabrica, on_delete=models.PROTECT))


class PedidoCuerpo(models.Model):
    cantidad = models.PositiveIntegerField()
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)


class PedidoCabecera(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    pedidoCuerpo = models.ManyToManyField(PedidoCuerpo)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT))

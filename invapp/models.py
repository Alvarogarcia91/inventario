from django.db import models

class Lote(models.model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    numero_de_lote = models.CharField(max_length=100)
    def __str__(self):
        return self.numero_de_lote

class Tipo_de_espuma(models.model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    modelo = models.CharField()
    especial = models.BooleanField()
    linea = models.BooleanField()
    def __str__(self):
        return self.modelo

class Tipo_de_unidad(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    descripcion = models.CharField(max_length = 100)
    def __str__(self):
        return self.descripcion
    # TIPOS_DE_UNIDAD = (
    # ('inicio','inicio'),
    # ('normal','normal'),
    # ('final','final'),
    # ('muestra','muestra'),
    # ('cambio','cambio')
    # )
    #reordenar 

class Defecto(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    descripcion =models.CharField(max_length =100)
    def __str__(self):
        return self.descripcion
#     DEFECTOS = (
#     ('pinhole','pinhole'),
#     ('grieta', 'grieta'),
#     ('vena', 'vena'),
#     ('mal manejo','mal manejo'),
#     ('fuera de medida', 'fuera de medida'),
#     ('algodonozo', 'algodonozo')
# )

class Figura(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion

class Maquina(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    figura = models.ForeignKey(Figura)
    modelo = models.CharField(max_length=200)
    numero = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion

class Block_de_espuma(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    figura = models.ForeignKey(Figura)
    tipo_de_espuma = models.ForeignKey(Tipo_de_espuma)
    maquina = models.ForeignKey(Maquina)
    numero_de_block = models.IntegerField('numero de block')
    tipo_de_unidad = models.ForeignKey(Tipo_de_unidad)
    #set default to normal
    lote = models.ForeignKey(Lote)
    defecto = models.ForeignKey(Question)
    desperdicio = models.BooleanField()
    curado = models.BooleanField()
    # MEDIDAS
    largo = models.DecimalField(max_digits=8, decimal_places=4)
    largo_curado = models.DecimalField(max_digits=8, decimal_places=4)
    ancho = models.DecimalField(max_digits=8, decimal_places=4)
    ancho_curado = models.DecimalField(max_digits=8, decimal_places=4)
    alto = models.DecimalField(max_digits=8, decimal_places=4, null=True)
    alto_curado = models.DecimalField(max_digits=8, decimal_places=4, null=True)
    flujo_de_aire = models.DecimalField(max_digits=8,decimal_places=4)
    peso = models.DecimalField(max_digits=8,decimal_places=4)
    def __str__(self):
        return (self.numero_de_block, self.figura, self.tipo_de_espuma)

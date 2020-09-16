from django.db import models

# Create your models here.

class ImpresoraDjango(models.Model):
  id = models.IntegerField(primary_key=True)
  nombre_impresora = models.TextField(max_length=50)
  modelo = models.TextField(max_length=50)
  marca = models.TextField(max_length=50) 
  fecha_compra = models.DateField(verbose_name='fecha de compra')
  ultimo_mantenimiento = models.DateField(verbose_name='fecha del ultimo mantenimiento')
  ubicacion_fisica = models.TextField(max_length=50)
  nombre_responsable = models.TextField(max_length=50)
  correo_responsable = models.EmailField()
  ip = models.TextField(max_length=50)
  
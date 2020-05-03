from django.db import models

# Create your models here.
'''
SOURCES: 
https://levipy.com/crear-api-rest-con-django-rest-framework
https://docs.djangoproject.com/en/3.0/ref/models/fields/
https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/
'''

class Ingrediente(models.Model):
    ''' INGREDIENTES! '''

    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

class Hamburguesa(models.Model):
    '''Clase correspondiente a Hamburguesa'''

    nombre = models.CharField(max_length=255)
    precio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=255)
    imagen = models.URLField()
    # publications = models.ManyToManyField(Publication)
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)


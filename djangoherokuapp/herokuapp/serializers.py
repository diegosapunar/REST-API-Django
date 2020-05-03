'''
SOURCES: 
https://levipy.com/crear-api-rest-con-django-rest-framework
https://docs.djangoproject.com/en/3.0/ref/models/fields/
https://stackoverflow.com/questions/33182092/django-rest-framework-serializing-many-to-many-field
https://www.django-rest-framework.org/api-guide/relations/
'''
_BASE_URL = "https://tarea2-sapunar.herokuapp.com/ingrediente/"

from rest_framework import serializers
from .models import Hamburguesa, Ingrediente


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'descripcion')

class IngredientePathSerializer(IngredienteSerializer):

    def to_representation(self,value):
        serializer = IngredienteSerializer(value)
        path = _BASE_URL + str(serializer.data['id'])
        return {"path": path}

class HamburguesaSerializer(serializers.ModelSerializer):
    # book_list = BookSerializer(many=True, read_only=True)
    ingredientes = IngredientePathSerializer(many=True, required=False)
    class Meta:
        model = Hamburguesa
        fields = ('id','nombre', 'precio',
                  'descripcion', 'imagen', 'ingredientes')

'''
SOURCES: 
https://levipy.com/crear-api-rest-con-django-rest-framework
https://docs.djangoproject.com/en/3.0/ref/models/fields/
'''

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from herokuapp.models import Hamburguesa, Ingrediente
from herokuapp.serializers import HamburguesaSerializer, IngredienteSerializer

_BASE_URL = "https://tarea2-sapunar.herokuapp.com/ingrediente/"

# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def index(request):
    return render(request, 'index.html', status=404)

@csrf_exempt
def hamburguesa_list(request):
    """
    List all code hamburguesa, or create a new hamburguesa.
    """

    if request.method == 'GET':
        hamburguesas = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(hamburguesas, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        
        data = JSONParser().parse(request)
        serializer = HamburguesaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def hamburguesa_detail(request, pk):
    """
    Retrieve, update or delete a hamburguesa.
    """
    try:
        hamburguesa = Hamburguesa.objects.get(pk=pk)

    except Hamburguesa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HamburguesaSerializer(hamburguesa)
        return JSONResponse(serializer.data)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = HamburguesaSerializer(hamburguesa, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        hamburguesa.delete()
        return HttpResponse(status=200)

@csrf_exempt
def ingrediente_list(request):
    """
    List all code ingrddiente, or create a ningrediente.
    """

    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IngredienteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def ingrediente_detail(request, pk):
    """
    Retrieve, update or delete a ingrediente.
    """

    try:
        ingrediente = Ingrediente.objects.get(pk=pk)

    except Ingrediente.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return JSONResponse(serializer.data)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = IngredienteSerializer(ingrediente, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        serializer = IngredienteSerializer(ingrediente)
        hamburguesas = Hamburguesa.objects.all()
        for burger in hamburguesas:
            serializer_burger = HamburguesaSerializer(burger)
            path = _BASE_URL + str(serializer.data['id'])

            for ingre in serializer_burger.data['ingredientes']:
                if ingre['path'] == path:
                    return HttpResponse(status=409)
        ingrediente.delete()
        return HttpResponse(status=200)

@csrf_exempt
def edit(request, pk1, pk2):
    try:
        ingrediente = Ingrediente.objects.get(pk=pk2)
        
    except Ingrediente.DoesNotExist:
        return HttpResponse(status=404)
    
    try:
        hamburguesa = Hamburguesa.objects.get(pk=pk1)
    except Hamburguesa.DoesNotExist:
        return HttpResponse(status=400)
        
    if request.method == 'PUT':
        hamburguesa.ingredientes.add(ingrediente)
        return HttpResponse(status=201)

    elif request.method == 'DELETE':
        hamburguesa.ingredientes.remove(ingrediente)
        return HttpResponse(status=200)

    else:
        return HttpResponse(status=404)
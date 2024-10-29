# persona_app/views.py
from django.core.serializers import deserialize

from persona_app.serializers import PersonaSerializer
from django.shortcuts import render
from django.http import JsonResponse
from persona_app.models import Persona
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def obtenerPerfil(request, id):
    try:
        perfil = Persona.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializado = PersonaSerializer(perfil)

    return Response(serializado.data,status=status.HTTP_200_OK)

# PUT = Actualizar, DELETE = Borrar
@api_view(['PUT','DELETE'])
def modificarPersona(request, id):
    try:
        persona = Persona.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Verificamos si es actualizar
    if request.method == 'PUT':
        # Serializamos la data que envió el usuario
        serializado = PersonaSerializer(persona, data=request.data)

        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=status.HTTP_200_OK)

        return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)

    # Verificamos si es eliminar
    if request.method == 'DELETE':
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def obtenerPersonas(request):
    # Por GET obtendremos todas las personas de la tabla
    # persona_app_persona
    if request.method == 'GET':
        # Obtener todas las personas desde la bd
        personas_obtenidas = Persona.objects.all()
        # Serializar los resultados desde la base de datos a JSON
        serializado = PersonaSerializer(personas_obtenidas, many=True)

        return Response(serializado.data, status=status.HTTP_200_OK)

    # Acceso POST para ingresar una nueva persona vía JSON
    if request.method == 'POST':
        deserializado = PersonaSerializer(data=request.data)
        # Valida que el JSON recibido es correcto según la estrucutra de tabla
        if deserializado.is_valid():
            # Graba el resultado en la BD
            deserializado.save()
            return Response(deserializado.data, status=status.HTTP_200_OK)
        else:
            # En caso de errores, devuelve los errores
            return Response(deserializado.errors, status=status.HTTP_400_BAD_REQUEST)


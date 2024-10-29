# persona_app/serializers.py
from rest_framework import serializers
from persona_app.models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
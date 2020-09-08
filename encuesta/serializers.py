from rest_framework import routers, serializers, viewsets

from .models import Encuesta, Pregunta, Opcion

class EncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuesta
        fields = '__all__'


class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ['opcion', 'votos']


class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many=True, read_only=True)
    class Meta:
        model = Pregunta
        fields = ['pregunta', 'opciones']




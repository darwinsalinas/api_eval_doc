from rest_framework import routers, serializers, viewsets

from .models import Encuesta

class EncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuesta
        fields = '__all__'

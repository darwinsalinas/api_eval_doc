from django.shortcuts import render
from rest_framework import viewsets


from .models import Encuesta
from .serializers import EncuestaSerializer

class EncuestaViewSet(viewsets.ModelViewSet):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer

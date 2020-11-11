from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


from .models import Encuesta, Pregunta, Opcion
from .serializers import EncuestaSerializer, PreguntaSerializer, OpcionSerializer

class EncuestaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer


class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class OpcionViewSet(viewsets.ModelViewSet):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer



class PreguntaSingle(RetrieveAPIView):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer

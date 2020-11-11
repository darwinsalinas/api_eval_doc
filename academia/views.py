from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .models import Docente, Estudiante, Curso
from .serializers import DocenteSerializer, EstudianteSerializer, CursoSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer


class EstudianteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from encuesta.views import EncuestaViewSet
from academia.views import DocenteViewSet, EstudianteViewSet, CursoViewSet


router = routers.DefaultRouter()
router.register(r'encuestas', EncuestaViewSet)
router.register(r'docentes', DocenteViewSet)
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'cursos', CursoViewSet)

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router.urls)),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from encuesta.views import EncuestaViewSet, PreguntaViewSet, OpcionViewSet, PreguntaSingle
from academia.views import DocenteViewSet, EstudianteViewSet, CursoViewSet

router = routers.DefaultRouter()
router.register(r'encuestas', EncuestaViewSet)
router.register(r'preguntas', PreguntaViewSet)
router.register(r'opciones', OpcionViewSet)
router.register(r'docentes', DocenteViewSet)
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'cursos', CursoViewSet)

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/preguntas/<int:pk>', PreguntaSingle.as_view()),
]

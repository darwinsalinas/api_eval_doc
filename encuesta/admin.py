from django.contrib import admin
from .models import Encuesta, Pregunta, Opcion


admin.site.register(Encuesta)


class OpcioAdmin(admin.TabularInline):
    model = Opcion

class PreguntaAdmin(admin.ModelAdmin):
   inlines = [OpcioAdmin,]

admin.site.register(Pregunta, PreguntaAdmin)



# gestor
# WFB+$d*t2$rNc2a
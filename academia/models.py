from django.db import models


class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    class Meta:
        abstract=True

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

class Docente(Persona):
    pass


class Estudiante(Persona):
    pass

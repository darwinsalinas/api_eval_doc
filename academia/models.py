from django.db import models

# from encuesta.models import Encuesta


class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    class Meta:
        abstract=True

    def __str__(self):
        return self.nombres + ' ' + self.apellidos


class Catalogo(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        abstract=True

    def __str__(self):
        return self.nombre


class Asignatura(Catalogo):
    pass


class Docente(Persona):
    pass


class Estudiante(Persona):
    encuestas = models.ManyToManyField('encuesta.Encuesta', blank=True)


class Curso(models.Model):
    asignatura = models.ForeignKey(Asignatura, models.CASCADE)
    docente = models.ForeignKey(Docente, models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, blank=True)

    def __str__(self):
        return "{} --- {}".format(self.asignatura, self.docente)

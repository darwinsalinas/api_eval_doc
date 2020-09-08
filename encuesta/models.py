from django.db import models

from academia.models import Curso


class Encuesta(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    curso = models.ForeignKey(Curso, models.CASCADE)

    def __str__(self):
        return "{} --- {}".format(self.titulo, self.curso)


class Pregunta(models.Model):
    encuesta = models.ForeignKey(Encuesta, models.CASCADE)
    pregunta = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.pregunta)


class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, models.CASCADE)
    opcion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return "{} -- {} ({})".format(self.pregunta, self.opcion, self.votos)

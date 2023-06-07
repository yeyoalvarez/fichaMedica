from django.db import models
from apps.pacientes.models.base import BaseModel
from django.utils import timezone
from .pacientes import *
from django.conf import settings
from django.contrib.auth.models import User


class consulta(models.Model):
    fecha_consulta = models.DateField(default=timezone.now)
    paciente = models.ForeignKey("paciente",
                                 on_delete=models.PROTECT, related_name="PacienteCon")
    medico = models.ForeignKey("medico",
                               on_delete=models.PROTECT, related_name="Medico")
    consulta_realizada = models.BooleanField(default=False, help_text = 'si esta check, el paciente ya consulto')

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'


class especialidad(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.nombre


class medico(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    ci = models.IntegerField(blank=False)
    especialidad = models.ForeignKey(especialidad, help_text='Especialidad', on_delete=models.CASCADE, blank=True,
                               related_name="Especialidad", null=True)

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

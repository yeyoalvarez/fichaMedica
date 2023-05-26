from django.db import models
from django.contrib.humanize.templatetags import humanize
from apps.pacientes.models.base import BaseModel


class servicio(BaseModel):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    precio = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'servicios'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return f" {self.nombre}"[:35]



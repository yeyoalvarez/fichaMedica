from django.db import models
from apps.pacientes.models.base import BaseModel


class seguro_medico(BaseModel):
    id_seguro_medico = models.AutoField(primary_key=True)
    nombre_seguro = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Seguro Medico'
        verbose_name_plural = 'Seguros Medicos'

    def __str__(self):
        return self.nombre_seguro


class paciente(BaseModel):
    GENERO = (
        ('Masculino', 'M'),
        ('Femenino', 'F')
    )
    TIPOS_SANGRE = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')
    )
    SIGNOS_SANGRE = (
        ('POSTIVO', '+'),
        ('NEGATIVO', '-')
    )
    id_paciente = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    ci = models.IntegerField(blank=False)
    genero = models.CharField(choices=GENERO, max_length=10, blank=False)
    tipo_sangre = models.CharField(choices=TIPOS_SANGRE, max_length=8, blank=True)
    signo_sangre = models.CharField(choices=SIGNOS_SANGRE, max_length=8, blank=True)
    seguro = models.ForeignKey(seguro_medico, on_delete=models.CASCADE, blank=True,
                               related_name="Seguro_Medico", null=True)
    numero_seguro = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True)
    telefono = models.IntegerField(blank=True, null=True)
    notas = models.CharField(max_length=500, blank=True)

    def get_full_name(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class historial_paciente(BaseModel):
    paciente = models.ForeignKey("paciente",
                                 on_delete=models.PROTECT, related_name="Ficha")
    temperatura = models.IntegerField(blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    altura = models.IntegerField(blank=True, null=True)
    sintomas = models.CharField(max_length=500, blank=True)
    diagnostico = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Historial Paciente'
        verbose_name_plural = 'Historial Pacientes'

    def __str__(self):
        return f" {self.paciente.nombres} {self.paciente.apellidos} Fecha {self.creado.date()}"


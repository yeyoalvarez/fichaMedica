from django.db import models
from apps.pacientes.models.base import BaseModel
from django.utils import timezone



class seguro_medico(models.Model):
    nombre_seguro = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Seguro Medico'
        verbose_name_plural = 'Seguros Medicos'

    def __str__(self):
        return self.nombre_seguro

class paciente(models.Model):
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
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    ci = models.IntegerField(blank=False)
    genero = models.CharField(choices=GENERO, max_length=10, blank=False)
    tipo_sangre = models.CharField(choices=TIPOS_SANGRE, max_length=8, blank=True)
    signo_sangre = models.CharField('', help_text='Tipo de sangre ej: A+, AB-', choices=SIGNOS_SANGRE, max_length=8, blank=True)
    seguro = models.ForeignKey(seguro_medico, help_text='Seguro Medico', on_delete=models.CASCADE, blank=True,
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
    fecha_consulta = models.DateField(default=timezone.now)
    paciente = models.ForeignKey("paciente",
                                 on_delete=models.PROTECT, related_name="Paciente")
    temperatura = models.IntegerField(blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    indice_masa = models.FloatField(blank=True, null=True)
    hipertension_arterial = models.FloatField(blank=True, null=True)
    altura = models.IntegerField(blank=True, null=True)
    sintomas = models.CharField(max_length=500, blank=True)
    diagnostico = models.CharField(max_length=500, blank=True)
    estudios = models.ImageField(upload_to='estudios/', blank=True, null=True)
    triaje = models.ForeignKey("triaje",
                                 on_delete=models.PROTECT, related_name="Triajes", blank=True, null=True)

    class Meta:
        verbose_name = 'Historial Del Paciente'
        verbose_name_plural = 'Historial del Paciente'


    def get_fecha_creacion(self):
        return f"Fecha {self.creado.date()}"

class triaje(BaseModel):
    paciente = models.ForeignKey("paciente",
                                 on_delete=models.PROTECT, related_name="PacienteTriaje")
    frecuencia_cardiaca = models.FloatField(blank=True, null=True, default=0)
    frecuencia_respiratoria = models.FloatField(blank=True, null=True, default=0)
    saturacion = models.FloatField(blank=True, null=True, default=0)
    fecha_consulta = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Triajes'
        verbose_name_plural = 'Triajes'

    def __str__(self):
        return f"{self.paciente} Fecha {self.fecha_consulta}"

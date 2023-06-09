from django.db import models
from apps.pacientes.models.base import BaseModel
from django.utils import timezone
from .consultas import consulta
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete


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
    signo_sangre = models.CharField('', help_text='Tipo de sangre ej: A+, AB-', choices=SIGNOS_SANGRE, max_length=8,
                                    blank=True)
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
    motivo_consulta = models.CharField(max_length=500, blank=True)
    sintomas = models.CharField(max_length=500, blank=True)
    diagnostico = models.CharField(max_length=500, blank=True)
    tratamiento = models.CharField(max_length=500, blank=True)
    app = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Historial Del Paciente'
        verbose_name_plural = 'Historial del Paciente'

    def get_fecha_creacion(self):
        return f"Fecha {self.creado.date()}"


# instance es el registro que se maneja
@receiver([post_save], sender=paciente)
def update_consulta(sender, instance, **kwargs):
    if con := consulta.objects.filter(paciente=instance).last():
        con.consulta_realizada = True
        con.save()


class imagenEstudios(models.Model):
    imagen = models.ImageField(upload_to='estudios/', blank=True, null=True)
    estudio = models.ForeignKey(paciente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Estudio'
        verbose_name_plural = 'Estudios'


class triaje(BaseModel):
    paciente = models.ForeignKey("paciente",
                                 on_delete=models.PROTECT, related_name="PacienteTriaje")
    frecuencia_cardiaca = models.FloatField(blank=True, null=True, default=0)
    frecuencia_respiratoria = models.FloatField(blank=True, null=True, default=0)
    saturacion = models.FloatField(blank=True, null=True, default=0)
    temperatura = models.IntegerField(blank=True, null=True)
    peso = models.IntegerField(help_text='en kg', blank=True, null=True, default=0)
    altura = models.IntegerField(help_text='en cm', blank=True, null=True, default=0)
    fecha_consulta = models.DateField(default=timezone.now)
    indice_masa = models.FloatField(blank=True, null=True, default=0,)

    class Meta:
        verbose_name = 'Triajes'
        verbose_name_plural = 'Triajes'

    def __str__(self):
        return f"{self.paciente} Fecha {self.fecha_consulta}"

    def save(self):
        self.indice_masa = (self.peso / (self.altura * self.altura)) / 0.0001
        return super(triaje, self).save()
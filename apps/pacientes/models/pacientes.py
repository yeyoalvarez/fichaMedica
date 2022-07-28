from django.db import models

class seguro_medico (models.Model):
    nombre_seguro = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Seguro Medico'
        verbose_name_plural = 'Seguros Medicos'

    def __str__(self):
        return self.nombre_seguro

class paciente(models.Model):
    GENERO=(
        ('Masculino','M'),
        ('Femenino','F')
    )
    TIPOS_SANGRE=(
        ('A','A'),
        ('B','B'),
        ('AB','AB'),
        ('O','O')
    )
    SIGNOS_SANGRE=(
        ('POSTIVO','+'),
        ('NEGATIVO','-')
    )
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    ci = models.IntegerField(blank=False)
    genero = models.CharField(choices=GENERO, max_length=10, blank=False)
    tipo_sangre = models.CharField(choices=TIPOS_SANGRE, max_length=8,blank=True)
    signo_sangre = models.CharField(choices=SIGNOS_SANGRE, max_length=8,blank=True)
    seguro = models.ForeignKey(seguro_medico, on_delete=models.CASCADE,blank=True, related_name="Seguro_Medico")
    numero_seguro = models.IntegerField(blank=True)
    direccion = models.CharField(max_length=255,blank=True)
    telefono = models.IntegerField(blank=True)
    notas = models.CharField(max_length=500,blank=True)

    def get_full_name(self):
        return f"{self.grado} {self.nombres} {self.apellidos}"

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
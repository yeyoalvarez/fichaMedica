from django.contrib import admin
from .models.pacientes import *


@admin.register(historial_paciente)
class historial_pacienteAdmin(admin.ModelAdmin):
    list_display = ['temperatura', 'peso']


@admin.register(paciente)
class pacienteAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'ci']


@admin.register(seguro_medico)
class seguro_medicoAdmin(admin.ModelAdmin):
    list_display = ['nombre_seguro']


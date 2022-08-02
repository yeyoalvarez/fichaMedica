from django.contrib import admin
from .models.pacientes import *


class historial_pacienteAdmin(admin.TabularInline):
    model = historial_paciente
    extra = 2

@admin.register(paciente)
class pacienteAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'ci']
    inlines = [historial_pacienteAdmin]


@admin.register(seguro_medico)
class seguro_medicoAdmin(admin.ModelAdmin):
    list_display = ['nombre_seguro']


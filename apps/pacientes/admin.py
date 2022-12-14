from django.contrib import admin
from .models.pacientes import *


class historial_pacienteAdmin(admin.TabularInline):
    model = historial_paciente
    extra = 1


class triaje_pacienteAdmin(admin.TabularInline):
    model = triaje
    extra = 1


@admin.register(paciente)
class pacienteAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'ci']
    inlines = [historial_pacienteAdmin, triaje_pacienteAdmin]
    search_fields = ['nombres','apellidos', 'ci']
    fieldsets = (
            ('Datos Personales',{
                'fields': ('nombres','apellidos',
                        ('ci', 'genero'),
                        ('tipo_sangre','signo_sangre'),
                        ('seguro','numero_seguro'),
                        ('direccion'), 'telefono')
            }),
    )

@admin.register(seguro_medico)
class seguro_medicoAdmin(admin.ModelAdmin):
    list_display = ['nombre_seguro']
    search_fields = ['nombre_seguro']

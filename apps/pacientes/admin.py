from django.contrib import admin
from .models.pacientes import *
from django.forms import Textarea
from django.utils.html import format_html
import PIL as pillow
from PIL import Image
from .models.consultas import *


class historial_pacienteAdmin(admin.StackedInline):
    model = historial_paciente
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 10, 'cols': 80})},
    }
    list_display = ['admin_estudio']

    class Media:
        js = ['js/collapsed-stacked-inlines.js']


class triaje_pacienteAdmin(admin.TabularInline):
    model = triaje
    extra = 0
    classes = ['collapse']


class imagenEstudiosAdmin(admin.TabularInline):
    model = imagenEstudios
    extra = 0
    classes = ['collapse']


@admin.register(paciente)
class pacienteAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'ci', ]
    inlines = [historial_pacienteAdmin, triaje_pacienteAdmin, imagenEstudiosAdmin]
    search_fields = ['nombres', 'apellidos', 'ci']
    fieldsets = (
        ('Datos Personales', {
            'fields': (('nombres', 'apellidos'),
                       ('ci', 'genero'),
                       ('tipo_sangre', 'signo_sangre'),
                       ('seguro', 'numero_seguro'),
                       ('direccion', 'telefono'))
        }),
    )


@admin.register(seguro_medico)
class seguro_medicoAdmin(admin.ModelAdmin):
    list_display = ['nombre_seguro']
    search_fields = ['nombre_seguro']


@admin.register(especialidad)
class especialidadAdmin(admin.ModelAdmin):
    model = especialidad
    search_fields = ['nombre']


@admin.register(medico)
class medicoAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'ci']
    search_fields = ['nombres', 'apellidos', 'especialidad', 'ci']
    autocomplete_fields = ['especialidad']


@admin.register(consulta)
class consultaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'fecha_consulta', 'medico',]
    autocomplete_fields = ['paciente', 'medico']


admin.site.register(triaje)

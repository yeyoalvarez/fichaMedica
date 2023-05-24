from django.contrib import admin
from .models.pacientes import *
from django.forms import Textarea
from django.utils.html import format_html
import PIL as pillow
from PIL import Image

class historial_pacienteAdmin(admin.StackedInline):
    model = historial_paciente
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 10, 'cols': 80})},
    }
    #
    # def imagen(self, obj):
    #     return format_html('<img src= {} width="130" height="100" />', obj.estudios.url)
    list_display = ['admin_estudio']
    list_per_page = 1


class triaje_pacienteAdmin(admin.TabularInline):
    model = triaje
    extra = 0


class imagenEstudiosAdmin(admin.TabularInline):
    model = imagenEstudios
    extra = 0


@admin.register(paciente)
class pacienteAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'ci', ]
    inlines = [historial_pacienteAdmin, triaje_pacienteAdmin, imagenEstudiosAdmin]
    search_fields = ['nombres', 'apellidos', 'ci']
    fieldsets = (
        ('Datos Personales', {
            'fields': ('nombres', 'apellidos',
                       ('ci', 'genero'),
                       ('tipo_sangre', 'signo_sangre'),
                       ('seguro', 'numero_seguro'),
                       ('direccion'), 'telefono')
        }),
    )


@admin.register(seguro_medico)
class seguro_medicoAdmin(admin.ModelAdmin):
    list_display = ['nombre_seguro']
    search_fields = ['nombre_seguro']


admin.site.register(triaje)

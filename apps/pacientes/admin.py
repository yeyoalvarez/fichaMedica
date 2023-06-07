from django.contrib import admin
from .models.pacientes import *
from django.forms import Textarea
from django.utils.html import format_html
import PIL as pillow
from PIL import Image
from .models.consultas import *
from django.views.generic.detail import DetailView
from rangefilter.filters import DateRangeFilter


class historial_pacienteAdmin(admin.StackedInline, DetailView):
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


@admin.register(consulta)
class consultaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'fecha_consulta', 'medico', 'consulta_realizada']
    autocomplete_fields = ['paciente', 'medico']
    list_filter = [('fecha_consulta', DateRangeFilter),]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.medico.usuario = request.user
        return form


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

    def get_context_data(self, **kwargs):
        context = super(historial_pacienteAdmin, self).historial_pacienteAdmin(**kwargs)
        obj = self.pacientes_consulta.get_object()
        obj.pacientes_consulta.consulta_realizada = True
        obj.save()

        return context


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
    autocomplete_fields = ['especialidad', 'usuario',]


admin.site.register(triaje)

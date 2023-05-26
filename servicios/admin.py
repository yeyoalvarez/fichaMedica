from django.contrib import admin
from django.contrib.humanize.templatetags import humanize
from .models import *


@admin.register(servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio"]
    search_fields = ["nombre"]

    @admin.display(description='Precio', ordering="precio", empty_value=0)
    def monto_formated(self, obj):
        return humanize.intcomma(obj.precio)

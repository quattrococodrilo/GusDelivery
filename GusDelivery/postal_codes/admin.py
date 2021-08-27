from django.contrib import admin
from .models import Estado, Municipio, Asentamiento, CodigoPostal

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    pass

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    pass

@admin.register(Asentamiento)
class AsentamientoAdmin(admin.ModelAdmin):
    pass

@admin.register(CodigoPostal)
class CodigoPostalAdmin(admin.ModelAdmin):
    pass
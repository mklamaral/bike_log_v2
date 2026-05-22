from django.contrib import admin
from .models import Bike, Component, MaintenanceRecord
# Register your models here.


class MaintenanceInline(admin.TabularInline):
    model = MaintenanceRecord
    extra = 1

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    # Aqui você coloca os nomes dos campos que estão no seu model Bike
    list_display = ("brand", "name", "model", "created_at")
    
    # Isso coloca uma barra de busca no topo do admin para encontrar bikes por marca ou nome
    search_fields = ("brand", "name")

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "kilometers", "bike", "status_manutencao")
    list_filter = ("category", "name") # Cria filtros laterais para facilitar a busca
    inlines = [MaintenanceInline] # Mostra as manutenções direto na tela do componente
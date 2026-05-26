from django.contrib import admin
from .models import Bike, Component, MaintenanceRecord, Ride
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
    ordering = ('-kilometers',)
    inlines = [MaintenanceInline] # Mostra as manutenções direto na tela do componente

@admin.register(Ride) # Isso substitui o admin.site.register(Ride)
class RideAdmin(admin.ModelAdmin):
    # 1. Colunas que aparecem na listagem (as colunas da tabela)
    list_display = ('id', 'bike', 'distance', 'date', 'short_description')
    readonly_fields = ("date",)
    
    # 2. Links clicáveis (o que abre o registro para edição)
    list_display_links = ('id', 'distance')
    
    # 3. Filtros na barra lateral (essencial para listas longas)
    list_filter = ('date', 'bike')
    
    # 4. Busca rápida no topo
    search_fields = ('description', 'bike__name')
    
    # 5. Organização da tela de edição (agrupamento de campos)
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('bike', 'distance', 'date')
        }),
        ('Detalhes', {
            'fields': ('description',),
            'classes': ('collapse',) # Opcional: cria uma seção retrátil
        }),
    )

    # 6. Método para exibir dados customizados (exemplo: encurtar descrição)
    def short_description(self, obj):
        return obj.description[:30] + '...' if len(obj.description) > 30 else obj.description
    short_description.short_description = 'Descrição Curta'
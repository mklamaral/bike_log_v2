from django.db import models
from django.utils.safestring import mark_safe
from .bike import Bike

class Component(models.Model):
    class Category(models.IntegerChoices):
        FREIO = 1, "Freio"
        TRANSMISSAO = 2, "Transmissão"
        SUSPENSAO = 3, "Suspensão"
        RODAS = 4, "Rodas"
        DIRECAO = 5, "Direção (Guidão/Mesa/Caixa)"
        SELIM = 6, "Selim e Canote"
        QUADRO = 7, "Quadro"
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='components')
    name = models.CharField(max_length=100)
    category = models.IntegerField(choices=Category.choices)
    kilometers = models.FloatField(default=0.0, help_text="Quilometragem acumulada no componente")
    install_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.kilometers}km)"
    
    max_kilometers = models.FloatField(default=2000.0, help_text="Quilometragem máxima para manutenção")
    
    def status_manutencao(self):
        if self.kilometers >= self.max_kilometers:
            return mark_safe('<span style="color: red; font-weight: bold;">⚠️ URGENTE</span>')
        elif self.kilometers >= (self.max_kilometers *0.8):
            return mark_safe('<span style="color: orange;">⚠️ Atenção</span>')
        return mark_safe('<span style="color: green;">✅ Em dia</span>')
    status_manutencao.short_description = 'Status' # Nome da coluna no admin
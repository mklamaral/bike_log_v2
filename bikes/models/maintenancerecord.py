from django.db import models

from .component import Component

class MaintenanceRecord(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='maintence_records')
    date = models.DateField()
    description = models.TextField()
    kilometers_at_service = models.FloatField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"Manutenção em {self.component.name} ({self.date})"
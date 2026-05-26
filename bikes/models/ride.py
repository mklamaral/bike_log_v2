from django.db import models
from .bike import Bike

class Ride(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name="rides")
    date = models.DateField(auto_now_add=True)
    distance = models.FloatField(help_text="Distância em KM")
    description = models.CharField(max_length=200, blank=True)
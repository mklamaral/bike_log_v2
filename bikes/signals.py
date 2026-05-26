from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models.ride import Ride
from .services import adicionar_pedal, remover_pedal

@receiver(post_save, sender=Ride)
def handle_ride_save(sender, instance, created, **kwargs):
    """
    Sempre que um Ride for criado, atualiza o km de todos os componentes da bike.
    """
    if created:
        adicionar_pedal(instance.bike, instance.distance)

@receiver(post_delete, sender=Ride)
def handle_ride_delete(sender, instance, **kwargs):
    """
    Sempre que um Ride for deletado, subtrai o km de todos os componentes da bike.
    """
    remover_pedal(instance.bike, instance.distance)
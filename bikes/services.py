from .models.ride import Ride

def adicionar_pedal(bike, distancia):
    """
    Esta função encapsula toda a lógica de atualizar os componentes
    """
    # Cria o pedal
    novo_pedal = Ride.objects.create(bike=bike, distance=distancia)
    
    # Atualiza os componentes
    for comp in bike.components.all():
        comp.kilometers += distancia
        comp.save()
        
    return novo_pedal


def remover_pedal(bike, distancia):
    """
    Regra de negócio contralizada para reverter quilometragem
    """
    for comp in bike.components.all():
        comp.kilometers = max(0, comp.kilometers - distancia)
        comp.save()
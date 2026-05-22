from rest_framework import viewsets
from bikes.models.bike import Bike
from bikes.serializers.bike import BikeSerializer

class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
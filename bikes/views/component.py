from rest_framework import viewsets
from bikes.models.component import Component
from bikes.serializers.component import ComponentSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
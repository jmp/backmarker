from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.models.circuit import Circuit
from backmarker.api.serializers.circuit_serializer import CircuitSerializer


class CircuitViewSet(ReadOnlyModelViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
    lookup_field = "reference"

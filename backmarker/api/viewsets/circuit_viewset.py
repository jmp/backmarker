from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.api.serializers.circuit_serializer import CircuitSerializer
from backmarker.models.circuit import Circuit


class CircuitViewSet(ReadOnlyModelViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
    lookup_field = "reference"

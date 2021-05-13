from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Circuit
from .serializers import CircuitSerializer


class CircuitViewSet(ReadOnlyModelViewSet):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
    lookup_field = "reference"

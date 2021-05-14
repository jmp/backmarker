from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Driver
from .serializers import DriverSerializer


class DriverViewSet(ReadOnlyModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = "reference"

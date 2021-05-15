from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.models.driver import Driver
from backmarker.api.serializers.driver_serializer import DriverSerializer


class DriverViewSet(ReadOnlyModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = "reference"

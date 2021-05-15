from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.api.serializers.driver_serializer import DriverSerializer
from backmarker.models.driver import Driver


class DriverViewSet(ReadOnlyModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = "reference"

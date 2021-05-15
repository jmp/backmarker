from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.models.driver_standing import DriverStanding
from backmarker.api.serializers.driver_standing_serializer import DriverStandingSerializer


class DriverStandingViewSet(ReadOnlyModelViewSet):
    queryset = DriverStanding.objects.all()
    serializer_class = DriverStandingSerializer

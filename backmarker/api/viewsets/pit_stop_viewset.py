from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.models.pit_stop import PitStop
from backmarker.api.serializers.pit_stop_serializer import PitStopSerializer


class PitStopViewSet(ReadOnlyModelViewSet):
    queryset = PitStop.objects.all()
    serializer_class = PitStopSerializer

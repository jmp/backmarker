from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.api.serializers.pit_stop_serializer import PitStopSerializer
from backmarker.models.pit_stop import PitStop


class PitStopViewSet(ReadOnlyModelViewSet):
    queryset = PitStop.objects.all()
    serializer_class = PitStopSerializer

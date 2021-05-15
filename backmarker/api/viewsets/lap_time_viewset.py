from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.api.serializers.lap_time_serializer import LapTimeSerializer
from backmarker.models.lap_time import LapTime


class LapTimeViewSet(ReadOnlyModelViewSet):
    queryset = LapTime.objects.all()
    serializer_class = LapTimeSerializer

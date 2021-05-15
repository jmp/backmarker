from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.models.race import Race
from backmarker.api.serializers.race_serializer import RaceSerializer


class RaceViewSet(ReadOnlyModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.api.serializers.race_serializer import RaceSerializer
from backmarker.models.race import Race


class RaceViewSet(ReadOnlyModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

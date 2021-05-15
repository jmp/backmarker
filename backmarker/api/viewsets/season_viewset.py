from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.models.season import Season
from backmarker.api.serializers.season_serializer import SeasonSerializer


class SeasonViewSet(ReadOnlyModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

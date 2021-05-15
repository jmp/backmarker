from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.api.serializers.season_serializer import SeasonSerializer
from backmarker.models.season import Season


class SeasonViewSet(ReadOnlyModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

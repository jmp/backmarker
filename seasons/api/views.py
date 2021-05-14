from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Season
from .serializers import SeasonSerializer


class SeasonViewSet(ReadOnlyModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

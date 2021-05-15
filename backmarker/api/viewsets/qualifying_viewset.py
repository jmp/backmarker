from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.models.qualifying import Qualifying
from backmarker.api.serializers.qualifying_serializer import QualifyingSerializer


class QualifyingViewSet(ReadOnlyModelViewSet):
    queryset = Qualifying.objects.all()
    serializer_class = QualifyingSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet

from backmarker.api.serializers.qualifying_serializer import QualifyingSerializer
from backmarker.models.qualifying import Qualifying


class QualifyingViewSet(ReadOnlyModelViewSet):
    queryset = Qualifying.objects.all()
    serializer_class = QualifyingSerializer

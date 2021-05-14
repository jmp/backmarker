from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Qualifying
from .serializers import QualifyingSerializer


class QualifyingViewSet(ReadOnlyModelViewSet):
    queryset = Qualifying.objects.all()
    serializer_class = QualifyingSerializer
